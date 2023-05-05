# Movie-Recommender

Steps to access and use movie recommender

Step 1: Used the kaggle top 5000 tmdb dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Step 2: "Movie Recommendation.ipynb" file will help to clean, structure and make an machine learning model with which user can get top 5 movie recommendations.
Also, two "pkl" files have been dumped to further being helpful while making a webpage.("similarity.pkl" and "movie_dict.pkl")

Step 3: using "streamlit" a website (named "streamlit_app.py") is being initialized and posters are fetched using api of tmdb.(also using the two files "similarity.pkl" and "movie_dict.pkl") in 

Step 4: using "flask", 'streamlit' and other 'html' files along with a 'database' have been integrated in "appfl.py" and "runn.py".

Step 5: using commands, "streamlit run streamlit_app.py" then, "python appfl.py" website is being hosted on local host(whatever port specified).

Now, user can register, login/logout, give ratings to the movies of their choice and
Also, select a movie to get recommendation for top 5 similar movies.


