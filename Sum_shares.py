# Sum_shares.py
# import sys
from mysql.connector import (connection)
import configparser
# import configparser
# import os
class MakeConnection:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
        #     self.name = name    # instance variable unique to each instance
        self.muser = muser
        self.mpwd = mpwd
        self.mhost = mhost
        self.mport = mport
        self.mfile = mfile

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        muser = config['DEFAULT']['muser']
        mpwd = config['DEFAULT']['mpwd']
        mhost = config['DEFAULT']['mhost']
        mport = config['DEFAULT']['mport']
        mfile = config['DEFAULT']['mfile']
        b = [muser, mpwd, mhost, mport, mfile]
        return b

    def create_connection(self):
        try:
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport,
                                              database=self.mfile)
            cursor = conn.cursor()
            print("connected")
            return conn
        except Exception as e:
            print("no connection")
            return e
class SumShares:
    def __init__(self, conn, msymbol, maid):
        self.conn = conn
        self.msymbol = msymbol
        self.maid = maid

    def sum_shares(self):
        # input("line 56")
        self.msymbol = input("Symbol: ")
        # self.mdate   = input("date (YYYY-MM-DD): ")
        self.maid    = input("Account index: ")
        cursor = self.conn.cursor()

        sql1 = """SELECT sum(quantity) INTO @mvar FROM stocks WHERE stock_symbol=%s and aid =%s"""
        sql2 = "SELECT @mvar AS manswer"

        cursor.execute(sql1, (self.msymbol, self.maid))
        mresult1 = cursor.fetchone()
        # print(msymbol, myresult1)

        cursor.execute(sql2)
        row = cursor.fetchone()

        while row is not None:
            # print("row: ",row)
            mvar = row[0]
            print(self.msymbol, "total shares: ", mvar)
            row = cursor.fetchone()

def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    conn = ' '

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()

    a1 = MakeConnection(b[0], b[1], b[2] , b[3], b[4])
    conn = a1.create_connection()

    msymbol = ''
    mdate = " "
    maid = 0

    ss1 = SumShares(conn, msymbol, maid)

    while True:
        msymbol = 'T'
        mdate = '2021-12-31'
        maid = 1

        ss1.sum_shares()


if __name__ == '__main__':
    main()




