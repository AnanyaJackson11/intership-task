import { useState } from "react";
import api from "../services/api";

function TransactionForm() {

    const [transactionId,setTransactionId]=useState("");
    const [userId,setUserId]=useState("");
    const [amount,setAmount]=useState("");

    const [message,setMessage]=useState("");
    const [isError,setIsError]=useState(false);

    async function submitTransaction(){

        try{

            const response=await api.post("/transaction",{

                transaction_id:transactionId,

                user_id:userId,

                amount:Number(amount)

            });

            setMessage(response.data.message);
            setIsError(false);

            setTransactionId("");
            setUserId("");
            setAmount("");

        }

        catch(error){

            setIsError(true);

            if(error.response){

                setMessage(error.response.data.detail);

            }

            else{

                setMessage("Unable to connect to backend.");

            }

        }

    }

    return(

        <div className="card">

            <h2>Create Transaction</h2>

            <label>Transaction ID</label>

            <input

                value={transactionId}

                onChange={(e)=>setTransactionId(e.target.value)}

            />

            <label>User ID</label>

            <input

                value={userId}

                onChange={(e)=>setUserId(e.target.value)}

            />

            <label>Amount</label>

            <input

                type="number"

                value={amount}

                onChange={(e)=>setAmount(e.target.value)}

            />

            <button

                onClick={submitTransaction}

            >

                Submit Transaction

            </button>

            {

                message &&

                <p className={isError?"error":"success"}>

                    {message}

                </p>

            }

        </div>

    )

}

export default TransactionForm;