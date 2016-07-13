import fresh_tomatoes
import media

# Movies to include in 'movies'
casper = media.Movie("Casper", 
		     "A ghost finds a friend.",
		     "http://firetheimagination.ca/images/productImages/orig/casper_movie.jpg",  # NOQA
		     "https://youtu.be/e8RATQJIngU")

black_swan = media.Movie("Black Swan", 
			 "A ballerina loses her grip on reality",
			 "http://www.filmofilia.com/wp-content/uploads/2010/08/blackswan_poster-535x793.jpg",  # NOQA
			 "https://youtu.be/5jaI1XOB-bs")

groundhog_day = media.Movie("Groundhog Day",
			    "It's always Grondhog Day for Phil...",
			    "http://ia.media-imdb.com/images/M/MV5BMTU0MzQyNTExMV5BMl5BanBnXkFtZTgwMjA0Njk1MDE@._V1_UY1200_CR87,0,630,1200_AL_.jpg",  # NOQA
			    "https://youtu.be/tSVeDx9fk60")

the_shining = media.Movie("The Shining",
			  "A family spends a winter in a remote hotel",
			  "http://t0.gstatic.com/images?q=tbn:ANd9GcSurv36gKqz9FhNhK8-ziym4RxX5bbVwvk_V-u_TvdI4T-omHXt",  # NOQA
			  "https://youtu.be/5Cb3ik6zP2I")

back_to_the_future = media.Movie("Back To The Future",
				"He was never on time until he wasn't in his time at all!",
				"http://t3.gstatic.com/images?q=tbn:ANd9GcT9d_lBBx0xxB7_d4RP82MlRcK82lzT2W1ZavxhV39SSTZOofDX",  # NOQA
				"https://youtu.be/qvsgGtivCgs")

slc_punk = media.Movie( "SLC Punk",
			"Punk kids in SLC learn life lessons",
			"http://t2.gstatic.com/images?q=tbn:ANd9GcRn-gOtXYVCYWGESgDnzkRpIvBbeI8kwGKBXYKJ49bVgm_yNHE7",  # NOQA
			"https://youtu.be/DILdeHgWF-U")

big_lebowski = media.Movie("The Big Lebowski",
			   "You got the wrong Lebowski!",
			   "http://t3.gstatic.com/images?q=tbn:ANd9GcRBYp315X-0pNvI-Dvqj8FR0AGdF39VCprXpurd0cQel__e17CP",  # NOQA
			   "https://youtu.be/cd-go0oBF4Y")

super_troopers = media.Movie("Super Troopers",
			     "Cops in Vermont prank and solve crimes",
			     "http://t0.gstatic.com/images?q=tbn:ANd9GcS5B3MYcNqFg4jd0Z-H8z-vYmFYhWWJCCI-GHem3OVcdO-F-1JG",  # NOQA
			     "https://youtu.be/2-9D2qUHN-E")

the_hobbit = media.Movie("The Hobbit",
			 "A hobbit goes on an adventure...",
			 "http://static2.hypable.com/wp-content/uploads/2012/09/New-Hobbit-Poster.jpg",  # NOQA
			 "https://youtu.be/SDnYMbYB-nU")

# list all the movies from the instances above
movies = [casper, black_swan, groundhog_day, the_shining, back_to_the_future,
		  slc_punk, big_lebowski, super_troopers, the_hobbit]

# send the movies list to fresh_tomatoes.py, which makes the webpage
fresh_tomatoes.open_movies_page(movies)
