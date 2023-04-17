import React from 'react';
import CardComponent, {Card, SPADES} from "../card/card";
import './trick.css'

interface TrickComponentProps {
    trick: Card[];
    spadesBroken: boolean
}

function TrickComponent({trick, spadesBroken}: TrickComponentProps) {
    return (
        <div className={"trick"}>
            {trick.map(({suit, rank}) => (
                <CardComponent suit={suit} rank={rank}/>
            ))}
            <div className={`spades-broken ${spadesBroken ? "broken" : ""}`}>{SPADES}</div>
        </div>
    );
}


export default TrickComponent;