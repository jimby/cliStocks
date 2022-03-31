#!/usr/bin/env python

import MakeConnection
# from mysql.connector import (connection)
import datetime
import configparser
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

    def __init__(self, conn, m_find1, m_account, m_aid):
        self.m_account = m_account
        self.conn = conn
        self.m_find1 = m_find1
        self.m_aid = m_aid

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

    def find_stock(self, m_aid):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("l92 find stock lot...")
        self.m_aid = m_aid
        while True:
            def find_account(self):
                try:

                    cursor = self.conn.cursor()

                    # m_aid = m_aid + ' collate utf8mb_general_ci'
                    sql = """SELECT accounts.aid, accounts.short_acct FROM accounts"""
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    while row is not None:
                        print(row)
                        row = cursor.fetchone()
                    self.m_find1 = input("If you see your account number, enter index number, else enter 0...")
                except:
                    print("undetermined error")
                finally:
                    return self.m_find1

            try:

                cursor = self.conn.cursor()
                # print('conn: ',self.conn)
                # print('cursor: ', cursor)
                self.m_find1 = input("l132 Enter symbol : ")
                self.m_find1 = '%{}%'.format(self.m_find1)

                # print("l103, m_aid: ", m_aid)
                # print("104, symbol: ", self.m_find1)
                # yn = input("waiting at line 104")

                # sql = """SELECT s.sid, a.long_acct, s.quantity,s.price,s.stock_symbol, s.name,s.trans_date,
                #     FROM stocks s inner join accounts a on a.aid = s.aid WHERE s.stock_symbol like '%WMT%' AND s.aid = 1"""

                sql = "select s.sid, a.long_acct, f.name, s.quantity, s.price, s.stock_symbol, s.name, s.trans_date" \
                      "  from stocks s, accounts a, firms f  where s.aid=a.aid and  a.fid=f.FID and s.stock_symbol like %s and s.aid = %s "        # where stock_symbol like  %s and aid = %s "
                cursor.execute(sql, (self.m_find1, m_aid))
                format = "%m/%d/%Y"
                # print('cursor#2: ', cursor)
                row = cursor.fetchone()
                print('sid---acct--company-------------qty-----price---symbol-----name---------------------------date------')

                while row is not None:
                    print("{0:<5}".format(row[0]),"{0:<5}".format(row[1]), "{0:<15}".format(row[2]), "{0:>10}".format(row[3]), "{0:>8}".format(row[4]), "{0:<5}".format(row[5]), "{0:<35}".format(row[6]), "{0:%m/%d/%Y}".format(row[7]))
                    row = cursor.fetchone()
                # print("row:", row)
                self.m_find1 = input("do you see your stock lot here (y/n)")
            except :
                print('error...')
            finally:
                # cursor.close()
                return self.m_find1


class Insert:
    def __init__(self, conn, m_sid, m_stock_symbol, m_name, m_quantity, m_price,
            m_fee, m_trans_date, m_buyorsell, m_aid, m_fid, m_agent, m_city_state_zip, m_email,
            m_FID, m_phone, m_street, m_acct_type, m_long_acct, m_short_acct):

        self.conn = conn
        self.m_sid = m_sid
        self.m_stock_symbol = m_stock_symbol
        self.m_name = m_name
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
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    conn = ' '
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

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

    f1 = Find(conn, m_var)
    # i1 = Insert().insert
    i1 = Insert(conn, m_sid, m_stock_symbol, m_name, m_quantity, m_price, m_fee, m_trans_date, m_buyorsell, m_aid,
        m_fid, m_agent, m_city_state_zip, m_email, m_FID, m_phone, m_street, m_acct_type,
        m_long_acct, m_short_acct)

    # find, insert firm name
    while True:

        m_aid = f1.find_account(m_long_acct)
        print(m_aid)
        # m_aid = int(m_aid)

        yn = f1.find_stock(m_aid)
        if yn == 'Y' or yn == 'y':
            yn = input("Do you want to search for more lots?")
            if yn == 'Y' or yn == 'y':
                continue
        else:
            yn = input("Do you want to add another lot of  stocks? (y/n")

        if yn == 'N' or yn == 'n':
            break
    # find, insert account number
        while True:
            m_sid = i1.insert_stock(m_aid)
            # print('m_aid: ', m_aid)

            yn = input("Continue (y/n)?")
            if yn == 'y' or yn == 'Y':
                break
            else:
                return



if __name__ == '__main__':
    main()
