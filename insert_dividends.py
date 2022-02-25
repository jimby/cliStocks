#!/usr/bin/env python
# insert_dividends.py
from mysql.connector import (connection)
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


class FindAccount:
    def __init__(self, conn, maccount):
        self.conn = conn
        self.maccount = maccount

    def find_account(self):
        """ find firm name, if already in firm table"""
        cursor = self.conn.cursor()
        self.maccount = '%'+self.maccount+'%'
        print(self.maccount)
        sql = """ SELECT aid, short_acct FROM accounts WHERE short_acct LIKE '%s' """ % (self.maccount)
        cursor.execute(sql)
        row = cursor.fetchone()
        print('AID-- ACCT#')
        while row is not None:
            print(row)
            row = cursor.fetchone()
        # return data

class FindStock:
    def __init__(self, conn, msymbol, maid, msid):
        self.conn = conn
        self.msymbol = msymbol
        self.maid = maid
        self.msid = msid

    def find_stock(self):
        # def find_stock(conn, maid):
        # """ find firm name, if already in from table"""
        self.msymbol = '%'+self.msymbol+'%'
        cursor = self.conn.cursor()
        self.msymbol = '%'+self.msymbol+'%'

        sql = """SELECT sid, aid, quantity, stock_symbol, name, price, trans_date, buyorsell FROM stocks WHERE aid =
            '%s' AND stock_symbol LIKE '%s' """ % (self.maid, self.msymbol)
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('SID-AID--QTY-SYMBOL-NAME-------------------PRICE-----DATE----------------------BUY/SELL')
        for row in rows:
            print(row)
        msid = input("Select stock-id (SID): ")
        return msid

class InsertDividend:
    def __init__(self, conn, msymbol, mdividend, mdate, maid):
        self.conn = conn
        self.msymbol = msymbol
        self.mdividend = mdividend
        self.mdate = mdate
        self.maid = maid
        

    def insert_dividend(self):
        cursor = self.conn.cursor()
        sql = """INSERT INTO dividend (symbol,Dividend,date,aid) VALUES ('%s', '%s', '%s', '%s')""" %\
          (self.msymbol, self.mdividend, self.mdate, self.maid)
        cursor.execute(sql)
        self.conn.commit()
        return cursor.lastrowid


def main():

    # mysql connection
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''



    # CONNECT TO MYSQL DATABASE
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # FindAccount
    maccount = ''

    # FindStock
    msymbol = ' '
    maid = 0
    msid = 0

    # InsertDividend
    mdate = ' '
    mdividend = 0

    fa1 = FindAccount(conn, maccount)
    while True:
        maccount = input("Enter account number: ")
        data = fa1.find_account()  # find_account
        maid = input("enter aid of account: ")  # duplicate data entry?

        while True:
            mdate = input("enter date of dividend: ")

            while True:
                # find stock already in file
                msymbol = input('Enter stock symbol:')
                # msid = find_stock(conn, m_aid, msymbol)

                # enter data
                mdividend = input('enter current dividend:')
                # mdate = input('enter settlememt date: (yyyy-mm-dd)')
                # maid = input('enter account id, aid: ')

                # insert dividend
                id1 = InsertDividend(conn, msymbol, mdividend, mdate, maid)

                lrowID = id1.insert_dividend()
                # lrowid= insert_dividend(conn, msymbol, mdividend, mdate, m_aid)                                # insert_dividend
                print(lrowID)

                yn = input('change dividend date (y/n)?  ')

                if yn == 'y' or yn =='Y':
                    break
            yn = input('Work with another account(y/n)')
            if yn == 'n' or yn == 'N':
                break

        yn = input('Quit: ')

        if yn == 'q' or yn=='Q':
            return



if __name__ == '__main__':
        main()
