import React from 'react';

export interface Card {
    suit: string,
    rank: number
}

export const SPADES = "♠"
export const HEARTS = "♥"
export const CLUBS = "♣"
export const DIAMONDS = "♦"

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

function CardComponent({suit, rank}: Card) {
    return (
        <p className={`card ${suit === HEARTS || suit === DIAMONDS ? "red" : "black"}`}>{getRank(rank)}{suit}</p>
    );
}

export default CardComponent;
