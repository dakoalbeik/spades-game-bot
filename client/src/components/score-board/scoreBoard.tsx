import React from 'react';
import './score-board.css'

interface ScoreBoardComponentProps {
    scores: number[],
    bags: number[]
}

function ScoreBoardComponent({scores, bags}: ScoreBoardComponentProps) {
    const header = scores.length == 2 ? "Team" : "Player"

    return (
        <div className={"score-board"}>
            <table>
                <thead>
                <tr>
                    {scores.map((score, i) => (
                        <>
                            <th key={i}>{header} {i + 1}</th>
                            <th key={i + "bags"}>Bags</th>
                        </>
                    ))}
                </tr>
                </thead>
                <tbody>
                <tr>
                    {scores.map((score, i) => <>
                        <td key={i}>{score}</td>
                        <td key={i + "bags"}>{bags[i]}</td>
                    </>)}
                </tr>
                </tbody>
            </table>
        </div>)
}


export default ScoreBoardComponent;
