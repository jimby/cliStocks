#!/usr/bin/env python

import MakeConnection
# from mysql.connector import (connection)
import datetime
# import configparser
import os


#g_name = ''# global yn
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("wrong date", date_text)
        return 0


class Find:

    def __init__(self, conn):
    #        self.m_account = m_account
        self.conn = conn
    #        self.m_symbol = m_symbol
    #        self.m_aid = m_aid
    #        self.m_fid = m_fid
    #        self.m_lot = m_lot

# find_firm
    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""

        m_fid = 0
        m_firm = input("Enter investment firm name: ")
        m_firm = '%' + m_firm + '%'

        cursor = self.conn.cursor()
        sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % m_firm
        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            return 0
        else:
            print("ID-----FIRM NAME")
            for row in data:
                print("{}".format(row[1]), "    ", "{}".format(row[0]))
            m_firm = input("Enter ID (fid), y/n:")
            return m_fid
            

        cursor.close()
        # self.conn.close()

# find account
    def find_account(self):

        m_account = input('L30 long_acct: ')
        m_account = m_account

        cursor = self.conn.cursor()
        sql = "SELECT a.aid, a.long_acct, a.acct_type FROM accounts a  WHERE a.long_acct like '%s' " % m_account
        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            return 0
        else:
            print('ID--ACCOUNT--ACCOUNT TYPE')
            for row in data:
                print(row)

            m_aid = input("Enter account ID (aid) :")
        return m_aid

# find symbol
    def find_stock(self, m_aid, m_fid):

        m_name = input('L 48 Enter stock name: ')
        m_name = '%' + m_name + '%'
        while True:
            m_sid = 0
            cursor = self.conn.cursor()

            # sql = """SELECT stocks.sid, accounts.long_acct, stocks.name, stocks.stock_symbol, stocks.trans_date FROM accounts
            # INNER JOIN firms on accounts.fid = firms.FID INNER JOIN stocks.aid = accounts.aid
            # where stocks.name like '%s' """ % m_name
            sql = "SELECT stocks.sid, stocks.stock_symbol, stocks.quantity, stocks.name, stocks.price, prices.prices," \
                  " accounts.long_acct, prices.effective_date from prices" \
                  " INNER JOIN stocks ON prices.sid = stocks.sid" \
                  " INNER JOIN accounts ON stocks.aid=accounts.aid" \
                  " INNER JOIN firms ON accounts.FID = firms.fid" \
                  " WHERE stocks.stock_symbol LIKE '%s' and " % m_name

            cursor.execute(sql)
            data = cursor.fetchall()
            print("ID---ACCT---NAME--SYMBOL--LOT---DATE")
            #while row is not None:
            for row in data:
                print(row)
                #print("{}".format(row[0]), "{}".format(row[1]), "{}".format(row[2]), "{}".format(row[3]), "{}".format(row[4]), "{}".format(row[5]), "{}".format(row[6]), "{}".format(row[7]))
                # row = cursor.fetchone()

            m_sid = input("If you see your symbol, enter index number (sid), else enter 0...")
            return m_sid

# find stock_lot
#    def find_stock_lot(self):
#            cursor = self.conn.cursor()
#            # print('conn: ',self.conn)
#            # print('cursor: ', cursor)
#            self.m_msymbol = input("l132 Enter symbol : ")
#            self.m_symbol = '%{}%'.format(self.m_msymbol)
#
#            sql = "select s.sid, a.long_acct, f.name, s.quantity, s.price, s.stock_symbol, s.name, s.trans_date" \
#                  "  from stocks s, accounts a, firms f  where s.aid=a.aid and  a.fid=f.FID and s.stock_symbol like %s and s.aid = %s "        # where stock_symbol like  %s and aid = %s "
#            cursor.execute(sql, (self.m_symbol, self.m_aid))
#            format = "%m/%d/%Y"
#            # print('cursor#2: ', cursor)
#            row = cursor.fetchone()
#            print('sid---acct--company-------------qty-----price---symbol-----name---------------------------date------')
#
#
#            while row is not None:
#                print("{0:<5}".format(row[0]),"{0:<5}".format(row[1]), "{0:<15}".format(row[2]), "{0:>10}".format(row[3]), "{0:>8}".format(row[4]), "{0:<5}".format(row[5]), "{0:<35}".format(row[6]), "{0:%m/%d/%Y}".format(row[7]))
#                row = cursor.fetchone()
#                self.m_ot = input("do you see your stock lot here (y/n)")#
#
#            if not row:
#                print('error...')
#
#            return self.m_lot


