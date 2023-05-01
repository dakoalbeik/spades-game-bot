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


        // Create a Chart.js data object with the collected data
        const data: ChartData = {
            labels: getLabels(),
            // datasets: scoresHistory.map((score, i) => ({
            //     label: games_history[0]?.players[i],
            //     data: score,
            //     borderColor: colors[i],
            //     fill: false
            // })),
            datasets: [
                {
                    label: 'Underachieved',
                    data: [200, 521, 276, 160],   // agent1, agent2, agent3, agent4
                    backgroundColor: colors[0]
                },
                {
                    label: 'Met',
                    data: [100, 250, 126, 517],
                    backgroundColor: colors[1]
                },
                {
                    label: 'Overachieved',
                    data: [300, 330, 432, 134],
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
                text: 'Chart.js Bar Chart',
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