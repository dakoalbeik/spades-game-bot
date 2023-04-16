import './App.css'
import {useEffect, useState} from "react";
import socket from './socket'

const SPADES = "♠"
const HEARTS = "♥"
const CLUBS = "♣"
const DIAMONDS = "♦"

const ORDER = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}

interface Card {
    suit: string,
    rank: number
}

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


    const getRank = (rank: number) => {
        // @ts-ignore
        return ORDER[rank] || rank
    }


    return (
        <div className="App">
            {state.hands.map(hand => (
                <div className={'hand'}>
                    {hand.map(({suit, rank}) => (
                        <p className={`card ${suit === HEARTS || suit === DIAMONDS ? "red" : "black"}`}>{getRank(rank)}{suit}</p>
                    ))}
                </div>
            ))}
        </div>

    )
}

export default App
