#!/usr/bin/env python
# edit first, then if no price, insert

#######
import MakeConnection
# from mysql.connector import (connection)
import datetime
# import os
# import configparser

#
# import os


# g_name = ''
# global yn

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
        # m_account = input("Enter account number: ")
        cursor = self.conn.cursor()
        m_var = 0
        while True:
            print("aid--acct--acct_type")
            try:
                sql = """select a.aid, a.long_acct, a.acct_type FROM accounts a WHERE a.long_acct LIKE '%s' """ % self.m_account
                cursor.execute(sql)
                row = cursor.fetchone()
                if len(row) == 0:
                    return 0
                else:
                    while row is not None:
                        print("{:3d}".format(row[0]), '  ', "{}".format(row[1]))

                self.m_aid = input("Enter account index number (AID)")
                return self.m_aid
            except ValueError:
                print('Error: unknown error')


    def find_symbol(self, m_aid, m_symbol):
    # def find_symbol(self, m_aid,  m_symbol, m_sid):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        # self.m_aid = m_aid
        # self.m_symbol = m_symbol
        # self.m_sid = m_sid
        m_var = 0
        while True:
            # def find_account(self):
            print("SID -SYMBOL NAME - ----------------LOT - -QTY - -PRICE")
            try:

                # m_aid = m_aid + ' collate utf8mb_general_ci'
                sql = "SELECT s.sid, s.stock_symbol, s.name, s.lot_number, s.quantity, s.price FROM stocks s WHERE s.aid LIKE %s AND s.stock_symbol LIKE %s "
                params = (self.m_aid, self.m_symbol)
                cursor.execute(sql, params)
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()
                m_sid = input("l101 If you see your stock symbol here, enter index number (sid), else enter 0...")
            except:
                print("-undetermined error")
                print("msid: ", m_sid)
                yn = input("waiting at line 73")
            finally:
                print("msid: ", m_sid)
                yn = input("waiting at line 76")
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
    conn = MakeConnection.get_config()
    if not conn:
        print("no connection fl65")

    # class find
    m_symbol = ' '
    m_account = ' '
    m_aid = ' '
    m_sid = ' '


    # class Find
    # m_var = ' '

    # class Insert
    # m_symbol = " "
    m_date = " "
    m_price = " "
    # m_sid = 0


    f1 = Find(conn, m_symbol, m_account, m_aid, m_sid)
    # i1 = Insert().insert
    # print("170 m_sid: ", m_sid)
    # yn = input("waiting at line 171")

    i1 = Insert(conn, m_symbol, m_date, m_price, m_sid)

    # find, insert firm name
    while True:

        #find account
        m_account = input("Account#: ")
        m_account = '%{}%'.format(m_account)
        m_aid = f1.find_account(m_account)


        # find symbol-
        #   if no symbol, insert price
        m_symbol = input("L172 Enter stock_symbol: ")
        print("Symbol, aid", m_symbol, m_aid)
        yn = ('Waiting at line 168)')
        m_sid = f1.find_symbol(m_aid, m_symbol)
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
