import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Box,
  TextField,
  Button,
  Typography,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  CircularProgress,
} from "@mui/material";
import { useParams, useNavigate } from "react-router-dom";

function UpdateSubVirtue() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [nameEn, setNameEn] = useState("");
  const [nameMr, setNameMr] = useState("");
  const [descriptionEn, setDescriptionEn] = useState("");
  const [descriptionMr, setDescriptionMr] = useState("");
  const [mainVirtueId, setMainVirtueId] = useState("");
  const [mainVirtues, setMainVirtues] = useState([]);
  const [loading, setLoading] = useState(true);
  const [updating, setUpdating] = useState(false);
  const [confirmDialogOpen, setConfirmDialogOpen] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [subVirtueResponse, mainVirtuesResponse] = await Promise.all([
          axios.get(`${import.meta.env.VITE_API_URL}/subvirtues/${id}`),
          axios.get(`${import.meta.env.VITE_API_URL}/main-virtues`),
        ]);

        const subVirtue = subVirtueResponse.data;
        setNameEn(subVirtue.name.en);
        setNameMr(subVirtue.name.mr);
        setDescriptionEn(subVirtue.description?.en || "");
        setDescriptionMr(subVirtue.description?.mr || "");
        setMainVirtueId(subVirtue.main_virtue_id);
        setMainVirtues(mainVirtuesResponse.data);
        setLoading(false);
      } catch (error) {
        console.error(error);
        setError("Failed to fetch data. Please try again.");
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  const openConfirmDialog = (e) => {
    e.preventDefault();
    setConfirmDialogOpen(true);
  };

  const closeConfirmDialog = () => {
    setConfirmDialogOpen(false);
  };

  const handleSubmit = async () => {
    setUpdating(true);
    const subVirtue = {
      name: { en: nameEn, mr: nameMr },
      description: { en: descriptionEn, mr: descriptionMr },
      main_virtue_id: mainVirtueId,
    };

    try {
      await axios.put(
        `${import.meta.env.VITE_API_URL}/subvirtues/${id}`,
        subVirtue
      );
      setUpdating(false);
      navigate("/subvirtues");
    } catch (error) {
      console.error(error);
      setError("Failed to update sub virtue. Please try again.");
      setUpdating(false);
      closeConfirmDialog();
    }
  };

  if (loading) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "80vh",
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" sx={{ marginBottom: 3 }}>
        Update Sub Virtue
      </Typography>
      {error && (
        <Typography color="error" sx={{ marginBottom: 2 }}>
          {error}
        </Typography>
      )}
      <form onSubmit={openConfirmDialog}>
        <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <TextField
            fullWidth
            required
            label="Name (English)"
            value={nameEn}
            onChange={(e) => setNameEn(e.target.value)}
          />
          <TextField
            fullWidth
            required
            label="Name (Marathi)"
            value={nameMr}
            onChange={(e) => setNameMr(e.target.value)}
          />
          <TextField
            fullWidth
            label="Description (English)"
            multiline
            rows={4}
            value={descriptionEn}
            onChange={(e) => setDescriptionEn(e.target.value)}
          />
          <TextField
            fullWidth
            label="Description (Marathi)"
            multiline
            rows={4}
            value={descriptionMr}
            onChange={(e) => setDescriptionMr(e.target.value)}
          />
          <FormControl fullWidth required>
            <InputLabel>Main Virtue</InputLabel>
            <Select
              value={mainVirtueId}
              label="Main Virtue"
              onChange={(e) => setMainVirtueId(e.target.value)}
            >
              {mainVirtues.map((virtue) => (
                <MenuItem key={virtue._id} value={virtue._id}>
                  {virtue.name.en} - {virtue.name.mr}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <Box sx={{ display: "flex", gap: 2, marginTop: 2 }}>
            <Button variant="contained" type="submit">
              Update Sub Virtue
            </Button>
            <Button variant="outlined" onClick={() => navigate("/subvirtues")}>
              Cancel
            </Button>
          </Box>
        </Box>
      </form>

      <Dialog
        open={confirmDialogOpen}
        onClose={closeConfirmDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Confirm Update"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to update this sub virtue?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeConfirmDialog}>Cancel</Button>
          <Button onClick={handleSubmit} disabled={updating} autoFocus>
            {updating ? <CircularProgress size={24} /> : "Update"}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default UpdateSubVirtue;
