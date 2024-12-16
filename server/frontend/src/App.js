import React from "react";
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";  // Your Login component
import Register from "./components/Register/Register";  // Import the Register component

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />  {/* Login route */}
      <Route path="/register" element={<Register />} />  {/* Register route */}
    </Routes>
  );
}

export default App;
