

export function DisplayCards(cards, selectedCard, revealAnswer, numCards) {
    let side = revealAnswer ? "back" : "front";
    let sideCap = side === "front" ? "Front" : "Back";
    let cardText = cards[selectedCard][side];

    //return cardText;

    return (
        <div>
            <div className="cardtopleft">
                Card Number: {selectedCard + 1} of {numCards}
            </div>
            <div className="cardtopright">
                {sideCap}
            </div>
            <p style={{fontSize:"xx-large"}}>{cardText}</p>
        </div>
    )
}