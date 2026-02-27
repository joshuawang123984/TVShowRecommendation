import { useState } from "react";
import { useFetch } from "./hooks/useFetch";
import bgImage from "../assets/tv_background.png";

export default function App() {
  const [input, setInput] = useState("");
  const [numberOfRecommendations, setNumberOfRecommendations] = useState(5);
  const { results, loading, error, searched, fetchRecommendations } = useFetch();

  async function handleSubmit(e) {
    e.preventDefault();
    await fetchRecommendations(input, numberOfRecommendations);
  }

  return (
    <div
      className="min-h-screen w-full relative flex flex-col items-center justify-start"
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        fontFamily: "'Courier New', Courier, monospace",
      }}
    >
      <div className="absolute inset-0 bg-black/30" />
      <div className="relative z-10 w-full max-w-2xl mt-[8vh] px-4">

        {/* header */}
        <div className="text-center mb-8">
          <h1
            className="text-4xl font-bold text-white tracking-widest uppercase mb-1"
            style={{ textShadow: "0 0 30px rgba(200,220,255,0.6)" }}
          >
            What to Watch?
          </h1>
          <p className="text-blue-200 text-sm tracking-widest uppercase opacity-70">
            Find your next show
          </p>
        </div>

        {/* search */}
        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-3 bg-white/5 border border-white/10 backdrop-blur-sm p-6 rounded-sm"
          style={{ boxShadow: "0 0 40px rgba(150,180,255,0.1)" }}
        >
          <div className="flex flex-col gap-1">
            <label className="text-blue-200 text-xs tracking-widest uppercase opacity-60">
              Show Name
            </label>
            <input
              className="bg-transparent border-b border-white/20 text-white placeholder-white/30 outline-none py-2 text-sm tracking-wide focus:border-blue-300 transition-colors"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="e.g. The Walking Dead"
              autoFocus
            />
          </div>

          <div className="flex flex-col gap-1">
            <label className="text-blue-200 text-xs tracking-widest uppercase opacity-60">
              Number of Recommendations (1–25)
            </label>
            <input
              type="number"
              min="1"
              max="25"
              className="bg-transparent border-b border-white/20 text-white placeholder-white/30 outline-none py-2 text-sm tracking-wide focus:border-blue-300 w-24"
              value={numberOfRecommendations}
              onChange={(e) => setNumberOfRecommendations(parseInt(e.target.value))}
            />
          </div>

          <button
            type="submit"
            className="mt-2 self-start px-6 py-2 text-xs tracking-widest uppercase text-black bg-white hover:bg-blue-100"
          >
            Search
          </button>
        </form>

        {/* loading */}
        {loading && (
          <p className="text-blue-200 text-xs tracking-widest uppercase text-center mt-6 animate-pulse">
            Searching...
          </p>
        )}

        {/* error */}
        {error && (
          <p className="text-red-400 text-xs tracking-widest uppercase text-center mt-6">
            {error}
          </p>
        )}

        {/* results */}
        {results.length > 0 && (
          <div className="mt-6 flex flex-col gap-2">
            <p className="text-blue-200 text-xs tracking-widest uppercase opacity-60 mb-2">
              Recommendations for "{searched}"
            </p>
            {results.map((r, i) => (
              <div
                key={i}
                className="flex justify-between items-center px-4 py-3 bg-white/5 border border-white/10 backdrop-blur-sm hover:bg-white/10"
              >
                <span className="text-white text-sm tracking-wide">{r.title}</span>
                <span className="text-blue-300 text-xs opacity-70">{r.score}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}