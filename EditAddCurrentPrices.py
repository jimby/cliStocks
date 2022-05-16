#!/usr/bin/env python
import MakeConnection
from os import system
from datetime import datetime
import getpass


class Prices:

    def __init__(self, conn, m_cid, m_symbol, m_price, m_date):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.m_cid = m_cid
        self.m_symbol = m_symbol
        self.m_price = m_price
        self.m_date = m_date

# enter symbol
    # get index
    # edit
    # insert
    def choose_symbol(self):
        while True:
            print('\n\nChoose stock symbol')
            m_symbol = input("enter stock symbol [Q]uit: ")
            if m_symbol == 'Q' or m_symbol == 'q':
                return
            m_symbol = '%{}%'.format(m_symbol)
            mindex = 0
            cursor = self.conn.cursor()
            #edit price, date

# get stock symbol
            sql = """select cid, symbol, price, date from CurrentPrices  where symbol like '%s' """ % m_symbol
            cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) == 0:
                print("No symbol found.")           # add stocks
                print('Add Symbol (A) or try again (T): ?')
                yn = input('wait ...')
                if yn == 'A' or yn == 'a':
                    self.insert_prices()
                elif yn == 'T' or yn == 't':
                    break

            print("ID  symbol|   |price             |Date")

            for row in data:
                  print("{}".format(row[0]), "{}".format(row[1]), "{}".format(row[2]), "{}".format(row[3]), "\n\n")
                  mindex = input("Enter id:")

            yn = input('Choose (E)dit, (A)dd record, or (Q)uit (E/R/Q): ')
            if yn == 'E' or yn == 'e':
                self.edit_prices(mindex)
            elif yn == 'A' or yn == 'a':
                self.insert_prices()
            if yn == 'Q' or yn == 'q':
                break

    def insert_prices(self):
        # fixup symbol
        print('Add prices\n')
        self.m_symbol = input('Enter stock symbol: ')
        self.m_symbol = self.m_symbol.replace("%", "")
        print('m_symbol: ', self.m_symbol)
        # fixup date
        self.m_date = input('Enter date: MM/DD/YYYY ')
        self.m_date = datetime.strptime(self.m_date, '%m/%d/%Y')
        print('m_date: ', self.m_date)

        self.m_price = input('Enter price:')
        print('m_price: ',self.m_price)
        yn = input('waiting at line 109')

        cursor = self.conn.cursor()
        # this sql actually works!!!!
        sql = """INSERT INTO CurrentPrices (symbol, price, date) VALUES (%s, %s, %s) """
        cursor.execute(sql, (self.m_symbol, self.m_price, self.m_date))
        self.conn.commit()
        return

    def edit_prices(self, mindex):
        print('Edit Current prices\n')
        while True:
            print('l67 mindex: ', mindex)
            yn = input('wait...')
            cursor = self.conn.cursor()
            # print("line 53 sid: ", val)
            # val = input('Symbol :')

            sql = """SELECT cid, symbol, price, date from CurrentPrices where cid = '%s'""" % mindex
            print(sql)
            cursor.execute(sql)
            results = cursor.fetchone()
            print("results: ", results)
            print("results[1]", results[0])# fetch one

            for row in results:
                m_cid = results[0]
                m_symbol = results[1]
                m_price = results[2]
                m_date = results[3]
                # m_price = float(results[5])
                # m_fee = float(results[6])
                # m_trans_date = results[7]
                # m_bs = results[8]
                # m_aid = int(results[9])

            print("\ncid:          {}".format(m_cid))
            print("1) symbol =     {}".format(m_symbol))
            print("2) price =      {}".format(m_price))
            print("3) date =       {}".format(m_date))
            # print("4) price =      {}".format(m_price))
            # print("5) fee =        {}".format(m_fee))
            # print("6) date =       {:%b %d, %Y} ".format(m_trans_date))
            # print("7) buyorsell =  {}".format(m_bs))
            print('[Q] quit')

            mcolumn = input("\nEnter column number to edit or [q]uit")
            if mcolumn == '1':
                col = 'symbol'
            elif mcolumn == '2':
                col = 'price'
            elif mcolumn == '3':
                col = 'date'
            # elif mcolumn == '4':
            #     col = 'price'
            # elif mcolumn == '5':
            #    col = 'fee'
            # elif mcolumn == '6':
            #    col = 'trans_date'
            # elif mcolumn == '7':
            #    col = 'buyorsell'

            mnewdata = input("Enter new value [Q]uit: ")
            if mcolumn == '1':
                if not type(mnewdata) == 'str':
                    cursor.execute("""UPDATE CurrentPrices set {}=%s where cid=%s""".format(col), (mnewdata, m_cid))
                    self.conn.commit()
                    continue
            if mcolumn == '2':
                if not type(mnewdata) == 'float':
                    cursor.execute("""UPDATE CurrentPrices set {}=%s where cid=%s""".format(col), (mnewdata, m_cid))
                    self.conn.commit()
                    continue
            if mcolumn == '3':
                if not type(mnewdata) == 'datetime.datetime':
                    mnewdata = datetime.strptime(mnewdata, '%m/%d/%Y')
                    cursor.execute("""UPDATE CurrentPrices set {}=%s where cid=%s""".format(col), (mnewdata, m_cid))
                    self.conn.commit()
                    continue
            if mcolumn == 'Q' or mcolumn == 'q':
                system('clear')
                break



def main():
    # a = 35
    # d = ''

    m_cid = ' '
    m_symbol = ' '
    m_price = ' '
    m_date = ' '

    while True:
        conn = MakeConnection.get_config()
        if not conn:
            print("No connection.")
            yn = input("Try again.")
        else:
            break
    system('clear')

    p = Prices(conn, m_cid, m_symbol, m_price, m_date)
    # yn = input('l137: ')
    # mp = p.choose_symbol()
    # if mp == 'E', whereis cid??
    # start 1st loop
    p.choose_symbol()
  #  mp = p.show_prices()




# quit or continue?



if __name__ == '__main__':
    main()
    system('clear')
