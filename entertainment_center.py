from media import Movie
import fresh_tomatoes


#
the_dark_knight = Movie("The Dark Knight",
                       "the Joker appears in Gotham, creating a new wave of chaos.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                       "https://www.youtube.com/watch?v=EXeTwQWrcwY")


lion = Movie("lion",
            "Five year old Saroo gets lost on a train which takes him thousands of miles across India",
            "https://upload.wikimedia.org/wikipedia/en/f/f0/Lion_%282016_film%29.png",
            "https://www.youtube.com/watch?v=9DbLKvpjFQk")


the_light_between_oceans = Movie("The Light Between Oceans",
                                "Tom is a World War I veteran "
                                "who maintains a lighthouse off the shore of Australia with his wife Isabel,",
                                "https://upload.wikimedia.org/wikipedia/en/9/91/The_Light_Between_Oceans_poster.jpg",
                                "https://www.youtube.com/watch?v=lk7yw00a4fs")


me_before_you = Movie("Me Before You",
                     "A girl in a small town forms an unlikely bond with a recently-paralyzed man "
                     "she's taking care of.",
                     "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                     "https://www.youtube.com/watch?v=Eh993__rOxA")

#create list of movies
movies = [the_dark_knight, lion, the_light_between_oceans, me_before_you]
#show movies in a static web page 
fresh_tomatoes.open_movies_page(movies)
