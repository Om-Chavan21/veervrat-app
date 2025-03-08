// src/pages/QuestionnaireForm.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Box, 
  Container, 
  Typography, 
  Button, 
  Stepper, 
  Step, 
  StepLabel,
  FormControl,
  FormControlLabel,
  Radio,
  RadioGroup,
  Card,
  CardContent,
  Grid,
  Chip,
  Alert,
  CircularProgress
} from '@mui/material';
import { toast } from 'react-toastify';
import { getWeaknessesByGroup, getRandomQuestions, submitQuestionnaire } from '../apiClient';
import { useAuth } from '../context/AuthContext';

const steps = ['Select Group A Weaknesses', 'Select Group B Weaknesses', 'Select Group C Weaknesses', 'Answer Questions'];

const QuestionnaireForm = () => {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [activeStep, setActiveStep] = useState(0);
  const [groupAWeaknesses, setGroupAWeaknesses] = useState([]);
  const [groupBWeaknesses, setGroupBWeaknesses] = useState([]);
  const [groupCWeaknesses, setGroupCWeaknesses] = useState([]);
  const [selectedGroupAWeaknesses, setSelectedGroupAWeaknesses] = useState([]);
  const [selectedGroupBWeaknesses, setSelectedGroupBWeaknesses] = useState([]);
  const [selectedGroupCWeaknesses, setSelectedGroupCWeaknesses] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login', { state: { from: '/questionnaire' } });
      return;
    }
    
    const fetchWeaknessesByGroup = async (group) => {
      try {
        return await getWeaknessesByGroup(group);
      } catch (error) {
        console.error(`Error fetching group ${group} weaknesses:`, error);
        setError(`Failed to load group ${group} weaknesses. Please try again.`);
        return [];
      }
    };

    const loadWeaknesses = async () => {
      setLoading(true);
      setError(null);
      
      const [groupA, groupB, groupC] = await Promise.all([
        fetchWeaknessesByGroup('A'),
        fetchWeaknessesByGroup('B'),
        fetchWeaknessesByGroup('C'),
      ]);
      
      setGroupAWeaknesses(groupA);
      setGroupBWeaknesses(groupB);
      setGroupCWeaknesses(groupC);
      setLoading(false);
    };

    loadWeaknesses();
  }, [isAuthenticated, navigate]);

  const handleWeaknessSelection = (weakness, group) => {
    switch(group) {
      case 'A':
        if (selectedGroupAWeaknesses.some(w => w._id === weakness._id)) {
          setSelectedGroupAWeaknesses(selectedGroupAWeaknesses.filter(w => w._id !== weakness._id));
        } else {
          if (selectedGroupAWeaknesses.length < 2) {
            setSelectedGroupAWeaknesses([...selectedGroupAWeaknesses, weakness]);
          } else {
            toast.warning('You can only select 2 weaknesses from Group A');
          }
        }
        break;
      case 'B':
        if (selectedGroupBWeaknesses.some(w => w._id === weakness._id)) {
          setSelectedGroupBWeaknesses(selectedGroupBWeaknesses.filter(w => w._id !== weakness._id));
        } else {
          if (selectedGroupBWeaknesses.length < 2) {
            setSelectedGroupBWeaknesses([...selectedGroupBWeaknesses, weakness]);
          } else {
            toast.warning('You can only select 2 weaknesses from Group B');
          }
        }
        break;
      case 'C':
        if (selectedGroupCWeaknesses.some(w => w._id === weakness._id)) {
          setSelectedGroupCWeaknesses(selectedGroupCWeaknesses.filter(w => w._id !== weakness._id));
        } else {
          if (selectedGroupCWeaknesses.length < 2) {
            setSelectedGroupCWeaknesses([...selectedGroupCWeaknesses, weakness]);
          } else {
            toast.warning('You can only select 2 weaknesses from Group C');
          }
        }
        break;
      default:
        break;
    }
  };

  const handleAnswerChange = (questionId, value) => {
    setAnswers({
      ...answers,
      [questionId]: value
    });
  };

  const handleNext = async () => {
    if (activeStep === 0 && selectedGroupAWeaknesses.length !== 2) {
      toast.error('Please select exactly 2 weaknesses from Group A');
      return;
    }

    if (activeStep === 1 && selectedGroupBWeaknesses.length !== 2) {
      toast.error('Please select exactly 2 weaknesses from Group B');
      return;
    }

    if (activeStep === 2 && selectedGroupCWeaknesses.length !== 2) {
      toast.error('Please select exactly 2 weaknesses from Group C');
      return;
    }

    if (activeStep === 2) {
      // Before moving to questions, fetch random questions
      try {
        setLoading(true);
        setError(null);
        
        const groupAWeaknessesParam = selectedGroupAWeaknesses.map(w => ({ weakness_id: w._id }));
        const groupBWeaknessesParam = selectedGroupBWeaknesses.map(w => ({ weakness_id: w._id }));
        const groupCWeaknessesParam = selectedGroupCWeaknesses.map(w => ({ weakness_id: w._id }));
        
        const response = await getRandomQuestions(
          groupAWeaknessesParam,
          groupBWeaknessesParam,
          groupCWeaknessesParam
        );
        
        setQuestions(response.questions);
        
        // Initialize answers object with empty values
        const initialAnswers = {};
        response.questions.forEach(q => {
          initialAnswers[q._id] = '';
        });
        setAnswers(initialAnswers);
        
      } catch (error) {
        console.error('Error fetching questions:', error);
        setError('Failed to load questions. Please try again.');
        setLoading(false);
        return;
      }
      setLoading(false);
    }

    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleSubmit = async () => {
    // Validate that all questions are answered
    const unansweredQuestions = Object.entries(answers).filter(([_, value]) => !value);
    if (unansweredQuestions.length > 0) {
      toast.error(`Please answer all questions (${unansweredQuestions.length} remaining)`);
      return;
    }

    try {
      setLoading(true);
      setError(null);
      
      // Format the responses
      const responses = Object.entries(answers).map(([questionId, answer]) => ({
        question_id: questionId,
        answer
      }));

      // Submit the questionnaire
      await submitQuestionnaire({
        group_a_weaknesses: selectedGroupAWeaknesses.map(w => ({ weakness_id: w._id })),
        group_b_weaknesses: selectedGroupBWeaknesses.map(w => ({ weakness_id: w._id })),
        group_c_weaknesses: selectedGroupCWeaknesses.map(w => ({ weakness_id: w._id })),
        responses
      });
      
      toast.success('Questionnaire submitted successfully');
      navigate('/profile');
      
    } catch (error) {
      console.error('Error submitting questionnaire:', error);
      setError('Failed to submit questionnaire. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const renderWeaknessList = (weaknesses, selectedWeaknesses, group) => (
    <Grid container spacing={2}>
      {weaknesses.map((weakness) => (
        <Grid item xs={12} sm={6} key={weakness._id}>
          <Card 
            sx={{ 
              cursor: 'pointer',
              bgcolor: selectedWeaknesses.some(w => w._id === weakness._id) ? 'primary.light' : 'white',
              '&:hover': {
                boxShadow: 3,
              }
            }}
            onClick={() => handleWeaknessSelection(weakness, group)}
          >
            <CardContent>
              <Typography variant="h6">{weakness.name.en}</Typography>
              {weakness.name.mr && (
                <Typography variant="subtitle2" color="text.secondary">
                  {weakness.name.mr}
                </Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );

  const renderQuestions = () => (
    <Box>
      {questions.map((question, index) => (
        <Card key={question._id} sx={{ mb: 3, p: 2 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Question {index + 1}: {question.content.en}
            </Typography>
            {question.content.mr && (
              <Typography variant="subtitle1" color="text.secondary" gutterBottom>
                {question.content.mr}
              </Typography>
            )}
            <FormControl component="fieldset" fullWidth margin="normal">
              <RadioGroup
                value={answers[question._id] || ''}
                onChange={(e) => handleAnswerChange(question._id, e.target.value)}
              >
                <FormControlLabel value="Always" control={<Radio />} label="Always" />
                <FormControlLabel value="Sometimes" control={<Radio />} label="Sometimes" />
                <FormControlLabel value="Rarely" control={<Radio />} label="Rarely" />
                <FormControlLabel value="Never" control={<Radio />} label="Never" />
              </RadioGroup>
            </FormControl>
          </CardContent>
        </Card>
      ))}
    </Box>
  );

  const getStepContent = (step) => {
    switch (step) {
      case 0:
        return (
          <Box>
            <Typography variant="h6" gutterBottom>
              Select 2 weaknesses from Group A
            </Typography>
            <Box sx={{ mt: 2 }}>
              <Box sx={{ display: 'flex', mb: 2 }}>
                {selectedGroupAWeaknesses.map((weakness) => (
                  <Chip
                    key={weakness._id}
                    label={weakness.name.en}
                    color="primary"
                    onDelete={() => handleWeaknessSelection(weakness, 'A')}
                    sx={{ mr: 1 }}
                  />
                ))}
              </Box>
              {renderWeaknessList(groupAWeaknesses, selectedGroupAWeaknesses, 'A')}
            </Box>
          </Box>
        );
      case 1:
        return (
          <Box>
            <Typography variant="h6" gutterBottom>
              Select 2 weaknesses from Group B
            </Typography>
            <Box sx={{ mt: 2 }}>
              <Box sx={{ display: 'flex', mb: 2 }}>
                {selectedGroupBWeaknesses.map((weakness) => (
                  <Chip
                    key={weakness._id}
                    label={weakness.name.en}
                    color="primary"
                    onDelete={() => handleWeaknessSelection(weakness, 'B')}
                    sx={{ mr: 1 }}
                  />
                ))}
              </Box>
              {renderWeaknessList(groupBWeaknesses, selectedGroupBWeaknesses, 'B')}
            </Box>
          </Box>
        );
      case 2:
        return (
          <Box>
            <Typography variant="h6" gutterBottom>
              Select 2 weaknesses from Group C
            </Typography>
            <Box sx={{ mt: 2 }}>
              <Box sx={{ display: 'flex', mb: 2 }}>
                {selectedGroupCWeaknesses.map((weakness) => (
                  <Chip
                    key={weakness._id}
                    label={weakness.name.en}
                    color="primary"
                    onDelete={() => handleWeaknessSelection(weakness, 'C')}
                    sx={{ mr: 1 }}
                  />
                ))}
              </Box>
              {renderWeaknessList(groupCWeaknesses, selectedGroupCWeaknesses, 'C')}
            </Box>
          </Box>
        );
      case 3:
        return (
          <Box>
            <Typography variant="h6" gutterBottom>
              Answer the following questions
            </Typography>
            {renderQuestions()}
          </Box>
        );
      default:
        return 'Unknown step';
    }
  };

  if (loading && activeStep < 3) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <CircularProgress />
          <Typography variant="h6" sx={{ mt: 2 }}>Loading...</Typography>
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Weakness Assessment
      </Typography>
      
      {error && <Alert severity="error" sx={{ mb: 3 }}>{error}</Alert>}
      
      <Stepper activeStep={activeStep} alternativeLabel sx={{ mb: 4 }}>
        {steps.map((label) => (
          <Step key={label}>
            <StepLabel>{label}</StepLabel>
          </Step>
        ))}
      </Stepper>
      
      <Box sx={{ mt: 2, mb: 4 }}>
        {getStepContent(activeStep)}
      </Box>
      
      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Button 
          disabled={activeStep === 0 || loading} 
          onClick={handleBack}
        >
          Back
        </Button>
        
        {activeStep === steps.length - 1 ? (
          <Button 
            variant="contained" 
            color="primary" 
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : 'Submit'}
          </Button>
        ) : (
          <Button 
            variant="contained" 
            color="primary" 
            onClick={handleNext}
            disabled={loading}
          >
            Next
          </Button>
        )}
      </Box>
    </Container>
  );
};

export default QuestionnaireForm;