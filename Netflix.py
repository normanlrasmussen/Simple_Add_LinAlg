from Person import Person
from Movie import Movie
import pandas as pd
import numpy as np

class Netflix:
    def __init__(self):
        self.movies = []
        self.subs = []
        self.movies_matrix = None
        self.subs_matrix = None

    def random_subs(self, quantity: int):
        self.subs = []
        names = pd.read_csv("random_names.csv")

        if quantity > 10000:
            raise ValueError("Not enough random names to use. Use number >+ 10000")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be integer")
        
        
        person = Person(name=names.iloc[0, 0] + " " + names.iloc[i, 1])
        self.subs.append(person)
        self.subs_matrix = person.tastes
        for i in range(1, quantity):
            person = Person(name=names.iloc[i, 0] + " " + names.iloc[i, 1])
            self.subs.append(person)
            self.subs_matrix = np.vstack((self.subs_matrix, person.tastes))

    def random_movies(self, quantity: int):
        self.movies = []
        movies = pd.read_csv("random_movies.csv")

        if quantity > 10000:
            raise ValueError("Not enough random movies to use. Use number >+ 10000")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be integer")
        
        movie = Movie(name=movies.iloc[0, 0])
        self.movies.append(movie)
        self.movies_matrix = movie.genre_array
        for i in range(1, quantity):
            movie = Movie(name=movies.iloc[i, 0])
            self.movies.append(movie)
            self.movies_matrix = np.vstack((self.movies_matrix, movie.genre_array))


#TODO Find people that like a certain genre
#TODO Find movies of a certain genre
#TODO Make a function to check which people will like a certain movie given a certain tolerence

"""Yeah thats about it"""
            