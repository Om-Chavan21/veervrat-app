import React, { useState, useEffect, useNavigate } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import {
    Box,
    TextField,
    Button,
    Autocomplete,
    IconButton,
} from "@mui/material";
import InputAdornment from "@mui/material/InputAdornment";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

function SignUpForm() {
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");
    const [dalOptions, setDalOptions] = useState([]);
    const [selectedDal, setSelectedDal] = useState(null);
    const [whatsappNumber, setWhatsappNumber] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [confirmPassword, setConfirmPassword] = useState("");
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [errors, setErrors] = useState({
        nameEn: "",
        dal: "",
        whatsappNumber: "",
        email: "",
        password: "",
        confirmPassword: "",
    });
    const [formSubmitted, setFormSubmitted] = useState(false);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/dals/`)
            .then((response) => {
                const dals = response.data.map((dal) => ({
                    label: dal.short_name.en,
                    value: dal._id,
                    shortNameMr: dal.short_name.mr,
                }));
                setDalOptions(dals);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const validateForm = () => {
        let hasErrors = false;
        const newErrors = { ...errors };

        if (!nameEn) {
            newErrors.nameEn = "Name in English is required";
            hasErrors = true;
        } else {
            newErrors.nameEn = "";
        }

        if (!selectedDal) {
            newErrors.dal = "Please select a dal";
            hasErrors = true;
        } else {
            newErrors.dal = "";
        }

        if (!whatsappNumber || whatsappNumber.length < 10) {
            newErrors.whatsappNumber = "WhatsApp number must be 10 digits";
            hasErrors = true;
        } else {
            newErrors.whatsappNumber = "";
        }

        if (!email || !email.includes("@")) {
            newErrors.email = "Invalid email";
            hasErrors = true;
        } else {
            newErrors.email = "";
        }

        if (!password || password.length < 8) {
            newErrors.password = "Password must be at least 8 characters long";
            hasErrors = true;
        } else {
            newErrors.password = "";
        }

        if (!confirmPassword || confirmPassword !== password) {
            newErrors.confirmPassword = "Passwords do not match";
            hasErrors = true;
        } else {
            newErrors.confirmPassword = "";
        }

        setErrors(newErrors);
        return hasErrors;
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
        if (formSubmitted) {
            if (e.target.value.length < 8) {
                setErrors((prevErrors) => ({
                    ...prevErrors,
                    password: "Password must be at least 8 characters long",
                }));
            } else {
                setErrors((prevErrors) => ({ ...prevErrors, password: "" }));
            }
        }
    };

    const handleConfirmPasswordChange = (e) => {
        setConfirmPassword(e.target.value);
        if (formSubmitted) {
            if (e.target.value !== password) {
                setErrors((prevErrors) => ({
                    ...prevErrors,
                    confirmPassword: "Passwords do not match",
                }));
            } else {
                setErrors((prevErrors) => ({
                    ...prevErrors,
                    confirmPassword: "",
                }));
            }
        }
    };

    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true);
        if (validateForm()) {
            return;
        }
        try {
            const user = {
                name: { en: nameEn, mr: nameMr },
                description: { en: descriptionEn, mr: descriptionMr },
                dal_id: selectedDal?.value,
                whatsappNumber: whatsappNumber,
                email: email,
                password: password,
            };
            
            await axios.post(`${import.meta.env.VITE_API_URL}/users/`, user);
            toast.success("User created successfully! Please log in.");
            navigate('/login');
            
            // Clear form fields
            setNameEn("");
            setNameMr("");
            setDescriptionEn("");
            setDescriptionMr("");
            setSelectedDal(null);
            setWhatsappNumber("");
            setEmail("");
            setPassword("");
            setConfirmPassword("");
        } catch (error) {
            console.error(error);
            if (error.response && error.response.status === 400) {
                if (error.response.data.detail.includes("Email already exists")) {
                    toast.error("Email already exists");
                } else if (error.response.data.detail.includes("User with this Phone Number already exists")) {
                    toast.error("User with this phone number already exists");
                } else {
                    toast.error("Failed to create user. Please try again.");
                }
            } else {
                toast.error("Failed to create user. Please try again.");
            }
        }
    };

    return (
        <Box
            className="flex justify-center items-center h-screen"
            sx={{ padding: 0 }}
        >
            <form
                onSubmit={handleSubmit}
                className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-md"
            >
                <h2 className="text-lg font-bold mb-4">Sign Up</h2>
                <TextField
                    label="Name (English)"
                    value={nameEn}
                    onChange={(e) => setNameEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    error={!!errors.nameEn}
                    helperText={errors.nameEn}
                    required
                />
                <Autocomplete
                    disablePortal
                    id="dal-select"
                    options={dalOptions}
                    sx={{ width: "100%", marginBottom: 2 }}
                    renderInput={(params) => (
                        <TextField
                            {...params}
                            label="Select Dal"
                            className="w-full"
                            error={!!errors.dal}
                            helperText={errors.dal}
                        />
                    )}
                    value={selectedDal}
                    onChange={(event, value) => {
                        setSelectedDal(value);
                        setFormSubmitted(false);
                    }}
                    getOptionLabel={(option) => option.label}
                    isOptionEqualToValue={(option, value) =>
                        option.value === value?.value
                    }
                    required
                />
                <TextField
                    label="WhatsApp Number"
                    value={whatsappNumber}
                    onChange={(e) => setWhatsappNumber(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    error={!!errors.whatsappNumber}
                    helperText={errors.whatsappNumber}
                    slotProps={{
                        input: {
                            startAdornment: (
                                <InputAdornment position="start">
                                    +91
                                </InputAdornment>
                            ),
                        },
                    }}
                    required
                />
                <TextField
                    label="Email ID"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    type="email"
                    error={!!errors.email}
                    helperText={errors.email}
                    required
                />

                <TextField
                    label="Create Password"
                    type={showPassword ? "text" : "password"}
                    value={password}
                    onChange={handlePasswordChange}
                    sx={{ marginBottom: 2 }}
                    error={!!errors.password}
                    helperText={errors.password}
                    slotProps={{
                        input: {
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton
                                        aria-label="toggle password visibility"
                                        onClick={() =>
                                            setShowPassword(!showPassword)
                                        }
                                    >
                                        {showPassword ? (
                                            <VisibilityOff />
                                        ) : (
                                            <Visibility />
                                        )}
                                    </IconButton>
                                </InputAdornment>
                            ),
                        },
                    }}
                    className="w-full"
                    required
                />
                <TextField
                    label="Confirm Password"
                    type={showConfirmPassword ? "text" : "password"}
                    value={confirmPassword}
                    onChange={handleConfirmPasswordChange}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    error={!!errors.confirmPassword}
                    helperText={errors.confirmPassword}
                    slotProps={{
                        input: {
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton
                                        aria-label="toggle password visibility"
                                        onClick={() =>
                                            setShowConfirmPassword(
                                                !showConfirmPassword
                                            )
                                        }
                                    >
                                        {showConfirmPassword ? (
                                            <VisibilityOff />
                                        ) : (
                                            <Visibility />
                                        )}
                                    </IconButton>
                                </InputAdornment>
                            ),
                        },
                    }}
                    required
                />
                <Button type="submit" variant="contained" className="w-full">
                    Create
                </Button>
            </form>
        </Box>
    );
}

export default SignUpForm;
