import os
import sqlite3

import utils.create as create
from utils.decorators.exceptions_handler import exceptions_handler
from utils.singleton import Singleton

class Db:
    __metaclass__ = Singleton

    @exceptions_handler
    def __init__(self, db_name='mvd.db'):
        print('Initialized Database object')
        self.conn = None
        self.cursor = None

        self.db_name = db_name

    @exceptions_handler
    def connect(self):
        if os.path.isfile(self.db_name):
            print('Database file already exists')
            self.connect_db()
        else:
            print('Database file does not exist. Creating new database')
            self.create()

    @exceptions_handler
    def connect_db(self):
        print('Connecting to database "%s"' % self.db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    @exceptions_handler
    def create(self):
        self.connect_db()
        print('Creating database "%s"' % self.db_name)
        self.execute(create.get_command())

    @exceptions_handler
    def execute(self, query):
        print('Executing query:\n%s' % query)
        return self.cursor.execute(query)