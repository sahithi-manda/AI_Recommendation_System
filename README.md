# 🤖 AI Recommendation System

A simple AI-based Recommendation System built using Python.  
This project recommends courses, activities, and learning resources based on user interests using basic recommendation logic.

---

# 📌 Project Overview

This project demonstrates how recommendation systems work in Artificial Intelligence.  
The system takes user interests as input, compares them with predefined item tags, calculates matching scores, and displays the best recommendations.

It is a beginner-friendly project that helps in understanding the core logic behind recommendation engines used in platforms like Netflix, YouTube, Amazon, and Spotify.

---

# 🎯 Features

- User interest-based recommendations
- Tag matching system
- Recommendation scoring logic
- Clean and beginner-friendly Python code
- Console-based interaction
- Simple AI recommendation workflow

---

# 🛠️ Technologies Used

- Python
- Artificial Intelligence Basics
- Recommendation Logic
- Lists & Dictionaries
- Functions and Loops

---

# 📂 Project Structure

```bash
AI-Recommendation-System/
│
├── README.md
└── recommendation.py
```

---

# ⚙️ How the System Works

1. A catalog of items is stored with:
   - Name
   - Description
   - Tags

2. User enters their interests.

3. The system:
   - Cleans the input
   - Matches interests with item tags
   - Calculates scores
   - Sorts recommendations

4. Top matching recommendations are displayed.

---

# 🧠 AI Logic Used

The recommendation engine uses a simple scoring mechanism:

- `+2 points` for exact tag matches
- `+1 point` for partial matches

Example:

```python
if interest == tag:
    score += 2
elif interest in tag or tag in interest:
    score += 1
```

---

# 📊 Sample Input

```bash
Your interests: coding, ai
```

# ✅ Sample Output

```bash
--- Your recommendations ---

1. Intro to Machine Learning (match score: 4)
   Concepts and small projects with scikit-learn.

2. Python Crash Course (match score: 2)
   Hands-on intro to Python programming.

3. The Pragmatic Programmer (match score: 2)
   Classic guide to becoming a better developer.
```

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Recommendation-System.git
```

---

## 2️⃣ Open the Project Folder

```bash
cd AI-Recommendation-System
```

---

## 3️⃣ Run the Python File

```bash
python main.py
```

---

# 📚 Concepts Covered

- Artificial Intelligence Basics
- Recommendation Systems
- Python Functions
- Data Matching
- Scoring Algorithms
- User Input Handling

---

# 🔮 Future Improvements

- Add Machine Learning-based recommendations
- Create a Streamlit web app
- Add database support
- User login system
- Personalized recommendation history
- GUI interface

---

# 📈 Learning Outcome

After completing this project, you will understand:

- How recommendation systems work
- Basic AI recommendation logic
- How user preferences are processed
- How scoring-based systems are designed
- Real-world applications of AI recommendation engines

---

# 👩‍💻 Author

**Sahithi Manda**  
B.Tech CSE (AIML)  
Aspiring AI/ML Engineer

---

# ⭐ Conclusion

This project is a simple implementation of an AI Recommendation System using Python. It provides a strong foundation for understanding how recommendation engines work and serves as a beginner-friendly introduction to Artificial Intelligence concepts.
