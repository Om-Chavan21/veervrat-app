// UpdateMainVirtue.js
import React, { useState, useEffect } from "react";
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
import { useParams, useNavigate } from "react-router-dom";

function UpdateMainVirtue() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [nameEn, setNameEn] = useState("");
  const [nameMr, setNameMr] = useState("");
  const [descriptionEn, setDescriptionEn] = useState("");
  const [descriptionMr, setDescriptionMr] = useState("");
  const [itemCode, setItemCode] = useState("");
  const [confirmDialogOpen, setConfirmDialogOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    axios
      .get(`${import.meta.env.VITE_API_URL}/main-virtues/${id}`)
      .then((response) => {
        const virtue = response.data;
        setNameEn(virtue.name.en);
        setNameMr(virtue.name.mr);
        setDescriptionEn(virtue.description?.en || "");
        setDescriptionMr(virtue.description?.mr || "");
        setItemCode(virtue.item_code || "");
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setError("Failed to load virtue data");
        setIsLoading(false);
      });
  }, [id]);

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
      await axios.put(
        `${import.meta.env.VITE_API_URL}/main-virtues/${id}`,
        virtue
      );
      navigate("/main-virtues");
    } catch (error) {
      console.error(error);
      setError(error.response?.data?.detail || "Failed to update");
    }
    closeConfirmDialog();
  };

  if (isLoading) return <Box>Loading...</Box>;
  if (error) return <Box color="error">{error}</Box>;

  return (
    <Box sx={{ padding: 2 }}>
      <form onSubmit={openConfirmDialog}>
        <TextField
          label="Name (English)"
          value={nameEn}
          onChange={(e) => setNameEn(e.target.value)}
          sx={{ marginBottom: 2, width: "100%" }}
          required
        />
        <TextField
          label="Name (Marathi)"
          value={nameMr}
          onChange={(e) => setNameMr(e.target.value)}
          sx={{ marginBottom: 2, width: "100%" }}
          required
        />
        <TextField
          label="Item Code"
          value={itemCode}
          onChange={(e) => setItemCode(e.target.value)}
          sx={{ marginBottom: 2, width: "100%" }}
          helperText="Format: x.0.0 (e.g., 1.0.0)"
          required
        />
        <TextField
          label="Description (English)"
          value={descriptionEn}
          onChange={(e) => setDescriptionEn(e.target.value)}
          sx={{ marginBottom: 2, width: "100%" }}
          multiline
          rows={2}
        />
        <TextField
          label="Description (Marathi)"
          value={descriptionMr}
          onChange={(e) => setDescriptionMr(e.target.value)}
          sx={{ marginBottom: 2, width: "100%" }}
          multiline
          rows={2}
        />
        <Button type="submit" variant="contained">
          Update
        </Button>
        <Button
          variant="outlined"
          onClick={() => navigate("/main-virtues")}
          sx={{ marginLeft: 2 }}
        >
          Cancel
        </Button>
      </form>

      {/* Confirmation Dialog */}
      <Dialog
        open={confirmDialogOpen}
        onClose={closeConfirmDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Confirm Update"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to update this main virtue?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeConfirmDialog}>Cancel</Button>
          <Button onClick={handleSubmit} color="primary" autoFocus>
            Update
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default UpdateMainVirtue;
