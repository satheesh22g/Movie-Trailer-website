import webbrowser

class Movie():
    """this class provides"""
    #valid
    def __init__(self,movie_title,movie_storyline,poster_image,myoutube,review,duration):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=myoutube
        self.review=review
        self.duration=duration
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
