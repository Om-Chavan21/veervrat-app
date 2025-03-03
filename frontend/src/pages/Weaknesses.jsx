import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";

function Weaknesses() {
    const [weaknesses, setWeaknesses] = useState([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/weaknesses/`)
            .then((response) => {
                setWeaknesses(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4">Weaknesses</Typography>
            <ul>
                {weaknesses.map((weakness) => (
                    <li key={weakness._id}>
                        <Link to={`/weaknesses/${weakness._id}`}>
                            {weakness.name.en}
                        </Link>
                    </li>
                ))}
            </ul>
            <Button component={Link} to="/create-weakness">
                Create New Weakness
            </Button>
        </Box>
    );
}

export default Weaknesses;
