import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import VirtueCard from "./MainVirtueCard";

function MainVirtues() {
    const [virtues, setVirtues] = useState([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/main-virtues/`)
            .then((response) => {
                setVirtues(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const handleDelete = (id) => {
        setVirtues(virtues.filter((virtue) => virtue._id !== id));
    };

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4">Main Virtues</Typography>
            {virtues.map((virtue) => (
                <VirtueCard
                    key={virtue._id}
                    virtue={virtue}
                    handleDelete={handleDelete}
                />
            ))}
            <Button
                component={Link}
                to="/create-main-virtue"
                sx={{ marginTop: 2 }}
            >
                Create New Main Virtue
            </Button>
        </Box>
    );
}

export default MainVirtues;
