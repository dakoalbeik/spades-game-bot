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