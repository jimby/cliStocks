#!/usr/bin/env python
# insert_dividends.py

import MakeConnection
import os


class FindAccount:
    def __init__(self, conn):
        self.conn = conn

    def find_accts(self, conn):
        """ find aid, stock_symbol, if already in stocks table"""
        # manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.mlong_acct = input("Enter account#: ")
        self.mlong_acct = '%{}%'.format(self.mlong_acct)
        print(self.mlong_acct)
        # choose record to edit
        sql = """SELECT a.aid, f.name, a.short_acct, a.long_acct, a.acct_type  FROM accounts a, firms f WHERE f.FID = a.fid AND a.long_acct LIKE '%s' """ % self.mlong_acct
        # print('sql:', sql)
        # yn = input('l23 waiting')

        try:
            # yn = input('l26 Waiting')
            cursor.execute(sql)
            results = cursor.fetchall()
            # print("ID| firm name", "{0:60s}".format(row[0]))
            print("AID__AcctName__________________ShortAcct______________________Long account__________account type")
            for row in results:
                print("%-4d %-25s %-30s %-25s %-25s" % (row[0], row[1], row[2], row[3], row[4]))
                # print(row)
            self.maid = input("l34 Enter id or quit: (q)?")
            return self.maid
            # print('fid: ', self.mfid)
            # yn = input('l 37 waiting')
        except Exception as e:
            print("Error: no data")
            yn = input("l40 Return")
            return 0    
        
    
class FindStock:

    cursor = ''
    msymbol = ''
    
    def __init__(self, conn, m_aid, m_symbol):
        self.conn = conn
        self.m_aid = m_aid
        self.m_symbol = m_symbol
        
    def find_stock(self, conn):
        """ find aid, stock_symbol, if already in stocks table"""

        # while True:
        cursor = self.conn.cursor()

        while True:
            m_symbol = input("Enter stock symbol: ")
            m_symbol = '%{}%'.format(m_symbol)
        
            sql = "SELECT stocks.sid, stocks.stock_symbol, stocks.quantity, stocks.name, stocks.price, prices.prices," \
              " accounts.long_acct, prices.effective_date from prices" \
              " INNER JOIN stocks ON prices.sid = stocks.sid" \
              " INNER JOIN accounts ON stocks.aid=accounts.aid" \
              " INNER JOIN firms ON accounts.FID = firms.fid" \
              " WHERE stocks.stock_symbol LIKE '%s' " % m_symbol
          
            cursor.execute(sql)
            
            data = cursor.fetchall()
            
            if len(data) == 0:
                print("no symbol found")
        
            for row in data:
                print("{a:<15}".format(a='stock id:'),"{}".format(row[0]),                  # next -> move "stock id:" etc to one line
                     "{a:<15}".format(a='symbol'),"{}".format(row[1]),
                     "{a:<15}".format(a='name:'),"{}".format(row[3]),
                     "{a:<15}".format(a='buy price:'),"{}".format(row[4]),
                     "{a:<15}".format(a='current price:'),"{}".format(row[5]),
                     "{a:<15}".format(a='account:'),"{}".format(row[6]),
                     "{a:<15}".format(a='settled:'),"{}".format(row[7]))
                
            try:
                cursor.execute(sql)
                results = cursor.fetchall()

                print("SID|symbol-|firm name--------------------|qty---|price|date------|acct")
                for row in results:
                    print("%-4d %-25s %-30s %-25s %-25s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                m_sid = input("l76 Enter sid: ")
                return m_sid
            except:
                print("l79 Error: no data")
                yn = input("l80 Return")
                return 0


class InsertDividend:


    def __init__(self, conn, maid, msid):
        self.conn = conn

    def insert_dividend(self):
        mdiv = input('l92 Enter dividend: ')
        mdate = input('l93 Enter dividend date ("MM/DD/YYYY"): ')
        cursor = self.conn.cursor()

        sql = """INSERT INTO dividend (Dividend,date,aid, sid) VALUES ('%s', '%s', '%s', '%s')""" %\
          (mdiv, mdate, self.maid, self.msid)
        cursor.execute(sql)
        self.conn.commit()
        return cursor.lastrowid


def main():

    # mysql connection
    conn = MakeConnection.get_config()
    m_aid = 0
    m_sid = 0
    m_symbol = ''





  # yn = input('l109 waiting')
    if not conn:
        print("no database connection")
 
    while True:                                                                     # find and save account number
        fa = FindAccount(conn)
        m_aid = fa.find_accts(conn)
        # print("account: ", m_aid)
        # yn = input('Continue (y/n): ')
        #if yn == 'N' or yn == 'n':
        #     break

        while True:                                                                 # find stock symbol
            fs = FindStock(conn, m_aid, m_symbol)
            # msymbol = input("l128 Enter stock symbol: ")
            m_sid = fs.find_stock(conn)
            # yn = input('L 149')
            m_account = input("l143 Enter account number: ")
            data = fa.find_accts()  # find_account
            # maid = input("l145 enter aid of account: ")  # duplicate data entry?

        
            m_date = input("l148 enter date of dividend: ")

        
            # find stock already in file
            msymbol = input('l152 Enter stock symbol:')
            msid = fs.find_stock(conn, m_aid)

            id = InsertDividend(conn, m_aid, m_sid)                                   # insert dividend
            id(conn, m_aid, m_sid)
            # yn = input('l138 continue (y/n)?  ')

            if yn == 'y' or yn =='Y':
                break
            yn = input('l170 Work with another account(y/n)')
            if yn == 'n' or yn == 'N':
                break

        yn = input('l174 Quit: ')

        if yn == 'q' or yn=='Q':
            return



if __name__ == '__main__':
        main()
