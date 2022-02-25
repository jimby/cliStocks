#!/usr/bin/env python
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


class FindAcct:
    def __init__(self, mvar, conn):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn

    def find_acct(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()

        sql = "SELECT f.name, f.Agent, a.short_acct, a.long_acct, a.acct_type FROM firms f, accounts a  WHERE a.long_acct like '%s' AND f.FID=a.fid" % self.mvar
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
            print("FIRM NAME----------------------AGENT__________________________SHORT_ACCOUNT________LONG_ACCOUNT__________________ACCT_TYPE")
            for row in data:
                print("%-30s %-30s %-20s %-10s %-10s" % ((row[0]),(row[1]),(row[2]), (row[3]), row[4]))
        cursor.close()
        # self.conn.close()
        



def main():
    muser='';mpwd='';mhost='';mport=0;mfile=''

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()

    # muser = 'b[0]'; mpwd = 'b[1]'; mhost = 'b[2]'; mport = b[3]; mfile = 'b[4]'
    mvar = ' '
    conn = ' '
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])

    conn = a1.create_connection()

    while True:
        m_var = input("Acct#: ")
        m_var = '%{}%'.format(m_var)

        if m_var == "%%":
            print("line 92, %%")
            break

        a2 = FindAcct(m_var, conn)
        a2.find_acct()

        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        # os.system('clear')
    # exit
    conn.close()
    return

if __name__ == '__main__':
    main()
    os.system('clear')
    # cursor.close
    # conn.close
    # import sys
    # find_menuNew

