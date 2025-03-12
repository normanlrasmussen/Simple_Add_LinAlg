import numpy as np

class Movie:
    def __init__(self, randomize=True, name=None):
        if randomize:
            self.randomize()
        else:
            self.genre_array = np.zeros(11) #This sets the genre of the movie to be edited later

        self.name = name #Set the name to none

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
            return f"{self.name} is {self.movie_genre()}."
        else:
            return f"This movie is {self.movie_genre()}."
