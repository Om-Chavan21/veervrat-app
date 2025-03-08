import motor.motor_asyncio
from app.config import MONGODB_URL, DATABASE_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Collections
weaknesses = db.weaknesses
main_virtues = db.main_virtues
subvirtues = db.subvirtues
questions = db.questions
dals = db.dals
users = db.users
questionnaires = db.questionnaires
