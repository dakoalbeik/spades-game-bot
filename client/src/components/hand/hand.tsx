import React from 'react';
import CardComponent, {Card} from "../card/card";
import './hand.css'

interface HandComponentProps {
    hand: Card[],
    bid: number,
    tricksWon: number,
}

function HandComponent({hand, bid, tricksWon}: HandComponentProps) {
    return (
        <div className={'hand'}>
            <div className={'hand-info'}>
                <p>{tricksWon}/{bid}</p>
            </div>
            <div className={'hand-cards'}>
                {hand.map(({suit, rank}) => (
                    <CardComponent suit={suit} rank={rank} key={`${rank} of ${suit}`}/>
                ))}
            </div>
        </div>

    );
}

export default HandComponent;