import streamlit as st
import pickle
import requests


# def fetch_poster(movies_id):
#     response = requests.get(https://api.themoviedb.org/3/movie/{movies_id}?api_key=69a8ce9b8c61269e602e83ec837b06b8&language=en-US)
#     data= response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_poster(movies_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movies_id}?api_key=69a8ce9b8c61269e602e83ec837b06b8&language=en-US"
        )
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except Exception as e:
        # Return a placeholder image if the API call fails
        return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_name = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_name, recommended_movies_poster

st.header("Movie Recommender System Using Machine Learning")

movies = pickle.load(open('artificates\movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificates\similarity.pkl', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie to get recommendation", movie_list)




if st.button('show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])