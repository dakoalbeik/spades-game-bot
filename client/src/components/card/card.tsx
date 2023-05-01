import React from 'react';
import './card.css'

export interface Card {
    suit: number,
    rank: number
}

export const SPADES = "♠"
export const HEARTS = "♥"
export const CLUBS = "♣"
export const DIAMONDS = "♦"


const SUIT_SYMBOL = {
    0: DIAMONDS,
    1: CLUBS,
    2: HEARTS,
    3: SPADES
}

const ORDER = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}

const getRank = (rank: number) => {
    // @ts-ignore
    return ORDER[rank] || rank
}

const getSuit = (suit: number) => {
    // @ts-ignore
    return SUIT_SYMBOL[suit]
}

function CardComponent({suit, rank}: Card) {
    return (
        <p key={rank + "" + suit}
           className={`card ${suit === 2 || suit === 0 ? "red" : "black"}`}>{getRank(rank)}{getSuit(suit)}</p>
    );
}

export default CardComponent;
