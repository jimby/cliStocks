#!/usr/bin/env python
import MakeConnection
from os import system
import datetime


class Prices:
    def __init__(self, conn, mpid):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.mpid = mpid

    # noinspection SqlResolve
    def choose_symbol(self, conn):

        mcp = 0
        cursor = self.conn.cursor()

        while True:
            #edit price, date
            while True:
                m_symbol = input("enter stock symbol: ")
                m_symbol = '%{}%'.format(m_symbol)
                sql = "select distinct cp.cid, cp.symbol, cp.price, cp.date from CurrentPrices cp where cp.symbol like 's' " % m_symbol
                cursor.execute(sql)
                data = cursor.fetchall()
                if len(data) == 0:
                    print("No symbol found.")
                    yn = input('wait ...')
                    continue
                else:
                    print("ID  symbol|   |price             |Date")
                    for row in data:
                        print("{a:<15}".format(a='ID'),"{}".format(row[0]), "\n",
                                "{a:<15}".format(a='Symbol'), "{}".format(row[1]), "\n",
                                "{a:<15}".format(a='Price'), "{}".format(row[2]), "\n",
                                "{a:<15}".format(a='Price'),  "{}".format(row[3]), "\n\n")
                mcp = input("Enter id:")
                if mcp:
                    return mcp
            # print('pid: ', self.mpid)


    def edit_prices(self, mp):
        while True:
            cursor = self.conn.cursor()

            sql = """SELECT * from prices where pid = '%s'""" % self.mpid
            cursor.execute(sql)
            results = cursor.fetchone()
            if results is not None:
                print("ID ---SYMBOL----DATE----PRICE ")
            else:
                yn = ('Empty table...')
                return
            while results is not None:
                self.mpid = int(results[0])
                self.msymbol = results[1]
                # "{0:%m/%d/%Y}",format(results[2])
                self.meffective_date = results[2]
                self.mprices = results[3]
                # self.msid = results[4]

            print("\npid:          {:7.2f}".format(self.mpid))
            print("symbol =   {0:<6}".format(self.msymbol))
            print("sid =      {} ".format(self.msid))
            # print("1) name =       {}".format(self.mname))
            print("\n1) date =     {0:%m/%d/%Y}".format(self.meffective_date))
            print("2) price =    {0:7.2f}".format(self.mprices))

            # print("6) email =      {}".format())
            mcolumn = input("Enter column number to edit (q=quit)")

            # choose fields to edit
            # if mcolumn == '1':
            #    col = 'name'
            if mcolumn == '1':
                col = 'effective_date'
            elif mcolumn == '2':
                col = 'prices'
            # elif mcolumn == '4':
            #     col = 'Agent'
            # elif mcolumn == '5':
            #     col = 'phone'
            # elif mcolumn == '6':
            #    col = 'email'
            elif mcolumn == 'q' or mcolumn == 'Q':
                break

            # get and insert values
            mnewdata = input("Enter new value: ")
            sql = "UPDATE test_prices SET prices = %s WHERE pid = $s"
            val = (mnewdata, col)
            cursor.execute("""UPDATE test_prices set {}=%s where pid=%s""".format(col), (mnewdata, self.mpid))
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
        m_symbol = input('l120 enter symbol: ')
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
            E = input("Enter ID to edit: ")
            E = int(E)
            print(type(E), E)
            yn = input('Waiting l135')
            return E                                # <- not returning to main
        elif( yn == 'A' or yn == 'a'):
            return 'A'
        elif(yn == 'Q' or yn == 'q'):
            return 'Q'

def main():
    a = 35
    print('l145',type(a))
    # mysql connection
    conn = MakeConnection.get_config()
    # print('Line 141 def main', conn)
    mpid = 0
    p = Prices(conn, mpid)
    # yn = input('l137: ')
    mp = p.show_prices()
    print('l150, MP', mp)
    yn = input('l151 waiting...')
# start 1st loop
    while True:
        if type(mp) == "<class 'int'>":
            print('hurrah')
            p.edit_prices()
        elif mp == 'A':
            p.insert_prices()
        elif (mp == 'Q' or mp == 'q'):
            print('mp: ', mp)
            yn = input('l162, waiting...')
            break
        else:
            p.edit_prices(mp)
        mp = p.show_prices()




# quit or continue?



if __name__ == '__main__':
    main()
    system('clear')
