import { useState } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './App.css'
import './style.css'
import { OPENAI_API_KEY } from './Token' // MUST CREATE A FILE CALLED "Token.jsx" AND EXPORT OPEN_API_KEY VAR
import { Parse } from "./components/Parse"
import { DisplayCards } from "./components/DisplayCards"
import { NumCardsButton } from './components/NumCardsButtons'
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
  const [notes, setNotes] = useState("");
  const [cards, setCards] = useState("");
  const [reveal, setReveal] = useState(false);
  const [numCards, setNumCards] = useState("5");
  const [promtNumCards, setPromptNumCards] = useState(5)
  const [currCardNum, setCurrCardNum] = useState(0);
  const [feedback, setFeedback] = useState("Hello! Welcome to stUDy Buddy");
  const [isCards, setIsCards] = useState(false);

  //const numCards = 5; //controls the number of cards generated, make sure this reads as string


  async function callOpenAIAPI() {
    console.log("function logged")

    if (notes === "") {
      setFeedback("You need to input notes to generate flashcards.")
      return
    }

    setFeedback("Generating " + numCards.toString() + " Flashcards based on your notes (this may take some time)");
    setPromptNumCards(parseInt(numCards, 10))
    const API_Body = {
        "model": "gpt-4",
        "messages": [
          {
            "role": "system",
            "content": "You will be provided with study notes, your job is to turn these notes into" + numCards.toString() + " flashcards with a front that asks a question and a back that contains the answer. You will format the flashcards as a JSON file"
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

    setIsCards(true);
    setFeedback("Here are your card, happy studying!");
  }

  function flipCard() {
    if (reveal === true) {
      setReveal(false);
    }

    else {
      setReveal(true);
    }
  }

  function prevCard() {
    let curr = currCardNum - 1;
    if (curr >= 0 & curr < promtNumCards) {
      setCurrCardNum(curr);
    }

    else {
      setFeedback("You are on the first card, there are no previous cards.")
    }
  }

  function nextCard() {
    let curr = currCardNum + 1;
    if (curr >= 0 & curr < promtNumCards) {
      setCurrCardNum(curr);
    }

    else {
      setFeedback("You are on the last card, there is no next card.")
    }
  }

  /* function toggleButton() {
    console.log("toggle");
    let button1 = document.getElementById("card button 1")
    let button2 = document.getElementById("card button 2")
    let button3 = document.getElementById("card button 3")
    button1.disabled = !isCards
    button2.disabled = !isCards
    button3.disabled = !isCards
} */


  //Parse(cards)
  //console.log(notes)
  //console.log(apiKey)
  // ~~~~~~~~ HTML STARTS HERE ~~~~~~~~
  return (
    <div className='content'>
      <div>Number of Cards: {numCards}</div>
      <div>Prompt Number of Cards: {promtNumCards}</div>
      <div>Current Card Num: {currCardNum}</div>
      <div>Reveal: {reveal}</div>
      <div className='input'>
        <div style={{display: 'flex'}}>
          {NumCardsButton(setNumCards)}
          <button 
              onClick={callOpenAIAPI}
              className='buttontop'
            >
              Get Flashcards
            </button>
        </div>
        <textarea 
          onChange={(e) => setNotes(e.target.value)}
          placeholder='Paste your notes here!'
          cols={50}
          rows={10}
        />
      </div>
      <br/>
      <br/>
      <div>
        <button onClick={prevCard} className='buttonbottom' disabled={!isCards}>Previous Card</button>
        <button onClick={flipCard} className='buttonbottom' disabled={!isCards}>Reveal Answer</button>
        <button onClick={nextCard} className='buttonbottom' disabled={!isCards}>Next Card</button>
      </div>
      <div className='card'>
        {isCards ? DisplayCards(cards, currCardNum, reveal, promtNumCards) : null}
      </div>

      <div className="bottomtext">
        {feedback}
      </div>
    </div>
  )
}

export default App
