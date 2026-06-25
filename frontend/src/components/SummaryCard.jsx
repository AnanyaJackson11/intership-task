import { useState } from "react";
import api from "../services/api";

function SummaryCard(){

    const [userId,setUserId]=useState("");

    const [summary,setSummary]=useState(null);

    const [error,setError]=useState("");

    async function loadSummary(){

        try{

            const response=await api.get(

                `/summary/${userId}`

            );

            setSummary(response.data);

            setError("");

        }

        catch{

            setSummary(null);

            setError("User not found");

        }

    }

    return(

        <div className="card">

            <h2>User Summary</h2>

            <label>User ID</label>

            <input

                value={userId}

                onChange={(e)=>setUserId(e.target.value)}

            />

            <button

                onClick={loadSummary}

            >

                Get Summary

            </button>

            {

                error &&

                <p className="error">

                    {error}

                </p>

            }

            {

                summary &&

                <div style={{marginTop:"20px"}}>

                    <p>

                        <b>User</b>

                        <br/>

                        {summary.user_id}

                    </p>

                    <br/>

                    <p>

                        <b>Total Spent</b>

                        <br/>

                        ₹ {summary.total_spent}

                    </p>

                    <br/>

                    <p>

                        <b>Total Points</b>

                        <br/>

                        {summary.total_points}

                    </p>

                    <br/>

                    <p>

                        <b>Transactions</b>

                        <br/>

                        {summary.transaction_count}

                    </p>

                </div>

            }

        </div>

    )

}

export default SummaryCard;