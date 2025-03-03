import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

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

function App() {
    return (
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
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/main-virtues" element={<MainVirtues />} />
                <Route
                    path="/create-main-virtue"
                    element={<CreateMainVirtue />}
                />
                <Route
                    path="/update-main-virtue/:id"
                    element={<UpdateMainVirtue />}
                />
                <Route path="/subvirtues" element={<SubVirtues />} />
                <Route path="/create-subvirtue" element={<CreateSubVirtue />} />
                <Route
                    path="/update-subvirtue/:id"
                    element={<UpdateSubVirtue />}
                />
                <Route path="/weaknesses" element={<Weaknesses />} />
                <Route path="/create-weakness" element={<CreateWeakness />} />
                <Route path="/questions" element={<Questions />} />
                <Route path="/create-question" element={<CreateQuestion />} />
                <Route path="/form-testing" element={<SignUpForm />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
