import { useEffect, useState } from "react";
import api from "../services/api";

function DashboardStats() {

    const [stats,setStats]=useState({

        users:0,

        highestScore:0,

        averageScore:0,

        leaderboardSize:0

    });

    async function loadStats(){

        try{

            const response=await api.get("/ranking");

            const data=response.data;

            if(data.length===0){

                return;

            }

            const highest=data[0].score;

            const average=(
                data.reduce((sum,item)=>sum+item.score,0)
                /data.length
            ).toFixed(2);

            setStats({

                users:data.length,

                leaderboardSize:data.length,

                highestScore:highest,

                averageScore:average

            });

        }

        catch(err){

            console.log(err);

        }

    }

    useEffect(()=>{

        loadStats();

        const timer=setInterval(loadStats,5000);

        return ()=>clearInterval(timer);

    },[]);

    return(

        <div
            style={{
                display:"grid",
                gridTemplateColumns:"repeat(4,1fr)",
                gap:"20px"
            }}
        >

            <div className="card">

                <h3>👥 Users</h3>

                <h1>{stats.users}</h1>

            </div>

            <div className="card">

                <h3>🏆 Highest Score</h3>

                <h1>{stats.highestScore}</h1>

            </div>

            <div className="card">

                <h3>📈 Avg Score</h3>

                <h1>{stats.averageScore}</h1>

            </div>

            <div className="card">

                <h3>🎯 Leaderboard</h3>

                <h1>{stats.leaderboardSize}</h1>

            </div>

        </div>

    )

}

export default DashboardStats;