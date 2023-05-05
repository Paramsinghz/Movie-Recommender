import streamlit as st
import pickle
import pandas as pd
import requests


def run():
#fetch poster for movie using api
    def fetch_poster(movie_id):
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4489e9394a3791826d659137c6c3b62f&language=en-US'.format(movie_id))
        data = response.json()
        # print(data)
        return "https://image.tmdb.org/t/p/original" + data['poster_path']

    #making recommend function similar to previous

    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        #used pickle dump for similarity matrix/vector
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies =[]
        recommend_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)

            #fetch poster from api
            recommend_movies_poster.append(fetch_poster(movie_id))
        return recommend_movies,recommend_movies_poster


    #importing dict
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

    #importing similarity matrix/vector
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    #making data frame
    movies = pd.DataFrame(movies_dict)


    st.title('Movie Recommender')

    #dropdown search
    selected_movie_name = st.selectbox(
        'Select Your Favourite movie!',
    movies['title'].values
    )

    #button
    if st.button('Recommend'):
        #creting a recommend function
        names,posters = recommend(selected_movie_name)
        # for i in recommendations:
        #     st.write(i)


        col1, col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])


if __name__ == "__main__":
    run()