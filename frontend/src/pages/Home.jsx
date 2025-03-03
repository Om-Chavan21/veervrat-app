import React from "react";
import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";

function Home() {
    return (
        <Box sx={{ padding: 2, textAlign: "center" }}>
            <Typography variant="h4">
                Welcome to Virtues and Weaknesses App
            </Typography>
            <Box sx={{ margin: "20px 0" }}>
                <Button
                    component={Link}
                    to="/main-virtues"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    View Main Virtues
                </Button>
                <Button
                    component={Link}
                    to="/create-main-virtue"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    Create Main Virtue
                </Button>
            </Box>
            <Box sx={{ margin: "20px 0" }}>
                <Button
                    component={Link}
                    to="/subvirtues"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    View Sub Virtues
                </Button>
                <Button
                    component={Link}
                    to="/create-subvirtue"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    Create Sub Virtue
                </Button>
            </Box>
            <Box sx={{ margin: "20px 0" }}>
                <Button
                    component={Link}
                    to="/weaknesses"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    View Weaknesses
                </Button>
                <Button
                    component={Link}
                    to="/create-weakness"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    Create Weakness
                </Button>
            </Box>
            <Box sx={{ margin: "20px 0" }}>
                <Button
                    component={Link}
                    to="/questions"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    View Questions
                </Button>
                <Button
                    component={Link}
                    to="/create-question"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    Create Question
                </Button>
                <Button
                    component={Link}
                    to="/form-testing"
                    variant="contained"
                    sx={{ margin: 1 }}
                >
                    Form Testing
                </Button>
            </Box>
        </Box>
    );
}

export default Home;
