import React from "react";
import { Card, CardContent, Typography, Link, IconButton } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import axios from "axios";

const VirtueCard = ({ virtue, handleDelete }) => {
    const handleDeleteVirtue = async () => {
        try {
            await axios.delete(
                `${import.meta.env.VITE_API_URL}/main-virtues/${virtue._id}`
            );
            handleDelete(virtue._id);
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
                    <Link to={`/main-virtues/${virtue._id}`}>
                        {virtue.name.en} - {virtue.name.mr}
                    </Link>
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    ID: {virtue.item_code}
                </Typography>
                <div style={{ float: "right" }}>
                    <IconButton
                        component={Link}
                        to={`/update-main-virtue/${virtue._id}`}
                    >
                        <EditIcon />
                    </IconButton>
                    <IconButton onClick={handleDeleteVirtue}>
                        <DeleteIcon />
                    </IconButton>
                </div>
            </CardContent>
        </Card>
    );
};

export default VirtueCard;
