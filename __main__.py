import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from models.recommender import Recommender

def main():
    recommender = Recommender(
        data_path=os.path.join(BASE_DIR, 'data', 'netflix_titles.csv'),
        cache_path=os.path.join(BASE_DIR, 'data', 'embeddings.pt')
    )

    while True:
        show_name = input("Enter a show name (or 'quit' to exit): ").strip()
        if show_name.lower() == 'quit':
            break

        results = recommender.recommend(show_name, k=5)

        if results is None:
            print(f"Show '{show_name}' not found in dataset.")
        else:
            print(f"\nTop recommendations for '{show_name}':")
            for show in results:
                print(f"  {show['title']} — similarity: {show['score']}")
        print()

if __name__ == '__main__':
    main()