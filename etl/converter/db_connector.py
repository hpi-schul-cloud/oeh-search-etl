import psycopg2

class Database:
    conn = None
    curr = None
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        if Database.conn == None:
            Database.conn = psycopg2.connect(
                host = 'localhost',
                user = 'search',
                password = 'admin',
                database = 'search'
            )
            Database.curr = self.conn.cursor()
    def uuidExists(self, uuid):
        Database.curr.execute("""SELECT uuid FROM "references" WHERE uuid = %s""", (
            uuid,
        ))
        data = Database.curr.fetchall()
        return len(data) > 0
    def findItem(self, id, spider):
        Database.curr.execute("""SELECT uuid, hash FROM "references_metadata" WHERE source = %s AND source_id = %s""", (
            spider.name,
            str(id),
        ))
        data = Database.curr.fetchall()
        if(len(data)):
            return data[0]
        else:
            return None
    def findSource(self, spider):
        Database.curr.execute("""SELECT * FROM "sources" WHERE id = %s""", (
            spider.name,
        ))
        data = Database.curr.fetchall()
        if(len(data)):
            return data[0]
        else:
            return None