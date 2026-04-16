# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeEngine 1.0 (Weighted Context-Based Recommender)**

---

## 2. Intended Use  

This recommender is designed to simulate how music streaming platforms match song attributes to user preferences. It generates a ranked list of the top 3-5 songs from a small catalog based on a user's favorite genre, mood, target energy, and acoustic preference. This model is intended for classroom exploration and educational purposes only.

---

## 3. How the Model Works  

VibeEngine 1.0 uses a "Weighted Scoring" approach to compare songs. It looks at several features:
- **Genre and Mood:** It gives high priority (bonus points) to songs that exactly match the user's favorite genre and current mood.
- **Energy and Positiveness:** It measures the "distance" between the song's energy level and what the user wants, rewarding songs that are closer to the target.
- **Acoustic vs. Electronic:** It checks if the song's acousticness matches whether the user likes acoustic or electronic music.

Each match is multiplied by a "weight" (Genre is worth more than Energy, for example) to calculate a final score. The songs with the highest total scores are recommended first.

---

## 4. Data  

The model uses a small dataset (`songs.csv`) containing 10 tracks.
- **Genres:** Pop, Lofi, Rock, Ambient, Jazz, Indie Pop, Synthwave.
- **Moods:** Happy, Chill, Intense, Relaxed, Moody, Focused.
- **Attributes:** All songs have numeric values for energy, valence (positiveness), tempo, and acousticness.
- **Limitations:** The dataset is very small and primarily reflects a modern, Western-centric selection of genres.

---

## 5. Strengths  

- **Predictability:** The model is very good at matching specific genres and moods. If you say you like "Pop" and "Happy," it reliably finds the most energetic Pop songs.
- **Transparency:** Because the weights are clear, a user can easily understand *why* a song was recommended (e.g., "it matches your genre and energy").
- **Precision in Vibe:** The distance-based energy rule works better than a simple threshold for users who want mid-range, "chill" vibes.

---

## 6. Limitations and Bias 

- **Overfitting to Genre:** Because Genre has a high weight, the system might recommend a song just because it's "Pop," even if the other attributes (energy, mood) are a poor match.
- **Filter Bubbles:** The model never suggests songs outside of the user's favorite genre, which can lead to a very repetitive listening experience.
- **Acoustic Binary:** The "likes_acoustic" preference is a simple yes/no, which ignores users who enjoy a mix of both acoustic and electronic textures.
- **Small Catalog Bias:** In such a small dataset, some genres (like Synthwave or Jazz) only have one song, meaning those users will always get the same single recommendation.

---

## 7. Evaluation  

I evaluated the system by creating several "extreme" user profiles:
- **The Gym Hero:** High energy, Pop genre, Happy mood.
- **The Midnight Coder:** Low energy, Lofi genre, Chill mood.
- **The Metalhead (Testing mismatch):** High energy, Rock genre, but no Rock songs in the catalog (The system correctly fell back to the next best match based on energy).
I compared the results to my own intuition and found that the Genre and Mood weights correctly prioritized the "feel" of the music.

---

## 8. Future Work  

- **Diversity Penalty:** I would add a "diversity score" that subtracts points from songs in the same genre if the top 3 are already full of that genre.
- **Dynamic Weighting:** Allowing users to choose which feature matters most to them (e.g., "vibe over genre").
- **Temporal Context:** Incorporating the time of day into the mood calculation.

---

## 9. Personal Reflection  

I learned that building a recommender is a balance between mathematical precision and human intuition. What surprised me was how a tiny change in weights (like moving Genre from 1.0 to 2.0) could completely shift the "personality" of the algorithm. This project made me realize that even the most advanced apps like Spotify are still fundamentally built on these types of human-designed rules and data hierarchies.
