import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, TextField, Button, Autocomplete } from "@mui/material";

function CreateQuestion() {
    const [contentEn, setContentEn] = useState("");
    const [contentMr, setContentMr] = useState("");
    const [subvirtues, setSubvirtues] = useState([]);
    const [selectedSubvirtue, setSelectedSubvirtue] = useState(null);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/subvirtues/`)
            .then((response) => {
                setSubvirtues(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!selectedSubvirtue) {
            console.error("Please select a subvirtue.");
            return;
        }

        const question = {
            content: { en: contentEn, mr: contentMr },
            subvirtueId: selectedSubvirtue._id,
        };

        axios
            .post(`${import.meta.env.VITE_API_URL}/questions/`, question)
            .then(() => {
                window.location.href = "/questions";
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <Box sx={{ padding: 2 }}>
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Content (English)"
                    value={contentEn}
                    onChange={(e) => setContentEn(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <TextField
                    label="Content (Marathi)"
                    value={contentMr}
                    onChange={(e) => setContentMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <Autocomplete
                    options={subvirtues}
                    getOptionLabel={(option) => option.name.en}
                    value={selectedSubvirtue}
                    onChange={(event, value) => setSelectedSubvirtue(value)}
                    renderInput={(params) => (
                        <TextField
                            {...params}
                            label="Select Subvirtue"
                            sx={{ marginBottom: 2 }}
                        />
                    )}
                />
                <Button type="submit">Create</Button>
            </form>
        </Box>
    );
}

export default CreateQuestion;
