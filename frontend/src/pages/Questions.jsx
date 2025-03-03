import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";

function Questions() {
    const [questions, setQuestions] = useState([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_API_URL}/questions/`)
            .then((response) => {
                setQuestions(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4">Questions</Typography>
            <ul>
                {questions.map((question) => (
                    <li key={question._id}>
                        <Link to={`/questions/${question._id}`}>
                            {question.content.en}
                        </Link>
                    </li>
                ))}
            </ul>
            <Button component={Link} to="/create-question">
                Create New Question
            </Button>
        </Box>
    );
}

export default Questions;
