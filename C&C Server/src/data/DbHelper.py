import sqlite3

class DbHelper:

    __connection = None;
    __cursor = None;

    def __init__(self):
        self.__connection = sqlite3.connect('survey6.db')
        self.__cursor = self.__connection.cursor()
        
    def __del__(self):
        self.close()

    def query(self, query, params):
        res = None
        with self.__connection:
            res = self.__cursor.execute(query, params)
        return res


    def close(self):
        self.__connection.close();
        