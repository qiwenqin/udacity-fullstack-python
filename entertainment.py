import website
import media
# the instance of Movie
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "1994",
                                       "9.3",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                       "https://www.youtube.com/watch?v=9ZDSAzMtbmc&list=PLzC3uEA-hVoy_AhY8IiCwBUUJWD4wavwV")
the_godfather = media.Movie("The Godfather",
                            "1972",
                            "9.2",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=DVQ4BJ94XEk")
scindler_list = media.Movie("Scindler's List",
                            "1993",
                            "8.9",
                            "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=ST5rN8Hjsx0")
forrest_gump = media.Movie("Forrest Gump",
                           "1994",
                           "8.7",
                           "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=QgStze9lTNY")

breaking_bad = media.TvShow("Breaking Bad",
                            "9.4",
                            "5",
                            "62",
                            "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=Xs6_vecSv2Y")
sherlock = media.TvShow("Sherlock",
                        "9.2",
                        "4",
                        "15",
                        "A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMWY3NTljMjEtYzRiMi00NWM2LTkzNjItZTVmZjE0MTdjMjJhL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTQ4NTc5OTU@._V1_.jpg",
                        "https://www.youtube.com/watch?v=qlcWFoNqZHc")
# initialize the page
movies = [the_shawshank_redemption,the_godfather,scindler_list,forrest_gump,breaking_bad,sherlock]
website.open_movies_page(movies)
