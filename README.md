# 🎬 Movie Recommendation System

## 📌 Project Overview
This project implements a **content-based movie recommender system** using the TMDB 5000 Movies dataset. It analyzes features like genres, keywords, cast, and crew to generate similarity scores between movies. Based on a given movie title, the system suggests other similar movies.

## 🚀 Features
- Content-based filtering using movie metadata  
- Text vectorization with **CountVectorizer**  
- **Porter Stemming** for better NLP preprocessing  
- Cosine similarity for movie recommendations  
- Model export using pickle (`movies.pkl`, `similarity.pkl`)  

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLTK  

## 📂 Usage
1. Run the Jupyter Notebook.  
2. Enter a movie title (e.g., `Batman Begins`) in the `recommend()` function.  
3. Get top recommended movies.  

