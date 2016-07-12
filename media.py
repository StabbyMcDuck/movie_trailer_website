import webbrowser

class Movie():
    # Initializes class Movie taking in 5 arguments
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens a webbrowser to show a youtube video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
