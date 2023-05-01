import React from "react";
import '../chart.css'
import {
    CategoryScale,
    Chart as ChartJS,
    Legend,
    LinearScale,
    LineElement,
    PointElement,
    Title,
    Tooltip,
} from 'chart.js';
import {Line} from "react-chartjs-2";
import socket from "../../../socket";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

interface Round {
    tricks: number[],
    bids: number[]
}

export interface Game {
    scores: number[],
    players: string[],
    rounds: Round[]
}

interface ChartComponentProps {
    games_history: Game[]
}

interface ChartData {
    labels: string[];
    datasets: {
        label: string;
        data: number[];
        borderColor: string;
        fill: boolean;
    }[];
    type: string;
}


/*
*
* ------CHARTS NEEDED-------
* 1) Bar chart - for underachieved, overachieved, met (each version?)
* 2) Line chart - Score History (each game not round)
* 3) Line chart - Win Against Diff Agents (rolling 100 game avg)
* 4) Pie chart - Winning Percentage (DQN vs other heuristic agents)
*
* */

const colors = [
    '#ff2323',
    '#2443ff',
    '#e8cf00',
    '#0eda00',
]

function ChartComponent({games_history}: ChartComponentProps) {

    const getLabels = () => {
        return games_history.map((game, i) => `Game ${i + 1}`)
    }

    const getWinPercentage = () => {
        let winCount = 0
        games_history.forEach(game => {
            let winner = 0
            let highScore = 0
            game.scores.forEach((score, i) => {
                if (score > highScore) {
                    winner = i
                    highScore = score
                }
            })
            if (winner === 0) {
                winCount++
            }
        })
        const percentage = (winCount / games_history.length) * 100
        return percentage.toFixed(2)
    }

    const collectGameData = () => {


        const scoresHistory: number[][] = [[], [], [], []]


        games_history.forEach(game => {
            game.scores.forEach((score, i) => {
                scoresHistory[i].push(score)
            })

        })

        // Create a Chart.js data object with the collected data
        const data: ChartData = {
            labels: getLabels(),
            datasets: scoresHistory.map((score, i) => ({
                label: games_history[0]?.players[i],
                data: score,
                borderColor: colors[i],
                fill: false
            })),
            type: 'line',
        }

        return data
    }


    const options = {
        responsive: true,
        animation: {
            duration: 0,
        },
        plugins: {
            legend: {
                position: 'top' as const,
            },
            title: {
                display: true,
                text: `Agents' Score History`,
            },
        },
    }


    return (
        <div className={'wrapper'}>
            <div className={'model'}>
                {/*<div id={'score_history'}>*/}
                <span>Win percentage: {getWinPercentage()}%</span>
                <Line
                    data={collectGameData()}
                    options={options}
                />
                {/*</div>*/}
            </div>
        </div>

    )
}

export default ChartComponent;