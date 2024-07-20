import psycopg2

bettingconn = psycopg2.connect(
    host="db", user="postgres", password="postgres", dbname="retroolympics"
)
bettingconn.autocommit = True
