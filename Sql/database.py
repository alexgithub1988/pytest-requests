import sqlite3
from sqlite3 import Error
import os

class Database:
    def __init__(self,path_to_db):
        '''Take path to db'''
        self.path_to_db = path_to_db
        self.connection =  None
        os.makedirs(os.path.dirname(path_to_db,exist_ok = True))
