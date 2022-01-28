import psycopg2
import hidden

# Grab all of our super secret stuff.
secrets = hidden.secrets()
# Pass our secrets to our conn.
conn = psycopg2.connect(host=secrets['host'],port=secrets['port'], connect_timeout=5,
        database=secrets['database'], user=secrets['user'], password=secrets['pass'])
cur = conn.cursor() # Create our cursor.

# Copies schema from one table to another.
sql = '''
Select * Into test From messages Where 1 = 2
'''

cur.execute(sql)

conn.commit()
cur.close()
