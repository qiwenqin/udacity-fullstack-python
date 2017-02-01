import webbrowser
# build a parent class
class Video:
    # constructor of class Video
    def __init__(self, video_title, video_rating, video_storyline, poster_image, youtube_trailer):
        # instance variavles of parent class Video
        self.title = video_title
        self.rating = video_rating
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    # instance method of class Video
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
# build child class Movie
class Movie(Video):
    def __init__(self, video_title, movie_year, video_rating, video_storyline, poster_image, youtube_trailer):
        # make to inheritant from parent class
        Video.__init__(self, video_title, video_rating, video_storyline, poster_image, youtube_trailer)
        self.year = movie_year
# build child class TvShow
class TvShow(Video):
    def __init__(self, video_title, video_rating, show_seasons, show_episodes, video_storyline, poster_image, youtube_trailer):
        Video.__init__(self, video_title, video_rating,  video_storyline,poster_image, youtube_trailer)
        self.seasons = show_seasons
        self.episodes = show_episodes
