import psycopg2

from .main import datacon, getAll, insertBet, removeBet

__all__ = ["insertBet", "removeBet", "getAll"]


createTableString = """
                    CREATE TABLE bettingtest (
                        id SERIAL PRIMARY KEY,
                        userid VARCHAR,
                        matchid INT,
                        teamid INT,
                        amount FLOAT
                    );
                    """


def __init__():
    with datacon.cursor() as curs:
        try:
            curs.execute(createTableString)
        except psycopg2.errors.DuplicateTable:
            print("duplicate table encountered")
            pass


__init__()
