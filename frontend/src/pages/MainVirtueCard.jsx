import React, { useState } from "react";
import {
  Card,
  CardContent,
  Typography,
  IconButton,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Button,
} from "@mui/material";
import { Link } from "react-router-dom";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import axios from "axios";

const VirtueCard = ({ virtue, handleDelete }) => {
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);

  const openDeleteDialog = () => {
    setDeleteDialogOpen(true);
  };

  const closeDeleteDialog = () => {
    setDeleteDialogOpen(false);
  };

  const handleDeleteVirtue = async () => {
    try {
      await axios.delete(
        `${import.meta.env.VITE_API_URL}/main-virtues/${virtue._id}`
      );
      handleDelete(virtue._id);
      closeDeleteDialog();
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
          <IconButton component={Link} to={`/update-main-virtue/${virtue._id}`}>
            <EditIcon />
          </IconButton>
          <IconButton onClick={openDeleteDialog}>
            <DeleteIcon />
          </IconButton>
        </div>
      </CardContent>

      {/* Delete Confirmation Dialog */}
      <Dialog
        open={deleteDialogOpen}
        onClose={closeDeleteDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Confirm Deletion"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to delete "{virtue.name.en}"? This action
            cannot be undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeDeleteDialog}>Cancel</Button>
          <Button onClick={handleDeleteVirtue} color="error" autoFocus>
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </Card>
  );
};

export default VirtueCard;
