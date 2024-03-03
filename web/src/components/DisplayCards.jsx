

export function DisplayCards(cards, selectedCard, revealAnswer) {
    let side = revealAnswer ? "back" : "front";
    let cardText = cards[selectedCard][side];

    return cardText;

    //return (<div></div>)
}