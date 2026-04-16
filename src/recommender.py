import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Ranks songs using weighted scoring and returns top k results.
        """
        # Convert user profile to dict format for score_song
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }
        
        scored_songs = []
        for song in self.songs:
            # Convert Song object to dict format for score_song
            song_dict = song.__dict__
            score, reasons = score_song(user_prefs, song_dict)
            scored_songs.append((song, score))
            
        # Sort by score descending
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [s[0] for s in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Provides a human-readable explanation for a recommendation.
        """
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }
        _, reasons = score_song(user_prefs, song.__dict__)
        return " and ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Loads and parses song data from a CSV file into a list of dictionaries."""
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric strings to appropriate types
                row['id'] = int(row['id'])
                row['energy'] = float(row['energy'])
                row['tempo_bpm'] = float(row['tempo_bpm'])
                row['valence'] = float(row['valence'])
                row['danceability'] = float(row['danceability'])
                row['acousticness'] = float(row['acousticness'])
                songs.append(row)
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a weighted relevance score and reasoning for a song based on user preferences."""
    score = 0.0
    reasons = []
    
    # 1. Genre Match (Weight: 2.0)
    if song.get('genre') == user_prefs.get('genre'):
        score += 2.0
        reasons.append(f"it matches your favorite genre ({song['genre']})")
        
    # 2. Mood Match (Weight: 1.5)
    if song.get('mood') == user_prefs.get('mood'):
        score += 1.5
        reasons.append(f"the mood is exactly {song['mood']}")
        
    # 3. Energy Proximity (Weight: 1.0)
    energy_diff = abs(song.get('energy', 0) - user_prefs.get('energy', 0.5))
    proximity_score = 1.0 - energy_diff
    score += proximity_score
    if energy_diff < 0.2:
        reasons.append("the energy level is just right")
        
    # 4. Acousticness preference (Weight: 1.0)
    # Using the 'likes_acoustic' bool from UserProfile
    likes_acoustic = user_prefs.get('likes_acoustic', False)
    song_acousticness = song.get('acousticness', 0)
    if (likes_acoustic and song_acousticness > 0.5) or (not likes_acoustic and song_acousticness <= 0.5):
        score += 1.0
        reasons.append("it matches your preference for acoustic/electronic sounds")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Generates a ranked list of the top k song recommendations with scores and explanations."""
    scored_results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " and ".join(reasons) if reasons else "It's a solid overall match."
        scored_results.append((song, score, explanation))
        
    # Sort by score descending
    scored_results.sort(key=lambda x: x[1], reverse=True)
    return scored_results[:k]
