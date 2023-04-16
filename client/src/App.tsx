import './App.css'
import {useEffect, useState} from "react";
import socket from './socket'
import CardComponent, {Card} from './components/card/card';
import TrickComponent from "./components/trick/trick";


interface GameState {
    scores: number[];
    bags: number[];
    trick: Card[];
    bids: number[];
    tricks_won: number[];
    spades_broken: boolean;
    hands: Card[][];
}

const initialState: GameState = {
    scores: [0, 0, 0, 0],
    bags: [0, 0, 0, 0],
    trick: [],
    bids: [0, 0, 0, 0],
    tricks_won: [0, 0, 0, 0],
    spades_broken: false,
    hands: [[], [], [], []],
};

function App() {
    const [state, setState] = useState(initialState)
    useEffect(() => {
        socket.on("new-state", (_state) => {
            console.log(_state)
            setState(_state)
        })
        socket.on("msg", (msg) => {
            console.log("msg", {msg})
        })
    }, [])


    return (
        <div className="App">
            {state.hands.map(hand => (
                <div className={'hand'}>
                    {hand.map(({suit, rank}) => (
                        <CardComponent suit={suit} rank={rank}/>
                    ))}
                </div>
            ))}
            <TrickComponent trick={state.trick} spadesBroken={state.spades_broken}/>

        </div>

    )
}

export default App
