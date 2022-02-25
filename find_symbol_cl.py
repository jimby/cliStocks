# this is attempt to ass configparser as function in class FindFirm
# from time import strftime
from mysql.connector import (connection)
# import importlib
import configparser
from os import system, name


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



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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
        



def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()

    # muser = 'b[0]'; mpwd = 'b[1]'; mhost = 'b[2]'; mport = b[3]; mfile = 'b[4]'
    mvar = ' '
    conn = ' '
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])

    conn = a1.create_connection()

    while True:
        m_var = input("Enter symbol: ")
        m_var = '%{}%'.format(m_var)

        if not m_var:
            input("line 119")
            break
        a2 = FindStock(m_var, conn)
        a2.find_stock()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break

    # exit
    # conn.close()

if __name__ == '__main__':
    main()
    clear()
    # cursor.close
    # conn.close
    # import sys
    # find_menuNew

