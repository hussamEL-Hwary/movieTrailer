import webbrowser


class Movie():
    """class Movie contains basic information about movie that
    will be showed in a web page

    Attributes:
        title: A string contains movie title.
        story: A string describes breaflly movie story.
        poster_image_url: A string contains poster image url.
        trailer_youtube_ulr: A string contains youtube trailer url.

    """
    def __init__(self, title, story, poster_image_url, trailer_url):
        """Inits movie class"""
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url

    def open_trailer(self):
        """open the movie trailer url"""
        webbrowser.open(self.trailer_url)
