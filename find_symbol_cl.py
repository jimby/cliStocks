#!/usr/bin/env python
import MakeConnection
from os import system

class FindStock:
    cursor = ''
    msymbol = ''
    
    def __init__(self, conn):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn

    def find_stock(self, conn):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()

        while True:
            msymbol = input("enter symbol: ")
            msymbol = '%{}%'.format(msymbol)
            
            sql = "SELECT stocks.sid, stocks.stock_symbol, stocks.quantity, stocks.name, stocks.price, prices.prices," \
              " accounts.long_acct, prices.effective_date from prices" \
              " INNER JOIN stocks ON prices.sid = stocks.sid" \
              " INNER JOIN accounts ON stocks.aid=accounts.aid" \
              " INNER JOIN firms ON accounts.FID = firms.fid" \
              " WHERE stocks.stock_symbol LIKE '%s' ORDER BY stocks.name ASC" % msymbol

            cursor.execute(sql)

            data = cursor.fetchall()

            if len(data) == 0:
                print("No symbol found")
                
                    
            for row in data:
               print("{a:<15}".format(a='stock id:'),"{}".format(row[0]),"\n",        
                     "{a:<15}".format(a='symbol'),"{}".format(row[1]),"\n",
                     "{a:<15}".format(a='quantity:'),"{}".format(row[2]),"\n",
                     "{a:<15}".format(a='name:'),"{}".format(row[3]),"\n",
                     "{a:<15}".format(a='buy price:'),"{}".format(row[4]),"\n",
                     "{a:<15}".format(a='current price:'),"{}".format(row[5]),"\n",
                     "{a:<15}".format(a='account:'),"{}".format(row[6]),"\n",
                     "{a:<15}".format(a='settled:'),"{}".format(row[7]),"\n\n")
        
            yn = input("continue y/n")
            if (yn == 'N' or yn == 'n'):
                break
            else:
                continue
        
        cursor.close()
        # self.conn.close()
        



def main():
    
    conn = MakeConnection.get_config()
    # print("fl37 Conn: ", conn)
    
    ff = FindStock(conn)
    # ff.find_firm()
    
    if not conn:
        print("no connection fl42")

    ff.find_stock(conn)
 
if __name__ == '__main__':
    main()
    system.clear()
    # cursor.close
    # conn.close
    # import sys
    # find_menuNew

