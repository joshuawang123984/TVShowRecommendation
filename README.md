
READ ME NEEDS TO BE MODIFIED!!!, change techstack, features (more netflix descriptions, inaccuracies, etc), maybe installation
# TV Show Recommendation

A machine learning recommender system that suggests similar TV shows based on natural language descriptions. Built using transformer-based sentence embeddings and cosine similarity to match shows by semantic meaning rather than keywords.

## Live Demo

https://tvshowrecommendation.vercel.app/

## How It Works

The system encodes 8,000+ Netflix show descriptions into 768-dimensional vector embeddings using a BERT-based transformer with mean pooling. When a user inputs a show name, the backend computes cosine similarity between the query embedding and all other embeddings, returning the top N most similar shows ranked by score.
Embeddings are precomputed and cached so the server loads instantly without running the model at runtime.

## Features

- Semantic similarity search across 8,000+ Netflix show descriptions
- BERT-based transformer embeddings implemented from scratch with mean pooling
- Cosine similarity computed via matrix multiplication for efficient batch comparisons
- Precomputed embedding cache for fast server startup
- Flask REST API backend
- React frontend

## Tech Stack

- Python 3.11+
- PyTorch
- Transformers (HuggingFace)
- Flask
- Flask-CORS
- Pandas

## Dataset

Uses the [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) dataset from Kaggle (`netflix_titles.csv`).

## Usage

The app is live at [tvshowrecommendation.vercel.app](https://tvshowrecommendation.vercel.app) — no installation needed.

For local development, follow the steps below.

## Installation

1. Clone the repository
```bash
git clone https://github.com/joshuawang123984/TVShowRecommendation.git
cd TVShowRecommendation
```

2. Install Python dependencies
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies
```bash
cd frontend
npm install
```

4. Run the Flask backend
```bash
python api/app.py
```

5. Run the React frontend
```bash
cd frontend
npm run dev
```

## API

**POST** `/recommend`

```json
{
  "show_name": "The Walking Dead",
  "num_of_recommendations": 5
}
```

Response:
```json
{
  "recommendations": [
    { "title": "Black Summer", "score": 0.904 },
    { "title": "Bird Box", "score": 0.867 }
  ]
}
```

## Planned Features

- Expanded dataset support beyond Netflix
- Improved embedding fine-tuning for higher accuracy
- User feedback loop to improve recommendations over time
