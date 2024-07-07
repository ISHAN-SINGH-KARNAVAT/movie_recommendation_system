import streamlit as st
import pickle
import pandas as pd
import requests
import bz2file as bz2

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=da87c80a65dae508ada18ceead20f933&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarities[movie_index]
    recommend_movie_list = sorted(list(enumerate(distances)),reverse=True, key= (lambda x:x[1]))[1:6]
    
    recommend_movie = []
    recommend_movie_posters  = []
    
    for i in recommend_movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommend_movie.append(movies_list.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    
    return recommend_movie, recommend_movie_posters

movies_list = pickle.load(open('movie.pkl', 'rb'))
movies_title_list = movies_list['title'].values

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

similarities = decompress_pickle('similarities.pbz2')

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Enter the title of your favorite movie to unlock personalized recommendations!",
    (movies_title_list))

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
