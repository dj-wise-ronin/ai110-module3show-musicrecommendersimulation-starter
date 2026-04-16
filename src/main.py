"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"--- Loaded songs: {len(songs)} ---")

    # Target profile: Chill Lo-Fi Lover
    user_prefs = {
        "genre": "lofi", 
        "mood": "chill", 
        "energy": 0.35, 
        "likes_acoustic": True
    }

    print(f"\nGenerating recommendations for: {user_prefs['genre']} / {user_prefs['mood']}...")
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*40)
    print("      Top 5 Music Recommendations")
    print("="*40 + "\n")
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
