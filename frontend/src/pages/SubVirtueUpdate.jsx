import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, TextField, Button } from "@mui/material";
import { useParams } from "react-router-dom";

function UpdateSubVirtue() {
    const { id } = useParams();
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");
    const [mainVirtueId, setMainVirtueId] = useState("");

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/subvirtues/${id}`)
            .then((response) => {
                const subVirtue = response.data;
                setNameEn(subVirtue.name.en);
                setNameMr(subVirtue.name.mr);
                setDescriptionEn(subVirtue.description?.en || "");
                setDescriptionMr(subVirtue.description?.mr || "");
                setMainVirtueId(subVirtue.main_virtue_id);
            })
            .catch((error) => {
                console.error(error);
            });
    }, [id]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const subVirtue = {
            name: { en: nameEn, mr: nameMr },
            description: { en: descriptionEn, mr: descriptionMr },
            main_virtue_id: mainVirtueId,
        };

        axios
            .put(`${import.meta.env.VITE_API_URL}/subvirtues/${id}`, subVirtue)
            .then(() => {
                window.location.href = "/subvirtues";
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
                <Button type="submit">Update</Button>
            </form>
        </Box>
    );
}

export default UpdateSubVirtue;
