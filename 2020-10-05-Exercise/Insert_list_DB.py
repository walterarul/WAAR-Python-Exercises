import sqlite3

class access_db:

    def __init__(self,dbname):
        self.dbname = dbname

    def get_connection(self):
        conn = sqlite3.connect(self.dbname)
        print("Connection open")
        return conn

    def create_table(self,conn,tbl_nm):
        conn.execute('''CREATE TABLE IF NOT EXISTS '''+tbl_nm+'''(Name,Age,Sex)''')
        print("Table Created with name :",tbl_nm)

    def insert_record(self,conn,tbl_nm,obj):
        query = '''INSERT INTO ''' +tbl_nm+'''(Name,Age,Sex) VALUES (?,?,?)'''
        conn.executemany(query,obj)
        conn.commit()

    def select_record(self,conn,tbl_nm):
        data = conn.execute('''SELECT * FROM '''+tbl_nm)
        return data

    def close_connection(self,conn):
        conn.close()
        print("Connection closed")

if __name__ == "__main__":
    frnd = access_db('database.db')
    conn = frnd.get_connection()
    frnd.create_table(conn,'my_friends')
    friends_list = [("Saravanan",44,"M"),("Sangeetha",40,"F"),("Amarnath",42,"M"),("Durga",40,"F")]
    frnd.insert_record(conn,'my_friends',friends_list)
    data = frnd.select_record(conn,'my_friends')
    for idx in data:
        print("Record from table :",idx)
    frnd.close_connection(conn)
