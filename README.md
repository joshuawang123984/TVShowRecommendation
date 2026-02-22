# TV Show Recommendation

A machine learning recommender system that suggests similar TV shows based on natural language descriptions. Built using transformer-based sentence embeddings and cosine similarity to match shows by semantic meaning rather than keywords.

## How It Works

The system encodes TV show descriptions from the Netflix dataset into high-dimensional vector embeddings using SentenceTransformers. When a user inputs a show name, the model finds the closest matching shows in embedding space using cosine similarity and returns ranked recommendations with similarity scores.

## Features

- Semantic similarity search across 1,000+ Netflix show descriptions
- Transformer-based embeddings using SentenceTransformers
- SGD feedback retraining to improve recommendations based on user input
- Similarity scores displayed for each recommendation

## Tech Stack

- Python 3.8+
- PyTorch
- SentenceTransformers
- NumPy
- Tkinter (current UI)

## Dataset

Uses the [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) dataset from Kaggle (`netflix_titles.csv`).

## Installation

1. Clone the repository
```bash
git clone https://github.com/joshuawang123984/ShowRecommendation.git
cd ShowRecommendation
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
python recommend.py
```

## Usage

Enter a TV show name in the search bar and the system will return the most similar shows ranked by similarity score. You can submit feedback on recommendations to retrain the model.

## Planned Features

- Flask REST API backend to serve recommendations
- React frontend replacing Tkinter for a modern web interface
- Deeper ML customization including custom similarity scoring and improved embedding fine-tuning
- Expanded dataset support beyond Netflix

## License

MIT