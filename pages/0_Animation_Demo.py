import streamlit as st
import webbrowser
import imdb

# Create an IMDb object
ia = imdb.IMDb()

# Function to search for a movie
def search_movie(title):
    movies = ia.search_movie(title)
    return movies

st.set_page_config(page_title="NIPSFLIX")
st.markdown("<h1 style='text-align: center; color: red;'>NIPSFLIX</h1>", unsafe_allow_html=True)


# Input for movie title
movie_title = st.text_input("Enter the name of the movie:")
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

def callback():
    st.session_state['button_clicked'] = True


# Button to search for movie
if (st.button("Search", on_click=callback) or st.session_state['button_clicked']):
    if movie_title:
        st.write("Searching for:", movie_title)
        movies = search_movie(movie_title)
        if movies:
            st.write("Found", len(movies), "movies:")
        else:
            st.write("No movies found with that title.")

        # Option to watch a movie
        option = st.selectbox("Select a movie to watch:", [movie["title"] for movie in movies])
        if st.button("Watch"):
            selection_idx = [movie["title"] for movie in movies].index(option)
            movie_id = ia.get_imdbID(movies[selection_idx])
            webbrowser.open("https://vidsrc.to/embed/movie/tt" + movie_id)

