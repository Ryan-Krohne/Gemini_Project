import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/navigation';
import LandingPage from './landingpage'; 
import GeminiPage from './geminipage';
import ContactPage from './contact'; 
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Routes>
          <Route path="/" exact element={<LandingPage />} />
          <Route path="/geminipage" element={<GeminiPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
