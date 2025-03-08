import React, { useState, useEffect } from "react";
import axios from "axios";
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

const SubVirtueCard = ({ subVirtue, handleDelete }) => {
  const [mainVirtue, setMainVirtue] = useState({});
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);

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

  const openDeleteDialog = () => {
    setDeleteDialogOpen(true);
  };

  const closeDeleteDialog = () => {
    setDeleteDialogOpen(false);
  };

  const handleDeleteSubVirtue = async () => {
    try {
      await axios.delete(
        `${import.meta.env.VITE_API_URL}/subvirtues/${subVirtue._id}`
      );
      handleDelete(subVirtue._id);
      closeDeleteDialog();
    } catch (error) {
      console.error(error);
      closeDeleteDialog();
    }
  };

  return (
    <>
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
            <IconButton onClick={openDeleteDialog}>
              <DeleteIcon />
            </IconButton>
          </div>
        </CardContent>
      </Card>

      <Dialog
        open={deleteDialogOpen}
        onClose={closeDeleteDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Confirm Deletion"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to delete this sub virtue ({subVirtue.name.en}
            )? This action cannot be undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeDeleteDialog}>Cancel</Button>
          <Button onClick={handleDeleteSubVirtue} autoFocus color="error">
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
};

export default SubVirtueCard;
