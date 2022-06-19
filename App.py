### Ricardo Sergio Gómez Cárdenas
### A01235366

from src.User.User import UserData
import src.Movies.Movie_Fetcher as mf
from src.Movies.MovieSelector import MovieSelector

def printMovies(movies):
    for movie in movies:
        print('Title: ', movie[0], end='\t')
        print('Year: ', movie[1], end='\t')
        print('Rating: ', movie[2])
        print('')

def main():
    mf.fetch_movies()

    option_selected = 0
    
    while option_selected not in (1, 2):
        print('''Menu:
            1. Register
            2. Login''')
        option_selected = int(input('Option: '))
    
    user = UserData(option_selected)
    
    while user.username == "":
        print('''Menu:
            1. Register
            2. Login''')
        option_selected = int(input('Option: '))
    
        user = UserData(option_selected)

    option_selected = 0

    while option_selected not in (1, 2):
        print('''Menu:
            1. Query
            2. Exit''')
        option_selected = int(input('Option: '))
    
    if option_selected == 1:
        option_selected = 0
        while option_selected not in (1, 2):
            print('''Rating:
            1. Ascending
            2. Descending''')
            option_selected = int(input('Option: '))

            movies = MovieSelector.selectorQuery(user.preferences_key, (option_selected == 2))

            print(user.preferences_key, movies)

            printMovies(movies)
    
    print('Closing...')

if __name__ == '__main__':
    main()