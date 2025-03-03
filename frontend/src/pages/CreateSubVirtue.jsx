import React, { useState } from "react";
import axios from "axios";
import { Box, TextField, Button } from "@mui/material";

function CreateSubVirtue() {
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");
    const [mainVirtueId, setMainVirtueId] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        const subVirtue = {
            name: { en: nameEn, mr: nameMr },
            description: { en: descriptionEn, mr: descriptionMr },
            main_virtue_id: mainVirtueId,
        };

        axios
            .post(`${import.meta.env.VITE_API_URL}/subvirtues/`, subVirtue)
            .then(() => {
                // window.location.href = "/subvirtues";
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <Box sx={{ padding: 2 }}>
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Name (English)"
                    value={nameEn}
                    onChange={(e) => setNameEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <TextField
                    label="Name (Marathi)"
                    value={nameMr}
                    onChange={(e) => setNameMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <TextField
                    label="Description (English)"
                    value={descriptionEn}
                    onChange={(e) => setDescriptionEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <TextField
                    label="Description (Marathi)"
                    value={descriptionMr}
                    onChange={(e) => setDescriptionMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <TextField
                    label="Main Virtue ID"
                    value={mainVirtueId}
                    onChange={(e) => setMainVirtueId(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <Button type="submit">Create</Button>
            </form>
        </Box>
    );
}

export default CreateSubVirtue;
