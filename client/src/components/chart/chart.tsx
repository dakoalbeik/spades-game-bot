import React from "react";
import {Game} from "./charts/line_chart";
import AchievementBarChart from "./charts/bar_chart";


/*
*
* ------CHARTS NEEDED-------
* 1) Bar chart - for underachieved, overachieved, met (each version?)
* 2) Line chart - Score History (each game not round)
* 3) Line chart - Win Against Diff Agents (rolling 100 game avg)
* 4) Pie chart - Winning Percentage (DQN vs other heuristic agents)
*
* */

interface ChartComponentProps {
    games_history: Game[]
}

function ChartComponent({games_history}: ChartComponentProps) {
    return (
        <div>
            {/*<ScoresChartComponent games_history={games_history}/>*/}
            <AchievementBarChart games_history={games_history}/>
        </div>
    )
}

export default ChartComponent;