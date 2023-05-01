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
                    <th>{header}s</th>
                    <th>Score</th>
                    <th>Bags</th>
                </tr>
                </thead>
                <tbody>
                {scores.map((score, i) =>
                    <tr>
                        <td>{header} {i + 1}</td>
                        <td key={i}>{score}</td>
                        <td key={i + "bags"}>{bags[i]}</td>
                    </tr>
                )}
                </tbody>
            </table>
        </div>)
}


export default ScoreBoardComponent;
