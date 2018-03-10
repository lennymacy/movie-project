import webbrowser


class Movie():
    """ This class provides a way to store movie related information """


    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, movie_release_date, movie_rating):
        """Initialize all variables for class movie """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.rating = movie_rating

    def show_trailer(self):
        """ opens a webbrowser to show the movie trailer """
        webbrowser.open(self.trailer_youtube_url)
