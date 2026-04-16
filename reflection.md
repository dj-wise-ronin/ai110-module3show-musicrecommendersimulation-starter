# 🎵 Evaluation Reflection

This document compares the outputs of different user profiles and examines how user preferences influence the final recommendations.

## Comparing Diverse Profiles

| Profile Name | Top Recommendation | Why it made sense |
|--------------|--------------------|-------------------|
| **Gym Hero** | *Sunrise City (Pop)* | High energy (0.9) and happy mood correctly prioritized the energetic pop sound. |
| **Midnight Coder** | *Library Rain (Lofi)* | Low energy (0.3) and chill mood correctly found the most relaxed, acoustic-leaning lofi track. |
| **Conflicted Listener** | *Spacewalk Thoughts (Ambient)* | Even though energy was 0.9, the initial genre/mood weights (2.0 and 1.5) kept this ambient track at #1. |

## The Impact of the "Weight Shift" Experiment

After changing the **Energy Weight** from 1.0 to 2.0 and the **Genre Weight** from 2.0 to 1.0:

- **The Change:** The system became much more responsive to the physical "intensity" of the music.
- **The Result:** For the *Conflicted Listener*, the system stopped being stuck in the "Ambient" bubble. Instead, it recommended **High-Energy Rock, Synthwave, and Techno**.
- **Conclusion:** This shows that user preferences (the inputs) are only as powerful as the **Algorithm Recipe** (the weights) allows them to be. In real-world systems like Spotify, "vibe" might actually matter more than "genre" depending on the playlist, and this experiment showed me exactly how that balance is achieved mathematically.

## Summary Reflection
Imagine explaining to a non-programmer: The "Gym Hero" song keeps showing up for people who just want "Happy Pop" because the system sees that a 100% match on genre (Pop) is worth way more than a 100% match on mood (Happy). If we want more variety, we have to make the "points" for mood almost as high as the "points" for genre.
