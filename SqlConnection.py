from SqliteConstants import SqliteConstants
import sqlite3

class SqlConnection:
    _CONNECTION = sqlite3.connect(SqliteConstants.SQLITE_DB_PATH)

    @staticmethod
    def getCursor():
        if SqlConnection._CONNECTION == None:
            _CONNECTION = sqlite3.connect(SqliteConstants.SQLITE_DB_PATH)

        if SqlConnection._CONNECTION != None:
            return SqlConnection._CONNECTION.cursor()

        return None
    
    def executeQuery(self, query):
        cursor = SqlConnection.getCursor()

        return cursor.execute(query)
