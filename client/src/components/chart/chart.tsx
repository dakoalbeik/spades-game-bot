import React, {useState} from "react";
import './chart.css'
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

function generateArrayOfArrays(): number[][] {
    const arr: number[][] = [];
    for (let i = 0; i < 4; i++) {
        const subArr: number[] = [];
        for (let j = 0; j < 300; j++) {
            subArr.push(Math.floor(Math.random() * 701) - 200);
        }
        arr.push(subArr);
    }
    return arr;
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
    const [labels, setLabels] = useState<string[]>([]);
    // const [data, setData] = useState<ChartData>({
    //     labels: [],
    //     datasets: [],
    //     type: ''
    // });


    const getLabels = () => {
        return games_history.map((game, i) => `Game ${i}`)
    }


    const collectGameData = () => {


        const scoresHistory: number[][] = [[], [], [], []]


        games_history.forEach(game => {
            scoresHistory.forEach((playerScore, i) => {

                if (game.scores.length === 0) return;

                playerScore.push(game.scores[i])
            })

        })


        // Create a Chart.js data object with the collected data
        const data: ChartData = {
            labels: getLabels(),
            datasets: scoresHistory.map((score, i) => ({
                label: `Agent ${i}`,
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

export default ChartComponent;