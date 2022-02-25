# insert_stocks_cl2.py
#######
# all ya need is aid to add stocks - no four table lookup!
#######
from mysql.connector import (connection)
import time
#noinspection PyUnresolvedReferences
import datetime
import configparser
import os


g_name = ''
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


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("wrong date", date_text)
        return 0


class Find:

    def __init__(self, conn, m_find1):
        self.conn = conn
        self.m_find1 = m_find1


    def find_account(self):
        try:

            cursor = self.conn.cursor()

            # m_aid = m_aid + ' collate utf8mb_general_ci'
            sql = """SELECT a.aid, a.short_acct FROM accounts a"""
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()
            self.m_find1 = input("If you see your account number, enter index number, else enter 'n'...")
        except:
            print("undetermined error")
        finally:
            return self.m_find1

    def find_stock(self, m_aid):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("maid", m_aid)
        # yn = input("Waiting at line 89")

        while True:

            cursor = self.conn.cursor()
            m_symbol = input("Enter symbol: ")
            m_symbol = '%'+m_symbol+'%'
            # print("m_aid, m_symbol", m_aid, m_symbol)
            # yn = input("waiting at line 96")
            sql = "select f.name, s.quantity,s.name, s.stock_symbol,s.price, s.trans_date, a.long_acct from stocks s " \
                  ", accounts a, firms f where f.FID = a.fid and a.aid = s.aid and s.aid = %s and s.stock_symbol" \
                  " like %s order by s.stock_symbol asc limit 10"
            format = "%m/%d/%Y"
            cursor.execute(sql, (m_aid, m_symbol))

            row = cursor.fetchone()
            if row is not None:
                print("\nFirm: ",row[0],",","Acct: ",row[6],"\n" )
            # if not row[0]:
            #     print("\n",row[0],"acct:",row[6],"\n")
            print('qty-----stock------------------------------------symbol---price-settled')
            while row is not None:
                print("{0:7.2f}".format(row[1]), "{0:<40}".format(row[2]), "{0:<6}".format(row[3]),"{0:7.2f}".format(row[4]), "{0:%m/%d/%Y}".format(row[5]))
                row = cursor.fetchone()
            yn = input("Continue (y/n): ")
            if yn == 'n' or yn == 'N':
                return yn


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
    f1 = Find(conn, m_var)
    while True:
        m_aid = f1.find_account()
        if m_aid == 'n' or m_aid == 'N':
            break

    # find, insert firm name
        while True:

            # print(m_aid)
            # m_aid = int(m_aid)

            yn = f1.find_stock(m_aid)

            if yn == 'n' or yn == 'N':
                break


if __name__ == '__main__':
    main()
