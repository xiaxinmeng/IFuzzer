
from collections import namedtuple
from operator import attrgetter
from bisect import bisect

Movie = namedtuple('Movie', ('name', 'released', 'director'))

movies = [
    Movie('Jaws', 1975, 'Speilberg'),
    Movie('Titanic', 1997, 'Cameron'),
    Movie('The Birds', 1963, 'Hitchcock'),
    Movie('Aliens', 1986, 'Scott')
]

# Find the first movie released on or after 1960
by_year = attrgetter('released') 
movies.sort(key=by_year)
print(movies[bisect(movies, 1960, key=by_year)])