class Insert:
    def __init__(self, conn, m_sid, m_stock_symbol, m_stock_name, m_quantity, m_price,
            m_fee, m_trans_date, m_buyorsell, m_aid, m_fid, m_agent, m_city_state_zip, m_email,
            m_FID, m_phone, m_street, m_acct_type, m_long_acct, m_short_acct):

        self.conn = conn
        self.m_sid = m_sid
        self.m_stock_symbol = m_stock_symbol
        self.m_name = m_stock_name
        self.m_quantity = m_quantity
        self.m_price = m_price
        self.m_fee = m_fee
        self.m_trans_date = m_trans_date
        self.m_buyorsell = m_buyorsell
        self.m_aid = m_aid
        self.m_fid = m_fid
        self.m_agent = m_agent
        self.m_city_state_zip = m_city_state_zip
        self.m_email = m_email
        self.m_FID = m_FID
        self.m_phone = m_phone
        self.m_street = m_street
        self.m_acct_type = m_acct_type
        self.m_long_acct = m_long_acct
        self.m_short_acct = m_short_acct

    def insert_stock(self, m_aid):
        cursor = self.conn.cursor(buffered=True)

        self.m_stock_symbol = input("Add lot- Enter symbol again:")
        self.m_name = input(" Enter stock name: ")
        self.m_quantity = input("Enter quantity: ")
        self.m_cost = input("Enter purchase or sell price: ")
        self.m_fee = input("Enter commission or fee: ")
        if self.m_fee is None:
            self.m_fee = 0

        # validate date
        while True:
            # t = 1
            self.m_trans_date = input("Enter date (YYYY-MM-DD): ")
            t = validate(self.m_trans_date)
            if t:
                break

        self.m_buyorsell = input("Is this a buy or sell (buy/sell) ?: ")
        self.m_aid = m_aid

        sql = """INSERT INTO stocks (stock_symbol, name, quantity, price, fee, trans_date, buyorsell, aid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (self.m_stock_symbol, self.m_name, self.m_quantity, self.m_cost, self.m_fee,
                             self.m_trans_date, self.m_buyorsell, self.m_aid))
                       
        self.conn.commit()
        # lastrow = cursor.lastrowid()
        # return int(lastrow)

    def insert_firm(self):
        cursor = self.conn.cursor(buffered=True)

        self.m_name = input('Enter firm name: ')
        self.m_street = input('Enter street address: ')
        self.m_city_state_zip = input('Enter City, State, and Zip: ')
        self.m_agent = input("Enter adviser's name: ")
        self.m_phone = input('Enter firm telephone number: ')
        self.m_email = input('Enter firm email address:')

        sql = """INSERT INTO firms (name, street, city_state_zip, agent, phone, email) VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (self.m_name, self.m_street, self.m_city_state_zip, self.m_agent, self.m_phone, self.m_email))
        self.conn.commit()
        self.m_fid = int(cursor.lastrowid)

        return self.m_fid

    def insert_account(self, m_fid):
        cursor = self.conn.cursor(buffered=True)

        self.m_short_acct = input("L226 Enter short account number: ")
        self.m_long_acct = input("L227 Enter long account number: ")
        self.m_acct_type = input("L228 Enter account type: ")
        self.m_fid = m_fid

        sql = """INSERT INTO accounts (short_acct, long_acct, acct_type, fid) VALUES (%s, %s, %s, %s) """

        cursor.execute(sql, (self.m_short_acct, self.m_long_acct, self.m_acct_type, self.m_fid))
        self.conn.commit()
        self.m_aid = cursor.lastrowid

        return int(self.m_aid)


def main(i1=None, f1=None):
    conn = MakeConnection.get_config()
    # class Find
    m_var = ' '
    
    # class Insert
    m_sid = 0
    m_stock_symbol = ' '
    m_name = ' '
    m_quantity = 0
    m_price = 0
    m_fee = 0
    m_trans_date = ' '
    m_buyorsell = ' '
    m_aid = 0
    m_fid = 0
    m_agent = ' '
    m_city_state_zip = ' '
    m_email = ' '
    m_FID = 0
    m_phone = ' '
    m_street = ' '
    m_acct_type = ''
    m_long_acct = ' '
    m_short_acct = ' '

    f1 = Find(conn)
    # i1 = Insert().insert
    #i1 = Insert(conn, m_sid, m_stock_symbol, m_name, m_quantity, m_price, m_fee, m_trans_date, m_buyorsell, m_aid,
    #    m_fid, m_agent, m_city_state_zip, m_email, m_FID, m_phone, m_street, m_acct_type,
    #    m_long_acct, m_short_acct)

    # find, insert firm name
    while True:
        m_fid = f1.find_firm()
        # print("m_fid: ", m_fid)
        # yn = input('wait at l250')
        yn = input('L252 find account (y/n)?')
        if yn == 'N' or yn == 'n':
            break

        while True:
            m_aid = f1.find_account()
            print('m_aid: ', m_aid)
            yn = input('wait at line 255')
            yn = input('L260 find stock name? (y/n)')
            if yn == 'N' or yn == 'n':
                break

            while True:
                m_sid = f1.find_stock(m_aid, m_fid)
                print('m_sid: ', m_sid)
                yn = input('wait at line 255')
                yn = input('continue with m_sid? (y/n)')
                if yn == 'N' or yn == 'n':
                    break



if __name__ == '__main__':
    main()
