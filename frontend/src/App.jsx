import "./App.css";

import DashboardStats from "./components/DashboardStats";
import TransactionForm from "./components/TransactionForm";
import SummaryCard from "./components/SummaryCard";
import Leaderboard from "./components/Leaderboard";

function App() {
  return (
    <div className="app">

      <header className="hero">

        <h1>🏆 Reward Ranking Dashboard</h1>

        <p>
          Loyalty Reward & Transaction Monitoring System
        </p>

      </header>

      <DashboardStats />

      <div className="grid">

        <TransactionForm />

        <SummaryCard />

      </div>

      <Leaderboard />

    </div>
  );
}

export default App;