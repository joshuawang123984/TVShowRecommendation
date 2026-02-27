from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

#for importing Recommender from models.recommender
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from models.recommender import Recommender

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:5173",
    "https://tvshowrecommendation.vercel.app"
])

recommender = Recommender(
    data_path=os.path.join(BASE_DIR, 'data', 'netflix_titles.csv'),
    embeddings_path=os.path.join(BASE_DIR, 'data', 'embeddings.pt')
)

#for creating new model
'''recommender = Recommender(
    data_path='data/netflix_titles.csv',
    cache_path='data/embeddings.pt'
)'''

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    print("Received:", data)
    show_name = data.get('show_name')
    print("Show name:", show_name)

    k = data.get('num_of_recommendations')
    print("k:", k)
    
    #can make this take user input for k from (1-25) but 5 is default
    if (k == None or k == "" or not isinstance(k, int)) or (k < 1 or k > 25):
        k = 5

    results = recommender.recommend(show_name, k=k)
    print("Results:", results)
    
    return jsonify({'recommendations': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))