#!/usr/bin/env python
# insert_stocks_cl.py

from mysql.connector import MySQLConnection, Error
import configparser
import os
import time
#noinspection PyUnresolvedReferences
import datetime



# validate date
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("wrong date", date_text)
        return 0

#create connection to NAS database
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
            conn = MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport, database=self.mfile)
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

#  find things
class Find:
    def __init__(self, conn, m_acct_type, m_fname, m_sacct, m_lacct, m_fid, m_ssymbol, m_qty, m_price, m_fee, m_tdate, m_bs, \
                 m_aid, m_sname, m_agent, m_cszip, m_email, m_phone, m_street, m_sid ):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.m_acct_type = m_acct_type
        self.m_fname = m_fname
        self.m_sacct = m_sacct
        self.m_lacct = m_lacct
        self.m_fid = m_fid
        self.m_ssymbol = m_ssymbol
        self.m_qty = m_qty
        self.m_price = m_price
        self.m_fee = m_fee
        self.m_tdate = m_tdate
        self.m_bs = m_bs
        self.m_aid = m_aid
        self.m_sname = m_sname
        self.m_agent = m_agent
        self.m_cszip = m_cszip
        self.m_email = m_email
        self. m_phone = m_phone
        self.m_street = m_street
        self.m_sid = m_sid
        print('conn:', self.conn)
        yn = input('stopping at line 82')

    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("aid,stock_symbol", aid, stock_symbol)
        cursor = self.conn.cursor()
        # m_symbol = input("Symbol: ")
        # m_symbol = '%{}%'.format(m_symbol)
        # print(m_symbol)
        sql = """ SELECT f.FID FROM firms f WHERE f.name like '%s';""" % self.m_fname
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) == 0:
            # print(len(data))
            # t = input("line: 51")
            # print('not found')
            print(self.m_name, " not found...")
            # yn = '0'
            return 0
        else:
            print("ID-----FIRM----------")
            for row in data:
                print("{}".format(row[1]),"    ","{}".format(row[0]))

    def find_account(self):
        cursor = self.conn.cursor()
        """ find firm name, if already in firm table"""
        while True:

            self.m_lacct = input("Enter account number: ")
            self.m_lacct = '%'+self.m_lacct+'%'

            # print(val1)
            sql = """SELECT aid, long_acct FROM accounts WHERE long_acct LIKE '%s' """ % self.m_lacct
            cursor.execute(sql)
            data = cursor.fetchall()

            if len(data) > 0:
                sfound = 1
            elif len(data) == 0:
                sfound = 0
                return sfound
            if sfound == 1:
                for row in data:
                    print(row)
                # answer = input("Do you see your "+msg+" here (y/n)")
                # if answer == 'y' or answer == 'Y':
                val = input("enter account index number (AID): ")
                return val


    def find_stock(self):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("aid,stock_symbol", aid, stock_symbol)
        print('conn', self.conn)
        yn = input('stopping at line 138')

        cursor = self.conn.cursor()

        # m_aid = aid
        m_symbol = input("Enter symbol : ")
        m_symbol = '%{}%'.format(m_symbol)

        while True:

            sql = """SELECT a.aid, a.long_acct, s.quantity,s.stock_symbol,s.price,s.name,s.trans_date, a.short_acct\
            FROM (stocks s inner join accounts a on s.aid = a.aid) WHERE stock_symbol LIKE '%s' """ % self.m_ssymbol
            print("AID LACCT QTY     SYMBOL PRICE  NAME  DATE    SACCOUNT")
            try:
                cursor.execute(sql, m_symbol)
                row = cursor.fetchone()
                while row is not None:
                    print("{0.3f}".format(row[0]), "{:25s}".format(row[1]), "{0:.3f}".format(row[2]), "{:15s}".format(row[3]), \
                          "{0.3f}".format(row[4]), "   ", "{:25s} ".format(row[5]), "{:%m/%d/%Y}".format(row[6]), "{:25s}".format(row[7]))
                    row = cursor.fetchone()
            except Error as e:
                print(e)
            finally:
                cursor.close()

            self.conn.close()

            answer = input("\nIf you see your stock lot here enter SID number, search again, or quit, enter (index (SID)/a/q)")
            val = ' '
            if val == int(answer):
                return val
            elif answer == 'N' or answer == 'n':
                return 0
            elif answer == 'A' or answer == 'a':
                return 'a'

                                                 # symbol


