import media
import fresh_tomatoes

"""create six movie objects and initialize each with movie title, storyline,
poster image, video trailer URL,release date, and rating"""

a_fish_called_wanda = media.Movie("A Fish Called Wanda",
                        "A jewelry heist goes all wrong",
                        "https://upload.wikimedia.org/wikipedia/en/4/4f/"\
                        "A_Fish_Called_Wanda_DVD.jpg",
                        "https://www.youtube.com/watch?v=dqAJUlSRCwo",
                        "July 15, 1988",
                        "Rated R")

monsters_inc = media.Movie("Monsters, Inc",
                        "Monsters save a little girl from the Scream Factory",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/"\
                        "Monsters_Inc.JPG",
                        "https://www.youtube.com/watch?v=cvOQeozL4S0",
                        "November 2, 2001",
                        "Rated G")

forrest_gump = media.Movie("Forrest Gump",
                        "Forrest Gump recounts his life story",
                        "https://upload.wikimedia.org/wikipedia/sco/6/67/"\
                        "Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0",
                        "July 6, 1994",
                        "Rated PG13")

transformers = media.Movie("Transformers",
                         "Robots bring their war to Earth",
                         "https://upload.wikimedia.org/wikipedia/en/6/66/"\
                         "Transformers07.jpg",
                         "https://www.youtube.com/watch?v=UxI_JI6chas",
                         "July 3, 2007",
                         "Rated PG13")

as_good_as_it_gets = media.Movie("As Good as it Gets",
                         "A dysfunctional writer's world is changed",
                         "https://upload.wikimedia.org/wikipedia/en/d/dc/"\
                         "As_good_as_it_gets.jpg",
                         "https://www.youtube.com/watch?v=rrRl2QQKkI8",
                         "December 6, 1997",
                         "Rated PG13")


maleficent = media.Movie("Maleficent",
                          "A vengeful fairy is driven to curse an infant princess",
                          "https://upload.wikimedia.org/wikipedia/en/5/55/"\
                          "Maleficent_poster.jpg",
                          "https://www.youtube.com/watch?v=_pgmFAOgm5E",
                          "May 28, 2014",
                          "Rated PG")

"""movie object list"""
movies = [a_fish_called_wanda, monsters_inc, forrest_gump, transformers,
          as_good_as_it_gets, maleficent]

"""opens movie trailer web site based on selected movie from movie list"""
fresh_tomatoes.open_movies_page(movies)
