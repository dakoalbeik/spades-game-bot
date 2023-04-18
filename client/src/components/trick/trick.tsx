import React from 'react';
import CardComponent, {Card, SPADES} from "../card/card";
import './trick.css'

interface TrickComponentProps {
    trick: Card[];
    spadesBroken: boolean,
    trickWinner: number
}

function TrickComponent({trick, spadesBroken, trickWinner}: TrickComponentProps) {
    return (
        <div className={"trick"}>
            {trick.map(({suit, rank}, i) => (
                <div className={`trick-card${(i + trickWinner) % 4}`}>
                    <CardComponent suit={suit} rank={rank}/>
                </div>
            ))}
            <div className={`spades-broken ${spadesBroken ? "broken" : ""}`}>{SPADES}</div>
        </div>
    );
}


export default TrickComponent;