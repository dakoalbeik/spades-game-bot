import React from "react";
import '../chart.css'
import {colors, Game} from "./line_chart";
import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip,} from 'chart.js';
import {Bar} from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

interface AchievementChartComponentProps {
    games_history: Game[]
}

interface ChartData {
    labels: string[];
    datasets: {
        label: string;
        data: number[];
        backgroundColor: string;
    }[];
    type: string;
}

function AchievementBarChart({games_history}: AchievementChartComponentProps) {
    const getLabels = () => {
        const labels: string[] = [];
        for (let i = 0; i < games_history[0].players.length; i++) {
            labels.push(games_history[0].players[i])
        }
        return labels;
    }

    const collectGameData = () => {


        const sets = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        games_history.forEach((game) => {
            game.rounds.forEach(({tricks, bids}) => {
                tricks.forEach((trick, i) => {
                    if (trick == bids[i]) {
                        sets[1][i] += 1
                    } else if (trick > bids[i]) {
                        sets[2][i] += 1
                    } else {
                        sets[0][i] += 1
                    }
                })
            })
        })

        let percent_total = [
            sets[0][0] + sets[1][0] + sets[2][0],
            sets[0][1] + sets[1][1] + sets[2][1],
            sets[0][2] + sets[1][2] + sets[2][2],
            sets[0][3] + sets[1][3] + sets[2][3]
        ]

        let percent_under = [
            sets[0][0] / percent_total[0], // agent 1
            sets[0][1] / percent_total[1], // agent 2
            sets[0][2] / percent_total[2], // agent 3
            sets[0][3] / percent_total[3], // agent 4
        ]
        let percent_met = [
            sets[1][0] / percent_total[0], // agent 1
            sets[1][1] / percent_total[1], // agent 2
            sets[1][2] / percent_total[2], // agent 3
            sets[1][3] / percent_total[3], // agent 4
        ]
        let percent_over = [
            sets[2][0] / percent_total[0], // agent 1
            sets[2][1] / percent_total[1], // agent 2
            sets[2][2] / percent_total[2], // agent 3
            sets[2][3] / percent_total[3], // agent 4
        ]

        // Create a Chart.js data object with the collected data
        const data: ChartData = {
            labels: getLabels(),
            datasets: [
                {
                    label: `Didn't Meet`,
                    data: percent_under,   // agent1, agent2, agent3, agent4
                    backgroundColor: colors[0]
                },
                {
                    label: 'Met',
                    data: percent_met,
                    backgroundColor: colors[1]
                },
                {
                    label: 'Exceeded',
                    data: percent_over,
                    backgroundColor: colors[2]
                },
            ],
            type: 'bar',
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
                text: `Agents' Bidding Performance`,
            },
        },
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true,
            },
        },
    };

    return (
        <div className={'wrapper'}>
            <div className={'model'}>
                <Bar data={collectGameData()} options={options}/>
            </div>
        </div>
    )
}

export default AchievementBarChart;