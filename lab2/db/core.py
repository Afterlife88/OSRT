import os
import sqlite3

import utils.queries as queries
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
            print('Database file does not exist. Will create new database')
            self.connect_db()
            self.fill_db()

    @exceptions_handler
    def connect_db(self):
        print('Connecting to database "%s"' % self.db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print('Creating tables that do not exist')
        self.execute(queries.get_create())

    @exceptions_handler
    def fill_db(self):
        print('Filling database with data')
        self.execute(queries.get_insert())

    @exceptions_handler
    def execute(self, queries):
        if not isinstance(queries, list):
            queries = [queries]

        for query in queries:
            print('Executing query:\n%s' % query)
            result = self.cursor.execute(query)

        return result