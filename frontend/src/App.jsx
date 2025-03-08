// src/App.jsx
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";
import NavigationBar from "./components/Navbar";

import Home from "./pages/Home";
import MainVirtues from "./pages/MainVirtues";
import CreateMainVirtue from "./pages/MainVirtueCreate";
import UpdateMainVirtue from "./pages/MainVirtueUpdate";
import SubVirtues from "./pages/SubVirtues";
import CreateSubVirtue from "./pages/CreateSubVirtue";
import Weaknesses from "./pages/Weaknesses";
import CreateWeakness from "./pages/CreateWeakness";
import Questions from "./pages/Questions";
import CreateQuestion from "./pages/CreateQuestion";
import UpdateSubVirtue from "./pages/SubVirtueUpdate";
import SignUpForm from "./pages/SignUpForm";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import QuestionnaireForm from "./pages/QuestionnaireForm";
import QuestionnaireDetail from "./pages/QuestionnaireDetail";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <ToastContainer
          position="top-right"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
        />
        <NavigationBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUpForm />} />
          
          {/* Profile and Questionnaire routes */}
          <Route path="/profile" element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          } />
          <Route path="/questionnaire" element={
            <ProtectedRoute>
              <QuestionnaireForm />
            </ProtectedRoute>
          } />
          <Route path="/questionnaire/:id" element={
            <ProtectedRoute>
              <QuestionnaireDetail />
            </ProtectedRoute>
          } />
          
          {/* Admin routes */}
          <Route path="/main-virtues" element={
            <ProtectedRoute>
              <MainVirtues />
            </ProtectedRoute>
          } />
          <Route path="/create-main-virtue" element={
            <ProtectedRoute>
              <CreateMainVirtue />
            </ProtectedRoute>
          } />
          <Route path="/update-main-virtue/:id" element={
            <ProtectedRoute>
              <UpdateMainVirtue />
            </ProtectedRoute>
          } />
          <Route path="/subvirtues" element={
            <ProtectedRoute>
              <SubVirtues />
            </ProtectedRoute>
          } />
          <Route path="/create-subvirtue" element={
            <ProtectedRoute>
              <CreateSubVirtue />
            </ProtectedRoute>
          } />
          <Route path="/update-subvirtue/:id" element={
            <ProtectedRoute>
              <UpdateSubVirtue />
            </ProtectedRoute>
          } />
          <Route path="/weaknesses" element={
            <ProtectedRoute>
              <Weaknesses />
            </ProtectedRoute>
          } />
          <Route path="/create-weakness" element={
            <ProtectedRoute>
              <CreateWeakness />
            </ProtectedRoute>
          } />
          <Route path="/questions" element={
            <ProtectedRoute>
              <Questions />
            </ProtectedRoute>
          } />
          <Route path="/create-question" element={
            <ProtectedRoute>
              <CreateQuestion />
            </ProtectedRoute>
          } />
          <Route path="/form-testing" element={<SignUpForm />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;