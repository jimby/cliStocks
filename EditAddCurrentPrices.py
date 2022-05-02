#!/usr/bin/env python
import MakeConnection
from os import system
import datetime


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
                sql = "select cid, symbol, price, date from CurrentPrices  where cid like 's' " % self.m_index
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
        while True:
            cursor = self.conn.cursor()
            sql = """SELECT * from prices where cid = '%s'""" % self.m_cid
            cursor.execute(sql)
            results = cursor.fetchone()

            for row in results:
                self.mcid = int(results[0])
                self.m_symbol = results([1])
                self.m_date = results([2])
                self.m_price = results([3])

            print("\nID:        {}".format(self.m_cid))
            print("\n1. symbol:    {}". format(self.m_symbol))
            print("\n2. price:     {}". format(self.m_price))
            print("\n3. date:      {}". format(self.m_date))

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
            sql = "UPDATE CurrentPrices SET price = %s WHERE cid = $s"
            val = (mnewdata, col)
            cursor.execute("""UPDATE CurrentPrices set {}=%s WHERE cid = %s""".format(col), (mnewdata, self.m_cid))
            self.conn.commit()


    def insert_prices(self):
        # fixup symbol
        m_symbol = input('Enter stock symbol: ')
        m_symbol = m_symbol.replace("%", "")
        print('m_symbol: ',m_symbol )
        # fixup date
        m_date = input('Enter date: MM/DD/YYYY ')
        month, day, year = map(int, m_date.split('/'))
        m_date = datetime.date(year, month, day)
        print('m_date: ', m_date)

        m_price = input('Enter price:')
        print('m_price: ', m_price)
        yn = input('waiting at line 109')

        cursor = self.conn.cursor()
        # this sql actually works!!!!
        sql = """INSERT INTO CurrentPrices (symbol, price, date) VALUES (%s, %s, %s) """
        cursor.execute(sql, (m_symbol, m_price, m_date))
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
            E = input('Enter symbol ID: ')
            str = 'E'
            return E                                # <- not returning to main
        elif( yn == 'A' or yn == 'a'):
            return 'A'
        elif(yn == 'Q' or yn == 'q'):
            return 'Q'

def main():
    a = 35
    d = ''
    mindex = 0
    # mysql connection
    conn = MakeConnection.get_config()
    # print('Line 141 def main', conn)
    mpid = 0
    p = Prices(conn, mindex)
    # yn = input('l137: ')
    mp = p.show_prices()
    print('l155, MP', mp)
    yn = input('l56',' wait')
    print('l156 type mp', type(mp))
    if (type(mp) == str):
        index = int(mp)
        mp = 'E'
        print('index: ', index)
        print('mp: ', mp)
        print('type(index', type(index))
        print('type(mp)', type(mp))
    yn = input('l163 waiting...')
# start 1st loop
    while True:
        if  mp == 'E':
            p.edit_prices(index)
        elif mp == 'A':
            p.insert_prices()
        elif (mp == 'Q' or mp == 'q'):
            print('mp: ', mp)
            yn = input('l167, waiting...')
            break
        else:
            p.edit_prices(mp)
       #  mp = p.show_prices()




# quit or continue?



if __name__ == '__main__':
    main()
    system('clear')
