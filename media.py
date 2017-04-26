import webbrowser

"""This file includes a data structure (i.e. a Python Class)
to store the selected movies, including movie title, poster URL
and a YouTube link to the movie trailer."""


class Movie ():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title  # instance variables
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
