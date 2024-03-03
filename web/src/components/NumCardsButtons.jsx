export function NumCardsButton (setNumCards) {
    return (
        <div>
            <input 
            type="radio" 
            value="5" 
            name="numCards" 
            onChange={(e) => setNumCards(e.target.value)} 
            defaultChecked 
        /> 5
        <input 
            type="radio" 
            value="10" 
            name="numCards" 
            onChange={(e) => setNumCards(e.target.value)} 
        /> 10
        <input 
            type="radio" 
            value="15" 
            name="numCards" 
            onChange={(e) => setNumCards(e.target.value)}
        /> 15
      </div>
    )
}