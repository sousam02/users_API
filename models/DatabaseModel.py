import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="registrations",
            user="root",
            password="root"
        )

    def query(self, query, params=None, fetchall=False):
        with self.conn.cursor() as cur:
            cur.execute(query, params)

            if fetchall:
                result = cur.fetchall()
            else:
                result = cur.fetchone()
        self.conn.commit()
            
        return result

    def execute(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
        self.conn.commit()
    
    def close(self):
        self.conn.close()




