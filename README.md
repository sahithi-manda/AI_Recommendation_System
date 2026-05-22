# Project 3: AI Recommendation Logic

A simple recommendation system that suggests items based on user interests.

## What it does

1. **Takes user input** — interests entered at the prompt (comma-separated).
2. **Matches preferences** — scores each catalog item by tag overlap and partial matches.
3. **Displays recommendations** — top matches ranked by score.

## Run

```bash
python recommendation.py
```

Example input:

```
Your interests: coding, beginner, books
```

## How matching works

- Each item has **tags** (e.g. `coding`, `art`, `fitness`).
- User interests are normalized (lowercase, trimmed).
- **Exact tag match** → +2 points  
- **Partial match** (interest in tag or tag in interest) → +1 point  
- Items with score 0 are excluded; results are sorted highest first.

## Skills practiced

- Logic building (scoring and ranking)
- Pattern matching (tag vs. interest comparison)
- Recommendation concepts (content-based filtering)

## Customize

Edit the `ITEMS` list in `recommendation.py` to add your own courses, books, hobbies, or products with matching tags.
