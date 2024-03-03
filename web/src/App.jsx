import { useState } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './App.css'
import { OPENAI_API_KEY } from './Token' // MUST CREATE A FILE CALLED "Token.jsx" AND EXPORT OPEN_API_KEY VAR
import { Parse } from "./components/Parse"
// import OpenAI from "openai";

/* const openai = new OpenAI();
async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}
main(); */

function App() {
  let apiKey = OPENAI_API_KEY;
  const [notes, setNotes] = useState("")
  const [cards, setCards] = useState("")


  async function callOpenAIAPI() {
    console.log("function logged")

    const API_Body = {
        "model": "gpt-4",
        "messages": [
          {
            "role": "system",
            "content": "You will be provided with study notes, your job is to turn these notes into 5 flashcards with a front that asks a question and a back that contains the answer. You will format the flashcards as a JSON file"
          },
          {
            "role": "user",
            "content": "Here are the study notes deliminated by two curly braces: {{" + notes + "}}"
          }
        ],
        "temperature": 0.5,
        "max_tokens": 500,
        "top_p": 1
    }

    await fetch("https://api.openai.com/v1/chat/completions" , {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey
      },
      body: JSON.stringify(API_Body)
    }).then((data) => {
      return data.json();
    }).then((data) => {
      console.log(data);
      let results = Parse(data.choices[0].message.content);

      setCards(results) //stores the json in cards
    })

  }

  //Parse(cards)
  //console.log(notes)
  //console.log(apiKey)
  return (
    <div>
      <div>
        <textarea 
          onChange={(e) => setNotes(e.target.value)}
          placeholder='Paste your notes here!'
          cols={50}
          rows={10}
        />
      </div>
      <div>
        <button onClick={callOpenAIAPI}>Get Flashcards</button>
        {cards !== "" ? <p>Your cards: {cards[0]["front"]} </p> : null}
      </div>

    </div>
  )
}

export default App
