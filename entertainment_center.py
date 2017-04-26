import fresh_tomatoes
import media

"""The file entertainment_center.py contains instances of that Python Class to
represent selected movies; and groups all the instances together in a list."""

fifty_shades_darker = media.Movie(
    "Fifty Shades Darker",
    "A story of a boy and his toys that come to life",
    "https://goo.gl/Qc8gxX",
    "https://youtu.be/n6BVyk7hty8")

john_wick = media.Movie(
    "John Wick",
    "Legendary hitman John Wick has a bounty on his head",
    "https://goo.gl/YNlvkX",
    "https://youtu.be/XGk2EfbD_Ps")

great_wall = media.Movie(
    "Great Wall",
    "A mercenary making a stand for humanity",
    "https://goo.gl/VxgjcD",
    "https://youtu.be/LVw9YdP1O-0")

rings = media.Movie(
    "Rings",
    "Rings is american supernatural psychological horror",
    "https://goo.gl/4OITiL",
    "https://youtu.be/NFB4eZSVgBE")

arrival = media.Movie(
    "Arrival",
    "A story of an aliens communicating with us",
    "https://goo.gl/wLmAUR",
    "https://youtu.be/ZLO4X6UI8OY")

moonlight = media.Movie(
    "Moonlight", "A timeless story of human self-discovery and connection",
    "https://goo.gl/5epBjP",
    "https://youtu.be/9NJj12tJzqc")

"""the open_movies_page() function takes in the list of movies and
generates an HTML file including that content, producing a website to
showcasing selected movies."""

movies = [fifty_shades_darker, john_wick,
          great_wall, rings, arrival, moonlight]
fresh_tomatoes.open_movies_page(movies)
