import { useState } from "react";
import { useFetch } from "../hooks/useFetch";

export default function App() {
  const [input, setInput] = useState("")
  const [numberOfRecommendations, setNumberOfRecommendations] = useState(5);
  const { results, loading, error, searched, fetchRecommendations } = useFetch();

  async function handleSubmit(e) {
    e.preventDefault();
    await fetchRecommendations(input, numberOfRecommendations);
  }

  return (<>
    <div className="headr">
      <h1 className="">TV Show Recommendation</h1>
      <p className="">Enter a show name to find 5 similar shows</p>
    </div>

    <form onSubmit={handleSubmit} className="">
      <input
        className=""
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="e.g. The Walking Dead"
        autoFocus
      />
      <input
        className=""
        value={numberOfRecommendations}
        onChange={(e) => setNumberOfRecommendations(e.target.value)}
        placeholder="(1-25)"
        autoFocus
      />
      <button
        type="submit"
        className=""
      >
        search
      </button>
    </form>

    {
      loading && (
        <p className="">searching...</p>
      )
    }

    {
      error && (
        <p className="">error: {error}</p>
      )
    }

    {
      results.length > 0 && (
        <div className="flex flex-col gap-3">
          <p className="">recommendations for '{searched}':</p>
          {results.map((r, i) => (
            <div key={i} className="">
              <span className="">{r.title}</span>
              <span className="">similarity: {r.score}</span>
            </div>
          ))}
        </div>
      )
    }
  </>
  )
}