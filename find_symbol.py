# import sys
from mysql.connector import (connection)
import configparser
# import os


class MakeConnection:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
        #     self.name = name    # instance variable unique to each instance
        self.muser = muser
        self.mpwd = mpwd
        self.mhost = mhost
        self.mport = mport
        self.mfile = mfile

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        muser = config['DEFAULT']['muser']
        mpwd = config['DEFAULT']['mpwd']
        mhost = config['DEFAULT']['mhost']
        mport = config['DEFAULT']['mport']
        mfile = config['DEFAULT']['mfile']
        b = [muser, mpwd, mhost, mport, mfile]
        return b

    def create_connection(self):
        try:
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport,
                                              database=self.mfile)
            cursor = conn.cursor()
            print("connected")
            return conn
        except Exception as e:
            print("no connection")
            return e




class FindStock:

    def __init__(self, conn, msymbol):
        self.conn = conn
        self.name = msymbol    # instance variable unique to each instance

    def find_stock(self):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("aid,stock_symbol", aid, stock_symbol)
        msymbol = input("Symbol: ")
        msymbol = '%{}%'.format(msymbol)
        if msymbol == "%%":
            return
        cursor = self.conn.cursor()
        sql = """SELECT a.long_acct, s.stock_symbol,s.quantity,s.name, s.price,p.prices, s.trans_date,
         p. effective_date,s.lot_number FROM accounts a, stocks s, prices p where a.aid= s.aid and s.stock_symbol=p.symbol and
           s.stock_symbol like '%s' """ % msymbol

        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            return 0
        else:
            print("Acct------------Firm---Qty---Name--------------------------------buy $----current $--buy DATE---currentdate-GAIN")
            for row in data:
                print( "{:<15s}".format(row[0]),"{0:5}".format(row[1]), "{:6.2f}".format(row[2]), "{0:35}".format(row[3]),
                      "{:6.2f}".format(row[4]), "{:8.2f}".format(row[5]),
                      "{:%m/%d/%Y}".format(row[6]),"{:%m/%d/%Y}".format(row[7]), "{:6.1f}".format((100*(row[5]-row[4])/row[4])), "%", row[8])
            cursor.close()




def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    conn = ' '

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()

    a1 = MakeConnection(b[0], b[1], b[2] , b[3], b[4])
    conn = a1.create_connection()

    msymbol = ''
    f1 = FindStock(conn, msymbol)
    # class FindStock



    while True:
        f1.find_stock()
        yn = input('Continue (y/n)')
        if yn == 'n' or yn == 'Y':
            break
        # elif yn == "R" or yn == "r":
        #     print("return to find_menu")
            # importlib.import_module('menuNew')
            # import menuNew
            #     t = menuNew.main()



if __name__ == '__main__':
    main()
