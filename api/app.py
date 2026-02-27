from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

#for importing Recommender from models.recommender
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.recommender import Recommender

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:5173",
    "https://tvshowrecommendation.vercel.app"
])

recommender = Recommender(
    data_path='data/netflix_titles.csv',
    cache_path='data/embeddings.pt'
)
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    print("Received:", data)
    show_name = data.get('show_name')
    print("Show name:", show_name)
    
    results = recommender.recommend(show_name, k=5)
    print("Results:", results)
    
    return jsonify({'recommendations': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))