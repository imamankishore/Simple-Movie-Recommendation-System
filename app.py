import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    # find movie index
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # get top 7 similar movies (excluding the same movie itself)
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies = []
    for i in similar_movies:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load data
movies = pickle.load(open('movies.pkl', 'rb'))   # keep dataframe form
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

# UI
selected_movie_name = st.selectbox(
    'Select the Movie Below',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
