### Ricardo Sergio Gómez Cárdenas
### A01235366

## Here I'm using The Single Responsibility Principle (SRP), 
## since the UserData class is only used to store the user information
## and also I using the Facade desgin pattern.

import pandas as pd
from src.User.UserValidator import validateUser

class Registration:
    def registerUser():
        username = input('Username: ')
        email = input('Email: ')
        return username, email

## On the Preferences class I'm considering the Open Closed Principle
## (OPS), because if we add more categories and users have to select
## more than 3 which is the actual requirement it is easy to update
## the new preferences quantity selection, since it is a parameter,
## and also we can update easily the preferences key calculation.

class Preferences:
    def selectPreferences(selecction_qty):
        preferences = []
        for selecction_n in range(selecction_qty):
            preferences.append(int(input(f'Preference {selecction_n}: ')))
        return preferences
        
    def calculatePreferenceKey(preferences):
        preferences_key = 1
        for preference in preferences:
            preferences_key *= preference
        preferences_key = preferences_key % 5 + 1
        return preferences_key

class UserData:
    username = ""
    email = ""
    preferences = []
    preferences_key = 0
    
    def __init__(self, option):
        if option == 1:
            self.username, self.email = Registration.registerUser()
            self.preferences = Preferences.selectPreferences(3)
            self.preferences_key = Preferences.calculatePreferenceKey(self.preferences)
            self.saveUserData()
            print('User succesfully registered.')
        else:
            username = input('Entrer your username: ')
            self.username, self.email, self.preferences, self.preferences_key = validateUser(username)
        
    def saveUserData(self):
        try:
            users = pd.read_csv('data/users-db.csv')
            users = users.append({'username': self.username, 
                          'email': self.email, 
                          'preferences': self.preferences, 
                          'preferences_key': self.preferences_key}, 
                         ignore_index=True)
        except:
            users = pd.DataFrame(columns=['username', 'email', 'preferences', 'preferences_key'])
            users = users.append({'username': self.username, 
                          'email': self.email, 
                          'preferences': self.preferences, 
                          'preferences_key': self.preferences_key}, 
                         ignore_index=True)
        finally:
            users.to_csv('data/users-db.csv', index=False)