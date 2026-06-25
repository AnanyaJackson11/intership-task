import { useEffect,useState } from "react";

import api from "../services/api";

function Leaderboard(){

    const [users,setUsers]=useState([]);

    async function load(){

        try{

            const response=await api.get("/ranking");

            setUsers(response.data);

        }

        catch(err){

            console.log(err);

        }

    }

    useEffect(()=>{

        load();

        const timer=setInterval(load,5000);

        return ()=>clearInterval(timer);

    },[]);

    function medal(rank){

        if(rank===1) return "🥇";

        if(rank===2) return "🥈";

        if(rank===3) return "🥉";

        return rank;

    }

    return(

        <div className="card">

            <h2>Leaderboard</h2>

            <table>

                <thead>

                    <tr>

                        <th>Rank</th>

                        <th>User</th>

                        <th>Score</th>

                        <th>Points</th>

                        <th>Transactions</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        users.map(user=>(

                            <tr key={user.user_id}>

                                <td>

                                    {medal(user.rank)}

                                </td>

                                <td>

                                    {user.user_id}

                                </td>

                                <td>

                                    {user.score}

                                </td>

                                <td>

                                    {user.total_points}

                                </td>

                                <td>

                                    {user.transaction_count}

                                </td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </div>

    )

}

export default Leaderboard;