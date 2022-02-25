from mysql.connector import (connection)
import configparser
import os

def InsertOrUpdate(conn, msym):
    cursor = conn.cursor(buffered=True)
    while True:
        # msym = input("enter symbol: ")
        sql = """SELECT  * FROM test_prices WHERE symbol LIKE '%s' """ % msym
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is None:  
            # insert, because no row
            return 0
            break
        else:
            #update, because row was found
            return 1
            break
    return CanUpdate



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
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport,
                                              database=self.mfile)
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

class InsertPrices:
    def __init__(self,conn, msymbol, mdate, mprice):    # sid not used here
        self.conn = conn
        self.msymbol = msymbol
        self.mdate = mdate
        self.mprice = mprice

    def insert_price(self):
        cursor = self.conn.cursor(buffered=True)
        # print("This program will enter purchase date and purchase price")
        while True:
            sql = """INSERT INTO test_prices (symbol, effective_date, prices) VALUES (%s, %s, %s)"""
            cursor.execute(sql, (self.msymbol, self.mdate, self.mprice))
            self.conn.commit()
            # print('inserted row(s): ', cursor.lastrowid())
            break
            return cursor.lastrowid


class UpdatePrices:
    def __init__(self, conn, msymbol, mdate, mprice):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.msymbol = msymbol
        self.mdate = mdate
        self.mprice = mprice

    def update_prices(self):
        query = """UPDATE test_prices SET effective_date = %s, prices = %s WHERE symbol = %s"""
        data = (self.mdate, self.mprice, self.msymbol)
        try:
            cursor = self.conn.cursor(buffered=True)
            cursor.execute(query, data)
            self.conn.commit()
        except Error as error:
            print(error)
        # finally:
            # cursor.close()
            # self.conn.close()
    


def main():
    # mysql connection
    muser = '';mpwd = '';mhost = '';mport = 0;mfile = ''
    conn = '';msymbol = '';mdate = '';mprice = 0

    # CONNECT TO MYSQL DATABASE
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # u1 = UpdatePrices(conn, msymbol, mdate, mprice)
    # i1 = InsertPrices(conn, msymbol, mdate, mprice)

    while True:
        msymbol = input("Enter ticker symbol: ")
        msymbol = msymbol.upper()
        if not mdate:
            mdate = input("Enter date: (yyyy-mm-dd) ")
        mprice = input("Enter stock price: ")
        
        # check to see if update or insert
        mrow = InsertOrUpdate(conn, msymbol)
        if mrow == 0:                          # insert, because no row w/ticker symbol
            i1 = InsertPrices(conn, msymbol, mdate, mprice)
            i1.insert_price()
        elif mrow == 1:                         # update, because ticker symbol row exists
            u1= UpdatePrices(conn, msymbol, mdate, mprice)
            u1.update_prices()

        yn = input('Continue (y/n)')
        if yn == 'n':
            break
    os.system('clear')
    # conn.close()


if __name__ == '__main__':
    main()
    os.system('clear')
    # conn.close()