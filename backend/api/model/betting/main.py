import psycopg2
import api.model.database as data

datacon = data.bettingconn
datacon.autocommit=True

def insertBet(userid, matchid, teamid, amount):
    with datacon.cursor() as curs:
        curs.execute(f"""INSERT INTO bettingtest (userid, matchid, teamid, amount)
                    VALUES ({userid},{matchid},{teamid},{amount});""")
    
def getAll():
    with datacon.cursor() as curs:
        curs.execute("""
                    SELECT * FROM bettingtest;
                    """)
        res = curs.fetchall()
    return res

def removeBet():
    pass
