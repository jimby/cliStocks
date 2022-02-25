#!/usr/bin/env python
# README: this is a collection of all find classes in cli interface

# move get_config() to class MakeConnection
from mysql.connector import (connection)
# import importlib
import configparser
import os
# this is attempt to ass configparser as function in class FindFirm

# import find_menuNew


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


class FindFirm:
    def __init__(self, mvar, conn):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn

    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % self.mvar
        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            # print(len(data))
            # t = input("line: 51")
            # print('not found')
            # print(m_var, "not found...")
            # yn = '0'
            return 0
        else:
            print("ID-----FIRM NAME")
            for row in data:
                print("{}".format(row[1]),"    ","{}".format(row[0]))
        cursor.close()
        # self.conn.close()

class FindAcct:
    def __init__(self, mvar, conn, maid, mshort_acct, mlong_acct, macct_type, mfid, mname):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn
        self.maid = maid
        self.mshort_acct = mshort_acct
        self.mlong_acct = mlong_acct
        self.macct_type = macct_type
        self.mfid = mfid
        self.mname = mname

    def find_accts(self,conn):
        """ find aid, stock_symbol, if already in stocks table"""
        manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.mlong_acct = input("enter account#: ")
        self.mlong_acct = '%{}%'.format(self.mlong_acct)
        print(self.mlong_acct)
        yn = input('line 58')

        # choose record to edit
        sql = """SELECT a.aid, f.name, a.short_acct, a.long_acct, a.acct_type  FROM accounts a, firms f WHERE f.FID = a.fid AND a.long_acct LIKE '%s' """ % self.mlong_acct
        print('sql:', sql)
        yn = input('waiting at line 64')

        try:
            yn = input('Waiting at line 67')
            cursor.execute(sql)
            results = cursor.fetchall()
            # print("ID| firm name", "{0:60s}".format(row[0]))
            print("AID__AcctName__________________ShortAcct______________________Long account__________account type")
            for row in results:
                # print("%-4d %-25s %-30s %-25s %-25s" % (row[0], row[1], row[2], row[3], row[4]))
                print(row)
            self.maid = input("Enter id or quit: (q)?")
            return self.maid
            # print('fid: ', self.mfid)
            # yn = input('waiting at line 74')
        except Exception as e:
            print("Error: no data")
            return 0
		cursor.close()  
		

class FindStock:
    def __init__(self, mvar, conn):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn

    def find_stock(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        # sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % self.mvar

        # sql = "SELECT s.sid, s.stock_symbol,s.quantity,s.name, s.price, p.prices, a.long_acct, p.effective_date" \
        #      " FROM firms f, accounts a,  stocks s, prices p  WHERE p.sid=s.sid and s.aid=a.aid and a.fid=f.FID and  s.stock_symbol like '%s' " % self.mvar

        sql = "SELECT stocks.sid, stocks.stock_symbol, stocks.quantity, stocks.name, stocks.price, prices.prices," \
              " accounts.long_acct, prices.effective_date from prices" \
              " INNER JOIN stocks ON prices.sid = stocks.sid" \
              " INNER JOIN accounts ON stocks.aid=accounts.aid" \
              " INNER JOIN firms ON accounts.FID = firms.fid" \
              " WHERE stocks.stock_symbol LIKE '%s' ORDER BY stocks.name ASC" % self.mvar


        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            # print(len(data))
            # t = input("line: 51")
            # print('not found')
            # print(m_var, "not found...")
            # yn = '0'
            return 0
        else:
            # print("ID-----FIRM NAME")
            print("-SID-SYM----QTY---NAME---------------------------price1 price2 acct-DATE---------GAIN")
            for row in data:
                # print("{}".format(row[1]),"    ","{}".format(row[0]))
                print("{:3d}".format(row[0]), "{0:5}".format(row[1]), "{:6.2f}".format(row[2]), "{0:30}".format(row[3]),
                "{:6.2f}".format(row[4]), "{:6.2f}".format(row[5]), "{0:15}".format(row[6]),
                "{:%m/%d/%Y}".format(row[7]), "{:6.1f}".format((100 * (row[5] - row[4]) / row[4])), "%")
        cursor.close()
        # self.conn.close()
		          

        
