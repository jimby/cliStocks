# test.py
# object-> to return a variable from a sql select sum statemment
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
            self.m_find1 = input("If you see your account number, enter index number, else enter 0...")
        except:
            print("undetermined error")
        finally:
            return self.m_find1

    def find_stock(self, m_aid):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("maid", m_aid)
        # yn = input("Waiting at line 89")

        while True:

            try:

                cursor = self.conn.cursor()

               # sql = "select s.sid, a.long_acct, f.name, s.quantity, s.price, s.stock_symbol, s.name, s.trans_date" \
               #       "  from stocks s, accounts a, firms f  where a.aid=s.aid and  f.FID = a.fid and s.aid = %s " % m_aid
               # sql = "select f.name, s.stock_symbol, a.long_acct from stocks s, account, a firms f on f.FID=a.fid order by s.stock_symbo and s.aid = %s" % m_aid
                sql = """select f.name, s.quantity,s.name, s.stock_symbol,s.price, s.trans_date, a.long_acct from stocks s , accounts a, firms f where f.FID = a.fid and a.aid = s.aid and s.aid = %s order by s.name asc""" % m_aid
                format = "%m/%d/%Y"
                cursor.execute(sql)
                row = cursor.fetchone()
                print("\n",row[0],",","acct:",row[5],"\n")
                print('qty--------name-------------------------------------symbol-price------settled')
                while row is not None:
                    print("{0:<10}".format(row[1]), "{0:<40}".format(row[2]), "{0:<6}".format(row[3]),"{0:<10}".format(row[4]), "{0:%m/%d/%Y}".format(row[5]))
                    row = cursor.fetchone()
                # print("row:", row)
                # print('cursor#2: ', cursor)
                self.m_find1 = input("continue (y/n)")
            except :
                print('puked up the champaign')
            finally:
                # cursor.close()
                return self.m_find1


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

    # find, insert firm name
    while True:
        m_aid = f1.find_account()
        # print(m_aid)
        # m_aid = int(m_aid)

        yn = f1.find_stock(m_aid)
        if yn == 'Y' or yn == 'y':
        #    yn = input("Do you want to search for more lots?")
        #    if yn == 'Y' or yn == 'y':
            continue
        else:
            # yn = input("Do you want to add another lot of  stocks? (y/n")
            break
        # if yn == 'N' or yn == 'n':
        #     break


if __name__ == '__main__':
    main()
