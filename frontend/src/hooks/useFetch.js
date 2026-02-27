import { useState } from "react"

export function useFetch() {
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [searched, setSearched] = useState("");

    async function fetchRecommendations(input, numOfRecommendations) {
        if (!input.trim()) return;
        setLoading(true);
        setError("");
        setResults([]);
        setSearched(input);

        try {
            const res = await fetch("https://tvshowrecommendation.onrender.com/recommend", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ show_name: input, num_of_recommendations: numOfRecommendations })
            });
            const data = await res.json();
            if (!res.ok) setError(data.error || "Something went wrong");
            else setResults(data.recommendations);
        } catch {
            setError("Could not connect to server");
        } finally {
            setLoading(false);
        }
    }

    return { results, loading, error, searched, fetchRecommendations };
}