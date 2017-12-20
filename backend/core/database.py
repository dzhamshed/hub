import psycopg2


class Preferences:
    def __init__(self, id=None, preferences=None):
        self.id = id
        self.preferences = preferences

    def __str__(self):
        return str(self.preferences)

    def __repr__(self):
        return str(self.preferences)


pg = None

try:
    pg = psycopg2.connect("dbname='hub' user='postgres' password='postgres' host='localhost'")

    cursor = pg.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
          id SERIAL PRIMARY KEY,
          preferences JSON
        );
    """)
    pg.commit()
    cursor.close()

except Exception as e:
    print("Couldn't connect to pg database", e)
