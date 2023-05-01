import './App.css'
import {useEffect, useState} from "react";
import socket from './socket'
import {Card} from './components/card/card';
import TrickComponent from "./components/trick/trick";
import HandComponent from "./components/hand/hand";
import ScoreBoardComponent from "./components/score-board/scoreBoard";
import {Game} from "./components/chart/chart";


interface GameState {
    scores: number[],
    bags: number[],
    trick: Card[],
    bids: number[],
    tricks_won: number[],
    spades_broken: boolean,
    hands: Card[][],
    previous_trick_winner: number,
    games_history: Game[]
}

const initialState: GameState = {
    scores: [0, 0, 0, 0],
    bags: [0, 0, 0, 0],
    trick: [],
    bids: [0, 0, 0, 0],
    tricks_won: [0, 0, 0, 0],
    spades_broken: false,
    hands: [[], [], [], []],
    previous_trick_winner: 0,
    games_history: [
        {
            'rounds': [],
            'players': [],
            'scores': [0, 0, 0, 0]
        }
    ]
};

function App() {
    const [state, setState] = useState(initialState)
    useEffect(() => {
        socket.on("new-state", (_state) => {
            // console.log(_state)
            setState(_state)
        })
        socket.on("msg", (msg) => {
            console.log("msg", {msg})
        })
    }, [])


    return (
        <div className="App">
            {state.hands.map((hand, i) => (
                <HandComponent hand={hand} bid={state.bids[i]} tricksWon={state.tricks_won[i]}
                               trickWinner={state.previous_trick_winner === i}/>
            ))}
            <TrickComponent trick={state.trick} spadesBroken={state.spades_broken}
                            trickWinner={state.previous_trick_winner}/>
            <ScoreBoardComponent scores={state.scores} bags={state.bags}/>
            {/*<ChartComponent games_history={state.games_history}/>*/}
        </div>

    )
}

export default App
