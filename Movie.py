import numpy as np

class Movie:
    def __init__(self, randomize=True):
        if randomize:
            self.randomize()
        else:
            self.movies_watched = np.zeros(11) #The amount of movies wathced
            self.tastes = np.zeros(11) #There tastes, normalized
            self.months_on_netflix = 0 #How long they have been on netflix
            self.movies_matrix = np.zeros(11) #This will be the altered movies watched list
        self.name = False #Set the name to none
        self.genre_key = { #This makes the genre key that will be used for later
            0: "Action",
            1: "Adventure",
            2: "Comedy",
            3: "Drama",
            4: "Fantasy",
            5: "Horror",
            6: "Mystery",
            7: "Thriller",
            8: "Romance",
            9: "Sci-Fi",
            10: "Western"
        }
        

        #These are some things that can be randomized
        self.movie_decay = 0.98 #How much other movies are decayed as other movies are watched
        self.like_rate = 0.02 #How much a like increases a given category
    
    def randomize(self) -> None:
        u = np.random.randint(0,100,11)
        self.genre_array = u/np.linalg.norm(u)

    def movie_genre(self) -> str:
        indices = np.where(self.genre_array == self.genre_array.max())[0]
        if len(indices) == 1:
            return self.genre_key[indices[0]]
        else:
            genres = self.genre_key[indices[0]]
            indices = indices[1::]
            for indice in indices:
                genres += f", {self.genre_key[indice]}"
            return genres
    
    def set_name(self, name: str) -> None:
        self.name = name

    def __str__(self):
        if self.name:
            return f"{self.name}'s favorite genre is {self.favorite_genre()}."
        else:
            return f"Favorite genre is {self.favorite_genre()}."





#TODO add a decay factor/rate with new shows are watched
#TODO add a function to indicate they have wathced a show

