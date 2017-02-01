import webbrowser
class Video:
    def __init__(self, video_title, video_rating, video_storyline, poster_image, youtube_trailer):
        self.title = video_title
        self.rating = video_rating
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
class Movie(Video):
    def __init__(self, video_title, movie_year, video_rating, video_storyline, poster_image, youtube_trailer):
        Video.__init__(self, video_title, video_rating, video_storyline, poster_image, youtube_trailer)
        self.year = movie_year
class TvShow(Video):
    def __init__(self, video_title, video_rating, show_seasons, show_episodes, video_storyline, poster_image, youtube_trailer):
        Video.__init__(self, video_title, video_rating,  video_storyline,poster_image, youtube_trailer)
        self.seasons = show_seasons
        self.episodes = show_episodes
