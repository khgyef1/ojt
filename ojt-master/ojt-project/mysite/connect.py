import psycopg2

try:
    conn = psycopg2.connect(host='localhost', dbname='ojtproject', user='fphug', password='fphug', port='5432')
    print("connected to the database.")
except:
    print("unable to connect to the database")
