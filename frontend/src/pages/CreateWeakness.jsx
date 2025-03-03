import React, { useState, useEffect } from "react";
import axios from "axios";
import {
    Box,
    TextField,
    Button,
    Checkbox,
    FormControlLabel,
} from "@mui/material";

function CreateWeakness() {
    const [nameEn, setNameEn] = useState("");
    const [nameMr, setNameMr] = useState("");
    const [descriptionEn, setDescriptionEn] = useState("");
    const [descriptionMr, setDescriptionMr] = useState("");
    const [group, setGroup] = useState("");
    const [suggestedSubvirtueIds, setSuggestedSubvirtueIds] = useState([]);
    const [subvirtues, setSubvirtues] = useState([]); // State for subvirtues

    // Fetch subvirtues from the API
    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/subvirtues/`)
            .then((response) => {
                const sortedSubvirtues = response.data.sort((a, b) =>
                    a.name.en.localeCompare(b.name.en)
                );
                setSubvirtues(sortedSubvirtues); // Store fetched and sorted subvirtues
            })
            .catch((error) => {
                console.error("Error fetching subvirtues:", error);
            });
    }, []);

    const handleSubvirtueChange = (id) => {
        if (suggestedSubvirtueIds.includes(id)) {
            setSuggestedSubvirtueIds(
                suggestedSubvirtueIds.filter(
                    (subvirtueId) => subvirtueId !== id
                )
            );
        } else {
            setSuggestedSubvirtueIds([...suggestedSubvirtueIds, id]);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const weakness = {
            name: { en: nameEn, mr: nameMr },
            description: { en: descriptionEn, mr: descriptionMr },
            group: group,
            suggested_subvirtue_ids: suggestedSubvirtueIds,
        };

        axios
            .post(`${import.meta.env.VITE_API_URL}/weaknesses/`, weakness)
            .then(() => {
                window.location.href = "/weaknesses";
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
                <p></p>
                <TextField
                    label="Name (Marathi)"
                    value={nameMr}
                    onChange={(e) => setNameMr(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />
                <p></p>
                {/* <TextField
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
                /> */}
                <TextField
                    label="Group"
                    value={group}
                    onChange={(e) => setGroup(e.target.value)}
                    sx={{ marginBottom: 2 }}
                />

                <p></p>
                {/* List of checkboxes for subvirtues */}
                {subvirtues.map((subvirtue) => (
                    <FormControlLabel
                        key={subvirtue._id}
                        control={
                            <Checkbox
                                checked={suggestedSubvirtueIds.includes(
                                    subvirtue._id
                                )}
                                onChange={() =>
                                    handleSubvirtueChange(subvirtue._id)
                                }
                            />
                        }
                        label={`${subvirtue.name.en} / ${subvirtue.name.mr}`}
                        sx={{ display: "block", marginBottom: 1 }}
                    />
                ))}

                <Button type="submit">Create</Button>
            </form>
        </Box>
    );
}

export default CreateWeakness;
