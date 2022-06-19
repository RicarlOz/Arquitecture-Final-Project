### Ricardo Sergio Gómez Cárdenas
### A01235366

## Here I'm using The Dependency Inversion Principle (DIP), in
## python I can't use interfaces so insted I used a class to
## declare the function only used to validate that user is registered.

import pandas as pd

def validateUser(username):
    try:
        users = pd.read_csv('data/users-db.csv')
        user = users[users['username'] == username].iloc[0]
        return user.username, user.email, user.preferences, user.preferences_key
    except:
        print('User not found.')
        return "", "", [], 0