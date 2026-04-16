"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def run_simulation(profile_name, user_prefs, songs):
    print(f"\n" + "="*60)
    print(f"   PROFILE: {profile_name}")
    print(f"   PREFS: {user_prefs}")
    print("="*60)
    
    recommendations = recommend_songs(user_prefs, songs, k=5)
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} | Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"   Why: {explanation}")
        print("-" * 60)

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"--- Loaded {len(songs)} songs from catalog ---")

    # 1. High-Energy Pop Profile
    pop_hero = {
        "genre": "pop", 
        "mood": "happy", 
        "energy": 0.9, 
        "likes_acoustic": False
    }
    
    # 2. Chill Lo-Fi Lover
    lofi_lover = {
        "genre": "lofi", 
        "mood": "chill", 
        "energy": 0.3, 
        "likes_acoustic": True
    }
    
    # 3. Adversarial / Edge Case: Conflicting Vibe
    # High energy requested, but "Chill" mood. How does the model react?
    conflicted = {
        "genre": "ambient", 
        "mood": "chill", 
        "energy": 0.9, 
        "likes_acoustic": False
    }

    profiles = [
        ("Gym Hero (High-Energy Pop)", pop_hero),
        ("Midnight Coder (Chill Lo-Fi)", lofi_lover),
        ("The Conflicted Listener (High Energy + Chill Mood)", conflicted)
    ]

    for name, prefs in profiles:
        run_simulation(name, prefs, songs)


if __name__ == "__main__":
    main()
