from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from bson.objectid import ObjectId
from app.database.mongodb import users
from app.models.schemas import UserCreate, User
from passlib.context import CryptContext
import datetime
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key for JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()


# Helper function to hash password
def hash_password(password):
    return pwd_context.hash(password)


# Helper function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Helper function to create JWT token
def create_access_token(data: dict, expires_delta: datetime.timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Helper function to get current user from token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await users.find_one({"email": email})
    if user is None:
        raise credentials_exception
    return user


@router.delete("/users/super-delete")
async def super_delete_weaknesses():
    try:
        await users.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


# Create user endpoint
@router.post("/users/", response_model=User)
async def create_user(user_data: UserCreate):
    # Check if email already exists
    if await users.find_one({"whatsappNumber": user_data.whatsappNumber}):
        raise HTTPException(
            status_code=400, detail="User with this Phone Number already exists"
        )

    # Check if email already exists
    if await users.find_one({"email": user_data.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    # Hash password
    user_data.password = hash_password(user_data.password)

    # Insert user into database
    result = await users.insert_one(user_data.dict())
    created_user = await users.find_one({"_id": result.inserted_id})

    # Convert _id to string
    created_user["_id"] = str(created_user["_id"])

    return created_user


# Login endpoint
@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Generate JWT token
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Get user endpoint
@router.get("/users/me", response_model=User)
async def get_user(current_user: dict = Depends(get_current_user)):
    user = await users.find_one({"email": current_user["email"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user
