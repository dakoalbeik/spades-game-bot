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

interface ScoreChartComponentProps {
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

export const colors = [
    '#ff2323',
    '#2443ff',
    '#e8cf00',
    '#0eda00',
]

function ScoresChartComponent({games_history}: ScoreChartComponentProps) {

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

export default ScoresChartComponent;