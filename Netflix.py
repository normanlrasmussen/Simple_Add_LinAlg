from Person import Person
from Movie import Movie
import pandas as pd

class Netflix:
    def __init__(self):
        self.movies = []
        self.subs = []

    def random_subs(self, quantity: int):
        self.subs = []
        names = pd.read_csv("random_names.csv")

        if quantity > 10000:
            raise ValueError("Not enough random names to use. Use number >+ 10000")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be integer")
        
        for i in range(quantity):
            person = Person(name=names.iloc[i, 0] + " " + names.iloc[i, 1])
            self.subs.append(person)

    def random_movies(self, quantity: int):
        self.movies = []
        movies = pd.read_csv("random_movies.csv")

        if quantity > 10000:
            raise ValueError("Not enough random movies to use. Use number >+ 10000")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be integer")
        
        for i in range(quantity):
            movie = Movie(name=movies.iloc[i, 0])
            self.movies.append(movie)


#TODO Find people that like a certain genre
#TODO Find movies of a certain genre
#TODO Make a function to check which people will like a certain movie given a certain tolerence

"""Yeah thats about it"""
            