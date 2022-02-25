#!/usr/bin/env python
# edit_stocks.py
# __all__ = ['datetime']
from mysql.connector import (connection)
import configparser
import os
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


class UpdatePrices:
    def __init__(self, msymbol, mprice, mdate, conn):
        self.msymbol = msymbol
        self.mprice = mprice
        self.mdate = mdate
        self.conn = conn

    def update_prices(self):
        """ find aid, stock_symbol, if already in stocks table"""
        print("price", self.mprice)
        yn = input("wait")
        print("price: ", self.mprice)
        print("date: ", self.mdate)
        print("symbol: ", self.msymbol)
        # yn = "line 34"
        cursor = self.conn.cursor()
        # sql = "UPDATE prices  set  prices=%s,  effective_date=% WHERE symbol = '%s'" % (self.mprice, mdate, msymbol)
        cursor.execute(""" update TestPrices set prices=%s, effective_date=%s where symbol=%s""", (self.mprice, self.mdate, self.msymbol))
        self.conn.commit()
        print(cursor.rowcount, "record(s) affected")
        cursor.close()
        # self.conn.close()


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    muser = config['DEFAULT']['muser']
    mpwd = config['DEFAULT']['mpwd']
    mhost = config['DEFAULT']['mhost']
    mport = config['DEFAULT']['mport']
    mfile = config['DEFAULT']['mfile']

    b = [muser, mpwd, mhost, mport, mfile]
    return b


def main():
    b = get_config()
    muser = 'b[0]'; mpwd = 'b[1]'; mhost = 'b[2]'; mport = b[3]; mfile = 'b[4]'
    mvar = ' '
    conn = ' '
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()


    while True:
        m_symbol = ''
        m_price = 0
        m_date = ' '

        m_symbol = input("Symbol: ")
        m_symbol = '{}'.format(m_symbol)
        if m_symbol == "":
            break

        m_price = input("New price: ")
        m_price = '{}'.format(m_price)
        if m_price == "":
            break

        m_date = input("New date: (YYYY-MM-DD)")
        m_date = '{}'.format(m_date)
        if m_date == "":
            break

        a2 = UpdatePrices(m_symbol, m_price, m_date, conn)
        a2.update_prices()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        os.system('clear')
    exit
    conn.close()


if __name__ == '__main__':
    main()
    os.system('clear')

