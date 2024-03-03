import React from 'react';
import './App.css';
import { Test } from './components/test';
import OpenAI from "openai";
import { OPENAI_API_KEY } from './Token';

// require('dotenv').config();


function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <Test></Test> */}
        <textarea 
          placeholder='Paste Notes Here'
          cols={50}
          rows={10}>
              
        </textarea>
      </header>
    </div>
  );
}

export default App;
