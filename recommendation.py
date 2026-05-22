"""
Project 3: AI Recommendation Logic
A simple recommendation system based on user preferences.
"""

# Catalog: each item has a name, description, and tags (interests it matches)
ITEMS = [
    {
        "name": "Python Crash Course",
        "description": "Hands-on intro to Python programming.",
        "tags": ["coding", "python", "beginner", "tech"],
    },
    {
        "name": "The Pragmatic Programmer",
        "description": "Classic guide to becoming a better developer.",
        "tags": ["coding", "career", "tech", "books"],
    },
    {
        "name": "Blender 3D Basics",
        "description": "Learn 3D modeling and animation from scratch.",
        "tags": ["design", "creative", "3d", "art"],
    },
    {
        "name": "Digital Photography 101",
        "description": "Composition, lighting, and editing for beginners.",
        "tags": ["photography", "creative", "art", "hobby"],
    },
    {
        "name": "Yoga for Beginners",
        "description": "Gentle flows to build flexibility and calm.",
        "tags": ["fitness", "wellness", "health", "relaxation"],
    },
    {
        "name": "HIIT Home Workouts",
        "description": "Short, intense sessions - no gym required.",
        "tags": ["fitness", "health", "active", "beginner"],
    },
    {
        "name": "Intro to Machine Learning",
        "description": "Concepts and small projects with scikit-learn.",
        "tags": ["coding", "ai", "data", "tech", "advanced"],
    },
    {
        "name": "Watercolor Painting",
        "description": "Color theory and simple landscape projects.",
        "tags": ["art", "creative", "painting", "hobby"],
    },
    {
        "name": "Personal Finance Basics",
        "description": "Budgeting, saving, and smart spending habits.",
        "tags": ["finance", "life skills", "beginner"],
    },
    {
        "name": "Spanish Conversation",
        "description": "Practice speaking for travel and everyday use.",
        "tags": ["languages", "travel", "hobby"],
    },
]


def normalize(text: str) -> str:
    """Lowercase and strip for consistent matching."""
    return text.strip().lower()


def parse_interests(raw: str) -> list[str]:
    """Split comma- or space-separated interests into a list."""
    raw = raw.replace(",", " ")
    return [normalize(word) for word in raw.split() if word.strip()]


def score_item(item: dict, interests: list[str]) -> int:
    """
    Score how well an item matches user interests.
    +2 for exact tag match, +1 if interest appears inside a tag.
    """
    score = 0
    tags = [normalize(t) for t in item["tags"]]

    for interest in interests:
        for tag in tags:
            if interest == tag:
                score += 2
            elif interest in tag or tag in interest:
                score += 1
    return score


def recommend(interests: list[str], top_n: int = 5) -> list[tuple[dict, int]]:
    """Return top-N items sorted by match score (highest first)."""
    if not interests:
        return []

    scored = [(item, score_item(item, interests)) for item in ITEMS]
    scored = [(item, s) for item, s in scored if s > 0]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


def display_recommendations(results: list[tuple[dict, int]]) -> None:
    """Print recommended items in a readable format."""
    if not results:
        print("\nNo strong matches found. Try interests like: coding, art, fitness, travel.")
        return

    print("\n--- Your recommendations ---\n")
    for rank, (item, score) in enumerate(results, start=1):
        tags_str = ", ".join(item["tags"])
        print(f"{rank}. {item['name']} (match score: {score})")
        print(f"   {item['description']}")
        print(f"   Tags: {tags_str}\n")


def main() -> None:
    print("=" * 50)
    print("  AI Recommendation System")
    print("=" * 50)
    print("\nTell us what you're interested in.")
    print("Examples: coding, art, fitness, travel, books")
    print("(Separate multiple interests with commas)\n")

    raw = input("Your interests: ")
    interests = parse_interests(raw)

    if not interests:
        print("No interests entered. Exiting.")
        return

    print(f"\nMatching for: {', '.join(interests)}")
    results = recommend(interests)
    display_recommendations(results)


if __name__ == "__main__":
    main()
