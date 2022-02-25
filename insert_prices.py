#!/usr/bin/env python
#######
from mysql.connector import (connection)
import datetime
import configparser

#
# import os


# g_name = ''
# global yn
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


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("malformed date entry", date_text)
        return 0


class Find:

    def __init__(self, conn, m_symbol, m_account, m_aid, m_sid):
        self.conn = conn
        self.m_symbol = m_symbol
        self.m_account = m_account
        self.m_aid = m_aid
        self.m_sid = m_sid

    def find_account(self, m_account):
        """ find aid, stock_symbol, if already in stocks table"""
        self.m_account = m_account
        cursor = self.conn.cursor()
        sql = "SELECT a.aid, a.short_acct, a.long_acct, a.acct_type FROM test_accounts a  WHERE a.long_acct like '%s' " % self.m_account
        cursor.execute(sql)

        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        self.m_aid = input("Enter aid:")
        return self.m_aid

    def find_symbol(self, m_aid, m_symbol, m_sid):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        self.m_aid = m_aid
        self.m_symbol = m_symbol
        self.m_sid = m_sid
        m_var = 0
        while True:
            # def find_account(self):
            print("SID -SYMBOL NAME - ----------------LOT - -QTY - -PRICE")
            try:

                # m_aid = m_aid + ' collate utf8mb_general_ci'
                sql = "SELECT s.sid, s.stock_symbol, s.name, s.LotNumber, s.quantity, s.price FROM test_stocks s WHERE s.aid LIKE %s AND s.stock_symbol LIKE %s "
                params = (m_aid, m_symbol)
                cursor.execute(sql, params)
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()
                m_sid = input("l101 If you see your stock symbol here, enter index number (sid), else enter 0...")
            except:
                print("-undetermined error")
            finally:
                return m_sid



class Insert:
    def __init__(self, conn, m_symbol ,m_effective_date, m_price, m_sid):
        self.conn = conn
        self.m_symbol = m_symbol
        self.m_effective_date = m_effective_date
        self.m_price = m_price
        self.m_sid = m_sid

    def insert_price(self, m_symbol, m_effective_date, m_price, m_sid):
        print("1121 m_sid: ", m_sid)
        yn = input("waiting at line 122")

        cursor = self.conn.cursor(buffered=True)

        # print("symbol: ", m_symbol)
        self.m_symbol = m_symbol
        self.m_price = input("Enter current stock price:  ")
        # self.m_effective_date = input("Enter date of new price (YYYY-MM-DD): ")
        self.m_sid = m_sid

        while True:
            self.m_effective_date = input("Enter date of price (YYYY-MM-DD) : ")
            t = validate(self.m_effective_date)
            if t:
                break

        print("m_symbol", self.m_symbol)
        print("price: ", self.m_price)
        print("date: ", self.m_effective_date)
        print("stock index #: ", self.m_sid)

        yn= input("waiting at line 125")
        # noinspection SqlResolve
        sql = """INSERT INTO test_prices (symbol, effective_date, prices, sid ) VALUES (%s, %s, %s, %s)"""
        params = (self.m_symbol, self.m_effective_date, self.m_price, self.m_sid)
        cursor.execute(sql, params)
        self.conn.commit()

        # self.m_fid = int(cursor.lastrowid)
        # return self.m_fid


def main(i1=None, f1=None):

    # class MakeConnection
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    conn = ' '

    # class find
    m_symbol = ' '
    m_account = ' '
    m_aid = ' '
    m_sid = ' '

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # class Find
    # m_var = ' '

    # class Insert
    # m_symbol = " "
    m_date = " "
    m_price = " "
    # m_sid = 0


    f1 = Find(conn, m_symbol, m_account, m_aid, m_sid)
    # i1 = Insert().insert
    print("170 m_sid: ", m_sid)
    yn = input("waiting at line 171")

    i1 = Insert(conn, m_symbol, m_date, m_price, m_sid)

    # find, insert firm name
    while True:
        m_account = input("Account#: ")
        m_account = '%{}%'.format(m_account)

        m_aid = f1.find_account(m_account)
        # maid = int(maid)

        m_symbol = input("L172 Enter stock symbol: ")
        m_sid = f1.find_symbol(m_aid, m_symbol, m_sid)
        print("185 m_sid: ", m_sid)
        yn = input("waiting at line 186")

        while True:
            # m_price = input("Enter new price: ")
            # m_date = input("Enter price date: ")
            print("m_symbol: ", m_symbol)
            print("l192 m-sid: ", m_sid)
            yn = input("waiting at line 193")
            i1.insert_price(m_symbol, m_date, m_price, m_sid)
            # print('m_aid: ', m_aid)

            yn = input("Continue (y/n)?")
            if yn == 'y' or yn == 'Y':
                break
            else:
                return


if __name__ == '__main__':
    main()
