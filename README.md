# 🍳 Recipe Generator – ML & NLP Powered

An intelligent and user-friendly system that suggests recipes based on the ingredients you have on hand. This project leverages machine learning and natural language processing to help users minimize food waste and explore new meal ideas.

---

## 📖 Table of Contents

* [About the Project](#-about-the-project)
* [Key Features](#-key-features)
* [How It Works](#️-how-it-works)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Project Structure](#-project-structure)
* [Future Enhancements](#-future-enhancements)
* [Acknowledgments](#-acknowledgments)

---

## 💡 About the Project

[cite_start]In a world where online recipes are abundant but often require specific ingredients, this Recipe Generator aims to bridge the gap between digital culinary data and real-world kitchen limitations. [cite: 58]

[cite_start]The system takes user input in the form of available ingredients and dynamically recommends dishes that can be prepared with those items. [cite: 49]

[cite_start]This project was developed by **Bharath JR, Darshan L, Monik, and Rithish** as a part of their **B.Tech CSE AIML** program at **Rai Technology University** for their Machine Learning subject. [cite: 5, 6, 7, 8, 9, 10, 16]

---

## ✨ Key Features

[cite_start]**Interactive Ingredient Matching:** The system dynamically asks for ingredients a user has and recommends recipes based on them. [cite: 49, 73]

[cite_start]**Intelligent Suggestions:** It computes a matching score for each recipe, prioritizing those with the highest ingredient overlap. [cite: 52]

[cite_start]**Fuzzy Matching:** It can handle variations in ingredient names and typos through techniques like fuzzy matching. [cite: 51, 275]

[cite_start]**Detailed Recipe Information:** Output includes recipe name, cuisine type, rating, ingredients, and step-by-step directions. [cite: 53]

[cite_start]**Resource Efficiency:** Helps minimize food waste by encouraging users to utilize ingredients they already have. [cite: 74, 85]

[cite_start]**Extensible Design:** Built to integrate into web apps or voice-based assistants. [cite: 56]

---

## ⚙️ How It Works

The system follows a simple, yet effective methodology:

[cite_start]**Dataset Collection:** A recipe dataset is loaded, containing information like recipe names, ingredients, directions, and ratings. [cite: 48, 110, 70]

[cite_start]**Data Preprocessing:** Clean null values, standardize ingredient names, and tokenize ingredient lists for comparison. [cite: 50, 114, 115, 116]

**Ingredient Matching:** Compare the user's ingredients against the recipe dataset.

[cite_start]**Ranking:** Identify and rank recipes by the number/quality of matched ingredients. [cite: 51, 52]

[cite_start]**Display:** Show the top-ranked recipes with details and step-by-step instructions. [cite: 53, 171]

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* `pandas`
* `scikit-learn` (optional, for advanced similarity measures)
* `nltk` or `re` (for text cleaning)
* `fuzzywuzzy` or `difflib` (for fuzzy matching)

Install dependencies:

```bash
pip install pandas scikit-learn nltk python-Levenshtein fuzzywuzzy
```

### Quick Start

```bash
# 1) Clone your repository
git clone https://github.com/your-username/recipe-generator.git
cd recipe-generator

# 2) (Optional) Create a virtualenv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 3) Install requirements
pip install -r requirements.txt  # or use the pip line above

# 4) Run the app (CLI example)
python app.py --ingredients "tomato, onion, pasta, cheese"
```

---

## 🧑‍🍳 Usage

**CLI Example:**

```bash
python app.py --ingredients "egg, milk, bread, butter"
```

**Sample Output:**

```
Top Matches (k=5)
1) French Toast  ⭐ 4.6/5  | Cuisine: American  | Match: 4/5
   Ingredients: bread, egg, milk, sugar, butter
   Steps:
   - Whisk eggs and milk
   - Soak bread
   - Pan-fry with butter
   - Serve warm
```



## 🔮 Future Enhancements

* Nutritional filters (calories, macros, allergens)
* Substitution suggestions (e.g., yogurt ↔ curd)
* Pantry tracking & expiry reminders
* Multi-language support
* Personalized ranking (learn from user likes/saves)
* Image-based ingredient recognition

---

## 🙏 Acknowledgments

* Dataset providers & open-source contributors
* Faculty mentors at **Rai Technology University**
* Team: **Bharath JR, Darshan L, Monik, Rithish**

---

