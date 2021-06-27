import sqlite3
from functools import wraps


# ========= connect
def connect_db(func):
    """Is a decorator, used to create a connection to the database.
    :param func: function to be decorated
    :return: wrapped function
    """
    @wraps(func)
    def wrapper(directory, db_name, sql):
        try:
            with sqlite3.connect(directory + db_name + '.db') as db_connect:
                func(directory, db_name, sql, db_connect)
        except sqlite3.Error as error:
            print(error)
    return wrapper


# ========= create
@connect_db
def create_table(directory, db_name, sql, db_connect):
    """Creates tables in the database.
    Function must be used with a decorator.
    :param directory: path where the database is located
    :param db_name: name of the database where you want to create the table
    :param sql: sql code to create table
    :param db_connect: database connection object, it will be retrieved in the decorator
    """
    db_cursor = db_connect.cursor()
    db_cursor.execute(sql)
    db_connect.commit()

