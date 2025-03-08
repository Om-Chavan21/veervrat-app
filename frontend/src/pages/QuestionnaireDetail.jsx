// src/pages/QuestionnaireDetail.jsx
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Container,
  Typography,
  Card,
  CardContent,
  Button,
  Divider,
  CircularProgress,
  Alert,
  Grid,
  Chip
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { format } from 'date-fns';
import { getQuestionnaireById } from '../apiClient';
import { useAuth } from '../context/AuthContext';

const QuestionnaireDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [questionnaire, setQuestionnaire] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login', { state: { from: `/questionnaire/${id}` } });
      return;
    }
    
    const fetchQuestionnaire = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await getQuestionnaireById(id);
        setQuestionnaire(data);
      } catch (error) {
        console.error('Error fetching questionnaire:', error);
        setError('Failed to load questionnaire details. Please try again.');
      } finally {
        setLoading(false);
      }
    };
    
    if (id) {
      fetchQuestionnaire();
    }
  }, [id, isAuthenticated, navigate]);

  const formatDate = (dateString) => {
    try {
      return format(new Date(dateString), 'PPP');
    } catch (error) {
      return 'Unknown date';
    }
  };

  const getAnswerColor = (answer) => {
    switch (answer) {
      case 'Always':
        return 'success';
      case 'Sometimes':
        return 'primary';
      case 'Rarely':
        return 'warning';
      case 'Never':
        return 'error';
      default:
        return 'default';
    }
  };

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <CircularProgress />
          <Typography variant="h6" sx={{ mt: 2 }}>Loading questionnaire details...</Typography>
        </Box>
      </Container>
    );
  }

  if (error) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Alert severity="error">{error}</Alert>
        <Box sx={{ mt: 3 }}>
          <Button
            variant="contained"
            startIcon={<ArrowBackIcon />}
            component={RouterLink}
            to="/profile"
          >
            Back to Profile
          </Button>
        </Box>
      </Container>
    );
  }

  if (!questionnaire) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Alert severity="info">No questionnaire found with this ID.</Alert>
        <Box sx={{ mt: 3 }}>
          <Button
            variant="contained"
            startIcon={<ArrowBackIcon />}
            component={RouterLink}
            to="/profile"
          >
            Back to Profile
          </Button>
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Button
          variant="outlined"
          startIcon={<ArrowBackIcon />}
          component={RouterLink}
          to="/profile"
          sx={{ mb: 2 }}
        >
          Back to Profile
        </Button>
        
        <Typography variant="h4" component="h1" gutterBottom>
          Assessment Details
        </Typography>
        
        <Typography variant="subtitle1" color="textSecondary">
          Completed on {formatDate(questionnaire.created_at)}
        </Typography>
      </Box>

      <Card sx={{ mb: 4 }}>
        <CardContent>
          <Typography variant="h5" component="h2" gutterBottom>
            Selected Weaknesses
          </Typography>
          
          <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
            Group A
          </Typography>
          <Grid container spacing={2}>
            {questionnaire.group_a_weaknesses.map((weakness) => (
              <Grid item xs={12} sm={6} key={weakness._id}>
                <Card variant="outlined">
                  <CardContent>
                    <Typography variant="subtitle1">{weakness.name?.en || 'Unknown'}</Typography>
                    {weakness.name?.mr && (
                      <Typography variant="body2" color="textSecondary">
                        {weakness.name.mr}
                      </Typography>
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
          
          <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
            Group B
          </Typography>
          <Grid container spacing={2}>
            {questionnaire.group_b_weaknesses.map((weakness) => (
              <Grid item xs={12} sm={6} key={weakness._id}>
                <Card variant="outlined">
                  <CardContent>
                    <Typography variant="subtitle1">{weakness.name?.en || 'Unknown'}</Typography>
                    {weakness.name?.mr && (
                      <Typography variant="body2" color="textSecondary">
                        {weakness.name.mr}
                      </Typography>
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
          
          <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
            Group C
          </Typography>
          <Grid container spacing={2}>
            {questionnaire.group_c_weaknesses.map((weakness) => (
              <Grid item xs={12} sm={6} key={weakness._id}>
                <Card variant="outlined">
                  <CardContent>
                    <Typography variant="subtitle1">{weakness.name?.en || 'Unknown'}</Typography>
                    {weakness.name?.mr && (
                      <Typography variant="body2" color="textSecondary">
                        {weakness.name.mr}
                      </Typography>
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <Typography variant="h5" component="h2" gutterBottom>
            Responses
          </Typography>
          
          <Box sx={{ mt: 2 }}>
            {questionnaire.responses.map((response, index) => (
              <Card variant="outlined" key={response.question_id} sx={{ mb: 2, p: 2 }}>
                <CardContent>
                  <Typography variant="subtitle1" gutterBottom>
                    Question {index + 1}: {response.question?.content?.en || 'Unknown question'}
                  </Typography>
                  {response.question?.content?.mr && (
                    <Typography variant="body2" color="textSecondary" gutterBottom>
                      {response.question.content.mr}
                    </Typography>
                  )}
                  <Box sx={{ mt: 2 }}>
                    <Chip 
                      label={response.answer} 
                      color={getAnswerColor(response.answer)}
                      variant="filled"
                    />
                  </Box>
                </CardContent>
              </Card>
            ))}
          </Box>
        </CardContent>
      </Card>
    </Container>
  );
};

export default QuestionnaireDetail;