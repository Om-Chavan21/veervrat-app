import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import SubVirtueCard from "./SubVirtueCard";

function SubVirtues() {
    const [subVirtues, setSubVirtues] = useState([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/subvirtues`)
            .then((response) => {
                setSubVirtues(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const handleDelete = (id) => {
        setSubVirtues(subVirtues.filter((subVirtue) => subVirtue._id !== id));
    };

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4">Sub Virtues</Typography>
            {subVirtues.map((subVirtue) => (
                <SubVirtueCard
                    key={subVirtue._id}
                    subVirtue={subVirtue}
                    handleDelete={handleDelete}
                />
            ))}
            <Button
                component={Link}
                to="/create-subvirtue"
                sx={{ marginTop: 2 }}
            >
                Create New Sub Virtue
            </Button>
        </Box>
    );
}

export default SubVirtues;