class Insert:
    def __init__(self, conn, m_acct_type, m_fname, m_sacct, m_lacct, m_fid, m_ssymbol, m_qty, m_price, m_fee, m_tdate, m_bs, \
                 m_aid, m_sname, m_agent, m_cszip, m_email, m_phone, m_street ):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.m_acct_type = m_acct_type
        self.m_fname = m_fname
        self.m_sacct = m_sacct
        self.m_lacct = m_lacct
        self.m_fid = m_fid
        self.m_ssymbol = m_ssymbol
        self.m_qty = m_qty
        self.m_price = m_price
        self.m_fee = m_fee
        self.m_tdate = m_tdate
        self.m_bs = m_bs
        self.m_aid = m_aid
        self.m_sname = m_sname
        self.m_agent = m_agent
        self.m_cszip = m_cszip
        self.m_email = m_email
        self. m_phone = m_phone
        self.m_street = m_street

    def create_firm(self):
        self.m_fname = self.m_fname.replace("%", "")
        # print('firm name', self.firm_name)
        # yn=input('line 65, wait')
        cursor = self.conn.cursor()
        # this sql actually works!!!!
        sql = """INSERT INTO firms (name, street, CityStateZip, Agent, phone, email) VALUES ('%s', '%s', '%s', '%s', '%s', '%s') """
        cursor.execute(sql,(self.m_fname, self.m_street, self.m_cszip, self.m_agent, self.m_phone, self.m_email))
        self.conn.commit()

    def create_account(self):
        cursor = self.conn.cursor()

        sql = """INSERT INTO accounts (short_acct, long_acct, acct_type, fid) VALUES ('%s', '%s', '%s' '%s') """
        cursor.execute(sql, (self.sacct, self.m_lacct, self.m_acct_type, self.m_fid))
        self.conn.commit()

    def insert_stock(self):
        cursor = self.conn.cursor()
        # global g_name
        # need account index (aid)
        sql = """INSERT INTO stocks (stock_symbol, name, quantity, price, fee, trans_date, buyorsell, aid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (self.m_ssymbol, self.m_sname, self.m_qty, self.m_price, self.m_fee, self._tdate, self.m_bs, self.m_aid))
        self.conn.commit()
        return cursor.lastrowid


def main():
    muser=''
    mpwd=''
    mhost=''
    mport=0
    mfile=''

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()

    # conn = ' '
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    print(b[0])
    yn = input('stopping at line 235')
    conn = a1.create_connection()
    print('conn', conn)
    yn = input('stopping at line 238 ')

    m_acct_type = ''
    m_fname = ' '
    m_sacct = ''
    m_lacct = ''
    m_fid = 0
    m_ssymbol = ''
    m_qty = 0
    m_price = 0
    m_fee = 0
    m_tdate = ' '
    m_bs = ''
    m_aid = 0
    m_sname = ' '
    m_agent = ''
    m_cszip = ''
    m_email = ''
    m_phone = ''
    m_street = ''
    m_sid = 0

    mFind1 = Find(conn, m_acct_type, m_fname, m_sacct, m_lacct, m_fid, m_ssymbol, m_qty, m_price, m_fee, m_tdate, m_bs, m_aid, m_sname, m_agent, m_cszip, m_email, m_phone, m_street, m_sid)
    while True:

        # mFind = Find
        while True:
            answer = mFind1.find_stock()
            if answer == 1:
                print('Stock lot on file')
            elif answer == 0:
                print("stock lot not found in  database: ")
                time.sleep(2)
                Insert.insert_stock()
            elif answer == 'a':
                continue
            else:
                yn = input('[r] repeat,[q]quit')
                if yn == 'q' or yn == 'Q':
                    break

        yn = input('Use another account? (y/n)')
        if yn == 'n' or yn == 'N':
            conn.close()
            break



if __name__ == '__main__':
    main()
    os.system('clear')
