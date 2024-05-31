import React, { useState } from 'react';
import './App.css'; // Import your CSS file for styling

function App() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleInput1Change = (e) => {
    setInput1(e.target.value);
  };

  const handleInput2Change = (e) => {
    setInput2(e.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8000/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input1: parseFloat(input1), input2: parseFloat(input2) }), // Convert input values to float
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch');
        }
        return response.json();
      })
      .then((data) => {
        // Handle successful response from backend
        setPrediction(data.prediction);
        setError(null);
      })
    
  };

  return (
    <div className="container">
      <div className="input-container">
        <input
          type="text"
          value={input1}
          onChange={handleInput1Change}
          placeholder="Enter Rice Production"
          className="input-field"
        />
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input2}
          onChange={handleInput2Change}
          placeholder="Enter Area"
          className="input-field"
        />
      </div>
      <button onClick={handleSubmit} className="submit-button">
        Submit
      </button>
      {prediction !== null && (
        <div className="prediction">
          <p>Prediction: {prediction}</p>
        </div>
      )}
      {error && (
        <div className="error">
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default App;
