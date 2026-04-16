# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeEngine 1.0 (Weighted Context-Based Recommender)**

---

## 2. Goal / Task

VibeEngine 1.0 is designed to predict song relevance for a user based on their specific "taste profile." It calculates a numerical score for every song in its catalog to suggest the top 3-5 tracks that best match the user's current musical "vibe."

---

## 3. How the Model Works (Algorithm Summary)

The model uses a simple "Point System" to judge songs:
- **Genre & Mood:** It gives large "bonus points" if a song is in the user's favorite genre (+2.0) or matches their current mood (+1.5).
- **The Energy Gap:** It looks at how far a song's energy is from the user's target. The closer the song is to that target, the more points it gets (+1.0 max).
- **Acoustic Match:** It gives a small boost (+1.0) if the song is acoustic/electronic and matches the user's preference.

The system then ranks all songs from highest to lowest score and picks the winners.

---

## 4. Data  

- **Catalog Size:** 20 songs.
- **Features:** Genre, Mood, Energy (0.0-1.0), Tempo (BPM), Valence, and Acousticness.
- **Limitations:** The data is small and lacks variety in non-Western genres. It also depends on subjective tags (one person's "Happy" might be another's "Annoying").

---

## 5. Observed Behavior / Biases

- **The Genre Bubble:** Because Genre has the highest points, the system often recommends songs that match the genre but fail the "vibe" (energy/mood).
- **Data Imbalance:** Since 25% of the catalog is Lofi or Ambient, the system is naturally "better" at recommending chill music than high-energy metal or blues.
- **Linear Penalty:** It penalizes a song that is "slightly too fast" exactly the same as one that is "slightly too slow," which might not match how humans actually feel tempo.

---

## 6. Evaluation Process  

I tested the system using three distinct profiles:
1. **Gym Hero:** High energy/Pop.
2. **Midnight Coder:** Low energy/Lofi.
3. **The Conflicted Listener:** High energy requested, but Ambient genre preferred.
I also ran a **"Weight Shift" experiment** where I swapped the importance of Genre and Energy to see if I could break the "Genre Bubble" and recommend high-intensity music regardless of genre.

---

## 7. Intended Use and Non-Intended Use  

- **Intended Use:** For educational exploration of how recommendation scoring works.
- **Non-Intended Use:** This should **not** be used for a real music platform. It cannot handle more than a few dozen songs and doesn't understand user behavior (likes/skips) or song audio.

---

## 8. Ideas for Improvement  

- **Diversity Boost:** Add a rule that subtracts points if the Top 3 results are all from the same artist or genre.
- **Temporal Weighting:** Automatically increase the weight of "Mood" during late-night or early-morning hours.
- **Hybrid Logic:** Incorporate "Collaborative Filtering" (what other similar users liked).

---

## 9. Personal Reflection  

- **Biggest Learning Moment:** Seeing how a single change in weights (like doubling the Energy points) could turn a "boring" recommender into one that actually found interesting, high-intensity songs I hadn't considered. It showed me that the "personality" of an AI is really just a set of human-designed weights.
- **AI Tools Experience:** AI tools (like Copilot) were incredible for brainstorming the mathematical "Scoring Rules" and generating the expanded dataset. However, I had to double-check the math—sometimes the AI suggested a formula that would result in negative scores or wouldn't actually "reward" proximity correctly.
- **The "Feel" of Simple Code:** I was surprised that such a simple math loop (less than 50 lines of code) could produce results that felt "smart." It made me realize that even the most complex apps are often just layers of these simple logic-checks stacked on top of each other.
- **Next Steps:** If I kept going, I would try to implement a "Group Vibe" mode where it averages the tastes of 3 different users to find one song they would all enjoy.
