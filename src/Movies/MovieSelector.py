### Ricardo Sergio Gómez Cárdenas
### A01235366

## Here I'm using The Single Responsibility Principle (SRP), 
## since the MovieSelector class is only used to query the
## movies database.

import pandas as pd

class MovieSelector:
    def selectorQuery(key, rating=True):
        df = pd.read_csv('data/movie_results.csv', encoding = "ISO-8859-1")
        movies = df[df['preference_key'] == key].sort_values('rating', ascending=(not rating))[:10]
        result = []
        for _, movie in movies.iterrows():
            result.append((movie['movie_title'], movie['year'], movie['rating']))
        return result