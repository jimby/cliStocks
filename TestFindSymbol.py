#!/usr/bin/env python
import MakeConnection
import os

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
            print('Msymbol: ', msymbol)
            
            sql = "SELECT  s.stock_symbol, a.long_acct,p.sid from stocks s INNER JOIN prices p ON p.sid = s.sid INNER JOIN accounts a on a.aid = s.aid  WHERE s.stock_symbol LIKE '%s' ORDER BY  s.name ASC" % msymbol
             
            # sql = "SELECT s.sid, s.stock_symbol, s.name, s.price, a.long_acct, p.prices from prices p, stocks s,  accounts a where s.aid = a.aid and s.stock_symbol like '%s' "   %  msymbol
            
            
            cursor.execute(sql)

            data = cursor.fetchall()

            if len(data) == 0:
                print("No symbol found")
                
            print("\n{a:<4}".format(a='stock id:'),"{a:<15}".format(a='symbol:'),"{a:<10}".format(a='name:'),"                      {a:<15}".format(a='buy price:'),"{a:<15}".format(a='current price:'),"{a:<15}".format(a='account:'),"{a:<15}".format(a='settled:'))
   
            for row in data:
                # print("{a:<4}".format(a='stock id:'),"{a:<15}".format(a='symbol:'),"{a:<10}".format(a='name:'),"                   {a:<15}".format(a='buy price:'),"{a:<15}".format(a='current price:'),"{a:<15}".format(a='account:'),"{a:<15}".format(a='settled:'))
                print(
                    "\n{}".format(row[0]),        
                    "{}".format(row[1]),
                    "{}".format(row[2]))
                    
                    
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
    
    # cursor.close
    # conn.close
    # import sys
    # find_menuNew

