from mysql.connector import (connection)
import datetime
import configparser




class MakeConnection:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
        #     self.name = name    # instance variable unique to each instance
        self.muser = muser
        self.mpwd = mpwd
        self.mhost = mhost
        self.mport = mport
        self.mfile = mfile


    def create_connection(self):
        try:
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport, database=self.mfile)
            cursor = conn.cursor()
            print("connected")
            return conn
        except Exception as e:
            print("no connection")
            return e

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.muser = config['DEFAULT']['muser']
        self.mpwd = config['DEFAULT']['mpwd']
        self.mhost = config['DEFAULT']['mhost']
        self.mport = config['DEFAULT']['mport']
        self.mfile = config['DEFAULT']['mfile']

        b = [self.muser, self.mpwd, self.mhost, self.mport, self.mfile]
        return b

def insert_or_update(conn):
    cursor = conn.cursor(buffered=True)
    while True:
        msym = input("enter symbol: ")
        sql = """SELECT  * FROM test_prices WHERE symbol LIKE '%s' """ % msym
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is None:
            # yn = input("No stock symbol on file. Press a key")
            CanUpdate = 0

            break
            # return 0
        else:
            CanUpdate = 1
            break
            # return 1
    return CanUpdate


def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''

    conn = ' '
    msymbol = ''
    mdate = ' '
    mprice = 0

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()





if __name__ == '__main__':
    main()
