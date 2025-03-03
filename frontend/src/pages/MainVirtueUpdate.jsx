// UpdateMainVirtue.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, TextField, Button } from "@mui/material";
import { useParams } from "react-router-dom";

function UpdateMainVirtue() {
    const { id } = useParams();
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/main-virtues/${id}`)
            .then((response) => {
                const virtue = response.data;
                setNameEn(virtue.name.en);
                setNameMr(virtue.name.mr);
                setDescriptionEn(virtue.description?.en || "");
                setDescriptionMr(virtue.description?.mr || "");
            })
            .catch((error) => {
                console.error(error);
            });
    }, [id]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const virtue = {
            name: { en: nameEn, mr: nameMr },
            description: { en: descriptionEn, mr: descriptionMr },
        };

        axios
            .put(`${import.meta.env.VITE_API_URL}/main-virtues/${id}`, virtue)
            .then(() => {
                window.location.href = "/main-virtues";
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
                <Button type="submit">Update</Button>
            </form>
        </Box>
    );
}

export default UpdateMainVirtue;
