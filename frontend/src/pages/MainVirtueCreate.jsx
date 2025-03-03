import React, { useState } from "react";
import axios from "axios";
import { Box, TextField, Button } from "@mui/material";

function CreateMainVirtue() {
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        const virtue = {
            name: { en: nameEn, mr: nameMr },
            description: { en: descriptionEn, mr: descriptionMr },
        };

        axios
            .post(`${import.meta.env.VITE_API_URL}/main-virtues/`, virtue)
            .then(() => {
                window.location.href = "/main-virtues";
            })
            .catch((error) => {
                console.error(error);
            });
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
                <h2 className="text-lg font-bold mb-4">Create Main Virtue</h2>
                <TextField
                    label="Name (English)"
                    value={nameEn}
                    onChange={(e) => setNameEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                />
                <TextField
                    label="Name (Marathi)"
                    value={nameMr}
                    onChange={(e) => setNameMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                />
                <TextField
                    label="Description (English)"
                    value={descriptionEn}
                    onChange={(e) => setDescriptionEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    multiline
                    rows={1}
                    disabled
                />
                <TextField
                    label="Description (Marathi)"
                    value={descriptionMr}
                    onChange={(e) => setDescriptionMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                    className="w-full"
                    multiline
                    rows={1}
                    disabled
                />
                <Button type="submit" variant="contained" className="w-full">
                    Create
                </Button>
            </form>
        </Box>
    );
}

export default CreateMainVirtue;
