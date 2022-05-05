#!/usr/bin/env python
import MakeConnection
from os import system
from datetime import datetime



class Prices:
    def __init__(self, conn, m_cid, m_symbol, m_price, m_date):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.m_cid = m_cid
        self.m_symbol = m_symbol
        self.m_price = m_price
        self.m_date = m_date

    # noinspection SqlResolve
    def choose_symbol(self, conn):

        mcp = 0
        cursor = self.conn.cursor()

        while True:
            #edit price, date
            while True:
                m_symbol = input("enter stock symbol: ")
                m_symbol = '%{}%'.format(m_symbol)
                sql = "select cid, symbol, price, date from CurrentPrices  where cid = 's' " % self.m_cid
                cursor.execute(sql)
                data = cursor.fetchall()
                if len(data) == 0:
                    print("No symbol found.")
                    yn = input('wait ...')
                    continue
                else:
                    print("ID  symbol|   |price             |Date")
                    for row in data:
                        print("{a:<15}".format(a='ID'), "{}".format(row[0]), "\n",
                              "{a:<15}".format(a='Symbol'), "{}".format(row[1]), "\n",
                              "{a:<15}".format(a='Price'), "{}".format(row[2]), "\n",
                              "{a:<15}".format(a='Price'),  "{}".format(row[3]), "\n\n")
                mcp = input("Enter id:")
                if mcp:
                    return mcp
            # print('pid: ', self.mpid)


    def edit_prices(self):
        col = ''
        while True:
            cursor = self.conn.cursor()
            print("m_cid equals:", self.m_cid)
            yn = input("waiting at line 55")
            sql = """SELECT * from CurrentPrices where cid = %s""" % self.m_cid
            cursor.execute(sql)
            results = cursor.fetchone()
            print(results[1])
            yn = input('wait l 58')
            for row in results:
                self.m_cid = (row[0]),
                self.m_symbol = row([1]),
                self.m_price = row([2]),
                self.m_date = row([3])
                self.m_date = datetime.strptime(self.m_date, '%m/%d/%Y')


            print("\n1. symbol:     {}". format(self.m_symbol))
            print("\n2. price:      {}". format(self.m_price))
            print("\n3. date:       {}". format(self.m_date))

            m_column = input("Enter column number to edit (q='quit')")
            if m_column == '1':
                col = 'symbol'
            elif m_column == '2':
                col = 'price'
            elif m_column == '3':
                col = 'date'
            elif m_column == 'Q' or m_column == 'q':
                break

            mnewdata = input("Enter new value: ")
            if m_column == '3':
                mnewdata = datetime.strptime(mnewdata, '%m/%d/%Y')
            # sql = "UPDATE CurrentPrices SET price = %s WHERE cid = $s"
            # val = (mnewdata, col)
            # this won't work with date!'
            cursor.execute("""UPDATE CurrentPrices set {}=%s WHERE cid = %s""".format(col), (mnewdata, self.m_cid))
            self.conn.commit()


    def insert_prices(self):
        # fixup symbol
        self.m_symbol = input('Enter stock symbol: ')
        self.m_symbol = self.m_symbol.replace("%", "")
        print('m_symbol: ', self.m_symbol )
        # fixup date
        m_date = input('Enter date: MM/DD/YYYY ')
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

    def show_prices(self):
        # show prices for selected symbol

        m_symbol = input('l122 enter symbol: ')
        """ find firm name, if already in firm table"""
        cursor = self.conn.cursor()
        m_symbol = '%' + m_symbol + '%'
        sql = """ SELECT cid, symbol, price, date FROM CurrentPrices WHERE symbol LIKE '%s' """ % m_symbol
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("ID-----SYMBOL--PRICE--DATE")
        for row in rows:
            print("{}".format(row[0]), "    ", "{0:<6}".format(row[1]), "{0:.3f}".format(row[2]), "{0:%m/%d/%Y}".format(row[3]))

        yn = input("Edit, Add, or Quit (E/A/Q): ")
        if (yn == 'E' or yn == 'e'):
            self.m_cid = row[0]
            self.m_symbol = row[1]
            self.m_price = row[2]
            self.m_date = row[3]
            self.edit_prices()
            # return 'E'


        elif( yn == 'A' or yn == 'a'):
            self.insert_prices()
            return 'A'
        elif(yn == 'Q' or yn == 'q'):
            return 'Q'

def main():
    # a = 35
    # d = ''

    m_cid = ' '
    m_symbol = ' '
    m_price =' '
    m_date = ' '
    # mindex = 0
    # mysql connection
    conn = MakeConnection.get_config()
    # print('Line 141 def main', conn)
    mpid = 0
    p = Prices(conn, m_cid, m_symbol, m_price, m_date)
    # yn = input('l137: ')
    mp = p.show_prices()

    if (type(mp) == str):
        m_cid = int(mp)
        mp = 'E'
        print('l154 m_cid, type(m_cid: )', m_cid, type(m_cid))
    else:
        print('type(mp), mp', type(mp), mp)
    yn = input('l157 waiting...')
# start 1st loop
    while True:
        if  mp == 'E':
            p.edit_prices()
        elif mp == 'A':
            p.insert_prices()
        elif (mp == 'Q' or mp == 'q'):
            print('mp: ', mp)
            yn = input('l167, waiting...')
            break
        else:
            p.edit_prices()
       #  mp = p.show_prices()




# quit or continue?



if __name__ == '__main__':
    main()
    system('clear')
