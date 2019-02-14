import media
import fresh_tomatoes

#Create a movie object for What We Do
what_we_do = media.Movie("What We Do in the Shadows",
						 "A pack of New Zealand vampires gains a member, who doesn't quite "
						 +"know how vampire life works.",
						 "https://upload.wikimedia.org/wikipedia/en/7/70/What_We_Do_in_the_Shadows_poster.jpg", #NOQA
						 "https://www.youtube.com/watch?v=IAZEWtyhpes")

#Create a movie object for Warcraft
warcraft = media.Movie("Warcraft",
					   "A brutish race of orcs, their world corrupted by fel magic, "
					   +"invade Azeroth, the land of humans.",
					   "http://www.joblo.com/posters/images/full/warcraft-rbposter-gallery.jpg",
					   "https://www.youtube.com/watch?v=65AjY_nRdqE")

#Create a movie object for UHF
uhf = media.Movie("UHF",
				  "To save a television channel from being bought by a mogel, an inexperienced "
				  +"jokester must quickly learn how to create engaging television content.",
				  "http://www.impawards.com/1989/posters/uhf_ver1.jpg",
				  "https://www.youtube.com/watch?v=bRUx0I9xjTw")

#Create a movie object for Spaceballs
spaceballs = media.Movie("Spaceballs",
						 "A hilarious spoof of Star Trek, Star Wars and any other space franchise "
						 +"you can think of.",
						 "https://www.movieposter.com/posters/archive/main/38/MPW-19404",
						 "https://www.youtube.com/watch?v=uWVSVgU-I0s")

#Create a movie object for Labyrinth
labyrinth = media.Movie("Labyrinth",
						"A young girl must travel through a large labyrinth to save her baby brother "
						+"from the Goblin King.",
						"http://www.impawards.com/1986/posters/labyrinth_ver1.jpg",
						"https://www.youtube.com/watch?v=XRcOZZDvMv4")

#Create a movie object for Holy Grail
holy_grail = media.Movie("Monty Python and the Holy Grail",
						 "King Arthur gathers his knights and searches the lands for the holy grail.",
						 "http://img.moviepostershop.com/monty-python-and-the-holy-grail-movie-poster-1975-1010465240.jpg", #NOQA
						 "https://www.youtube.com/watch?v=LG1PlkURjxE")

#Create a list of movie objects
movies = [holy_grail, labyrinth, spaceballs, uhf, warcraft, what_we_do]
#Pass the list of movie objects to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)