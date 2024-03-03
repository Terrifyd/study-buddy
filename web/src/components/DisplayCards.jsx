

export function DisplayCards(cards, selectedCard, revealAnswer) {
    let side = revealAnswer ? "back" : "front";
    let sideCap = side === "front" ? "Front" : "Back";
    let cardText = cards[selectedCard][side];

    //return cardText;

    return (
        <div>
            <div className="cardtopleft">
                Card Number: {selectedCard + 1}
            </div>
            <div className="cardtopright">
                {sideCap}
            </div>
            <p>{cardText}</p>
        </div>
    )
}