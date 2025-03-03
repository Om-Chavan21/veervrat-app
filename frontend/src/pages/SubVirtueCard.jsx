import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card, CardContent, Typography, Link, IconButton } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

const SubVirtueCard = ({ subVirtue, handleDelete }) => {
    const [mainVirtue, setMainVirtue] = useState({});

    useEffect(() => {
        axios
            .get(
                `${import.meta.env.VITE_API_URL}/main-virtues/${
                    subVirtue.main_virtue_id
                }`
            )
            .then((response) => {
                setMainVirtue(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, [subVirtue.main_virtue_id]);

    const handleDeleteSubVirtue = async () => {
        try {
            await axios.delete(
                `${import.meta.env.VITE_API_URL}/subvirtues/${subVirtue._id}`
            );
            handleDelete(subVirtue._id);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <Card
            sx={{
                margin: 2,
                width: { xs: "100%", sm: "45%", md: "30%" },
                display: "inline-block",
            }}
        >
            <CardContent>
                <Typography variant="h6">
                    <Link to={`/subvirtues/${subVirtue._id}`}>
                        {subVirtue.name.en} - {subVirtue.name.mr}
                    </Link>
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Main Virtue: {mainVirtue.name?.en} - {mainVirtue.name?.mr}
                </Typography>
                <div style={{ float: "right" }}>
                    <IconButton
                        component={Link}
                        to={`/update-subvirtue/${subVirtue._id}`}
                    >
                        <EditIcon />
                    </IconButton>
                    <IconButton onClick={handleDeleteSubVirtue}>
                        <DeleteIcon />
                    </IconButton>
                </div>
            </CardContent>
        </Card>
    );
};

export default SubVirtueCard;
