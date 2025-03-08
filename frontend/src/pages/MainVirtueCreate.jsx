import React, { useState } from "react";
import axios from "axios";
import {
  Box,
  TextField,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from "@mui/material";
import { useNavigate } from "react-router-dom";

function CreateMainVirtue() {
  const navigate = useNavigate();
  const [nameEn, setNameEn] = useState("");
  const [nameMr, setNameMr] = useState("");
  const [descriptionEn, setDescriptionEn] = useState("");
  const [descriptionMr, setDescriptionMr] = useState("");
  const [itemCode, setItemCode] = useState("");
  const [confirmDialogOpen, setConfirmDialogOpen] = useState(false);
  const [error, setError] = useState(null);

  const openConfirmDialog = (e) => {
    e.preventDefault();
    setConfirmDialogOpen(true);
  };

  const closeConfirmDialog = () => {
    setConfirmDialogOpen(false);
  };

  const handleSubmit = async () => {
    const virtue = {
      name: { en: nameEn, mr: nameMr },
      description: { en: descriptionEn, mr: descriptionMr },
      item_code: itemCode,
    };

    try {
      await axios.post(`${import.meta.env.VITE_API_URL}/main-virtues/`, virtue);
      navigate("/main-virtues");
    } catch (error) {
      console.error(error);
      setError(error.response?.data?.detail || "Failed to create");
    }
    closeConfirmDialog();
  };

  return (
    <Box
      className="flex justify-center items-center h-screen"
      sx={{ padding: 0 }}
    >
      <form
        onSubmit={openConfirmDialog}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-md"
      >
        <h2 className="text-lg font-bold mb-4">Create Main Virtue</h2>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        <TextField
          label="Name (English)"
          value={nameEn}
          onChange={(e) => setNameEn(e.target.value)}
          sx={{ marginBottom: 2 }}
          className="w-full"
          required
        />
        <TextField
          label="Name (Marathi)"
          value={nameMr}
          onChange={(e) => setNameMr(e.target.value)}
          sx={{ marginBottom: 2 }}
          className="w-full"
          required
        />
        <TextField
          label="Item Code"
          value={itemCode}
          onChange={(e) => setItemCode(e.target.value)}
          sx={{ marginBottom: 2 }}
          className="w-full"
          helperText="Format: x.0.0 (e.g., 1.0.0)"
          required
        />
        <TextField
          label="Description (English)"
          value={descriptionEn}
          onChange={(e) => setDescriptionEn(e.target.value)}
          sx={{ marginBottom: 2 }}
          className="w-full"
          multiline
          rows={2}
        />
        <TextField
          label="Description (Marathi)"
          value={descriptionMr}
          onChange={(e) => setDescriptionMr(e.target.value)}
          sx={{ marginBottom: 2 }}
          className="w-full"
          multiline
          rows={2}
        />
        <div className="flex justify-between">
          <Button type="submit" variant="contained" className="w-full">
            Create
          </Button>
          <Button
            variant="outlined"
            onClick={() => navigate("/main-virtues")}
            sx={{ marginLeft: 2 }}
          >
            Cancel
          </Button>
        </div>
      </form>

      {/* Confirmation Dialog */}
      <Dialog
        open={confirmDialogOpen}
        onClose={closeConfirmDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Confirm Creation"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to create this main virtue?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeConfirmDialog}>Cancel</Button>
          <Button onClick={handleSubmit} color="primary" autoFocus>
            Create
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default CreateMainVirtue;
