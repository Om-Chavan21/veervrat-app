// src/pages/Profile.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate, Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Container,
  Typography,
  Card,
  CardContent,
  Button,
  Divider,
  Grid,
  CircularProgress,
  Alert,
  Chip,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle
} from '@mui/material';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import DeleteIcon from '@mui/icons-material/Delete';
import VisibilityIcon from '@mui/icons-material/Visibility';
import { format } from 'date-fns';
import { toast } from 'react-toastify';
import { getUserQuestionnaires, deleteQuestionnaire } from '../apiClient';
import { useAuth } from '../context/AuthContext';

const Profile = () => {
  const navigate = useNavigate();
  const { user, isAuthenticated } = useAuth();
  const [questionnaires, setQuestionnaires] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [questionnaireToDelete, setQuestionnaireToDelete] = useState(null);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login', { state: { from: '/profile' } });
      return;
    }
    
    const fetchQuestionnaires = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await getUserQuestionnaires();
        setQuestionnaires(data);
      } catch (error) {
        console.error('Error fetching questionnaires:', error);
        setError('Failed to load your questionnaires. Please try again.');
      } finally {
        setLoading(false);
      }
    };
    
    fetchQuestionnaires();
  }, [isAuthenticated, navigate]);

  const handleOpenDeleteDialog = (questionnaire) => {
    setQuestionnaireToDelete(questionnaire);
    setDeleteDialogOpen(true);
  };

  const handleCloseDeleteDialog = () => {
    setDeleteDialogOpen(false);
    setQuestionnaireToDelete(null);
  };

  const handleDeleteQuestionnaire = async () => {
    if (!questionnaireToDelete) return;
    
    try {
      await deleteQuestionnaire(questionnaireToDelete._id);
      setQuestionnaires(questionnaires.filter(q => q._id !== questionnaireToDelete._id));
      toast.success('Questionnaire deleted successfully');
    } catch (error) {
      console.error('Error deleting questionnaire:', error);
      toast.error('Failed to delete questionnaire');
    } finally {
      handleCloseDeleteDialog();
    }
  };

  const formatDate = (dateString) => {
    try {
      return format(new Date(dateString), 'PPP');
    } catch (error) {
      return 'Unknown date';
    }
  };

  const getWeaknessesNames = (weaknesses) => {
    return weaknesses.map(weakness => weakness.name?.en || 'Unknown').join(', ');
  };

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <CircularProgress />
          <Typography variant="h6" sx={{ mt: 2 }}>Loading your profile...</Typography>
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography variant="h4" component="h1">
          My Profile
        </Typography>
        <Button
          variant="contained"
          color="primary"
          startIcon={<AddCircleOutlineIcon />}
          component={RouterLink}
          to="/questionnaire"
        >
          New Assessment
        </Button>
      </Box>

      {user && (
        <Card sx={{ mb: 4 }}>
          <CardContent>
            <Typography variant="h5" component="h2" gutterBottom>
              {user.name?.en || 'User'}
            </Typography>
            <Typography color="textSecondary">
              {user.email}
            </Typography>
            {user.whatsappNumber && (
              <Typography color="textSecondary">
                WhatsApp: {user.whatsappNumber}
              </Typography>
            )}
          </CardContent>
        </Card>
      )}

      <Typography variant="h5" component="h2" gutterBottom>
        My Assessments
      </Typography>

      {error && <Alert severity="error" sx={{ mb: 3 }}>{error}</Alert>}

      {questionnaires.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 4 }}>
          <Typography variant="body1" color="textSecondary" gutterBottom>
            You haven't completed any assessments yet.
          </Typography>
          <Button
            variant="contained"
            component={RouterLink}
            to="/questionnaire"
            sx={{ mt: 2 }}
          >
            Start an Assessment
          </Button>
        </Box>
      ) : (
        <Grid container spacing={3}>
          {questionnaires.map((questionnaire) => (
            <Grid item xs={12} key={questionnaire._id}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <Box>
                      <Typography variant="h6" component="h3" gutterBottom>
                        Assessment from {formatDate(questionnaire.created_at)}
                      </Typography>
                      
                      <Box sx={{ mt: 1 }}>
                        <Typography variant="subtitle2" color="textSecondary">
                          Group A Weaknesses:
                        </Typography>
                        <Typography gutterBottom>
                          {getWeaknessesNames(questionnaire.group_a_weaknesses)}
                        </Typography>
                        
                        <Typography variant="subtitle2" color="textSecondary">
                          Group B Weaknesses:
                        </Typography>
                        <Typography gutterBottom>
                          {getWeaknessesNames(questionnaire.group_b_weaknesses)}
                        </Typography>
                        
                        <Typography variant="subtitle2" color="textSecondary">
                          Group C Weaknesses:
                        </Typography>
                        <Typography gutterBottom>
                          {getWeaknessesNames(questionnaire.group_c_weaknesses)}
                        </Typography>
                      </Box>
                      
                      <Box sx={{ mt: 2 }}>
                        <Chip 
                          label={`${questionnaire.responses.length} Questions`} 
                          size="small" 
                          color="primary" 
                          variant="outlined"
                        />
                      </Box>
                    </Box>
                    
                    <Box>
                      <Button
                        variant="outlined"
                        startIcon={<VisibilityIcon />}
                        sx={{ mr: 1 }}
                        component={RouterLink}
                        to={`/questionnaire/${questionnaire._id}`}
                      >
                        View
                      </Button>
                      <Button
                        variant="outlined"
                        color="error"
                        startIcon={<DeleteIcon />}
                        onClick={() => handleOpenDeleteDialog(questionnaire)}
                      >
                        Delete
                      </Button>
                    </Box>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}

      <Dialog
        open={deleteDialogOpen}
        onClose={handleCloseDeleteDialog}
      >
        <DialogTitle>Delete Assessment</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Are you sure you want to delete this assessment? This action cannot be undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDeleteDialog}>Cancel</Button>
          <Button onClick={handleDeleteQuestionnaire} color="error">
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default Profile;