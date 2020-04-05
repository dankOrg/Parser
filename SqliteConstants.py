import os

class SqliteConstants:
    SQLITE_PATH_KEY = "PARSER_SQLITE_PATH"
    SQLITE_DB_PATH = os.environ.get(SQLITE_PATH_KEY) # Gets the path to the database from the environment key defined in `SQLITE_PATH_KEY`
    
