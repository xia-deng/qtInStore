import sqlite3


class Sql(object):
    def connect(self):
        return sqlite3.connect("inStore")

    def __init__(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE TOKEN
           (ID INT PRIMARY KEY     NOT NULL,
           token          TEXT    NOT NULL,
           expire         BIGINT       NOT NULL);''')

            print("created orc token table...")
            conn.commit()
        except Exception as e:
            print("init tables failed:%s" % e)
            return
        finally:
            conn.close()

    def insert(self, sql):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            result=cursor.execute(sql)
            conn.commit()
            print("insert data sql:%s successfully:%s" % (sql,result))
        except Exception as e:
            print("insert data sql:%s failed:%s" % (sql, e))
        finally:
            conn.close()

    def search(self, sql):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            result=cursor.execute(sql)
            print("search sql:%s data successfully:%s" % (sql, result))
            return result
        except Exception as e:
            print("search data sql:%s failed:%s" % (sql, e))
        finally:
            conn.close()

    def update(self, sql):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            result=cursor.execute(sql)
            conn.commit()
            print("update sql:%s data successfully:%s" % (sql, result))
            return result
        except Exception as e:
            print("update data sql:%s failed:%s" % (sql, e))
        finally:
            conn.close()


#print(Sql().search("SELECT * from TOKEN").rowcount)