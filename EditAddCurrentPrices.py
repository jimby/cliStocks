#!/usr/bin/env python
import MakeConnection
from os import system
import datetime


class EditPrices:
    def __init__(self, conn):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn

    # noinspection SqlResolve
    def FindPrices(self):

        """ find aid, stock_symbol, if already in stocks table"""
        mcp = 0
        cursor = self.conn.cursor()

        while True:
            #edit price, date
            while True:
                msymbol = input("enter stock symbol: ")
                msymbol = '%{}%'.format(self.msymbol)
                sql = "select distinct cp.cid, s.stock_symbol, cp.price, cp.date from stocks s inner join CurrentPrices cp on s.stock_symbol where s.stock_symbol like 's' " % msymbol
                cursor.execute(sql)
                data = cursor.fetchall()
                if len(data) == 0:
                    print("No symbol found.")
                    yn = input('Add symbol (y/n)? ')
                    if yn == 'Y' or yn == 'y':
                        break
                else:
                    print("ID  symbol|   |price             |Date")
                    for row in data:
                        print("{a:<15}".format(a='ID'),"{}".format(row[0]),"\n",
                                "{a:<15}".format(a='Symbol'), "{}".format(row[1]),"\n",
                                "{a:<15}".format(a='Price'), "{}".format(row[2]), "\n",
                                "{a:<15}".format(a='Price'),  "{}".format(row[3]),"\n\n"
                                                                                  "")
                mcp = input("Enter id or quit: (q)?")
            return mcp
            # print('pid: ', self.mpid)


    def EditPrices(self):
        while True:
            cursor = self.conn.cursor()

            sql = """SELECT * from prices where pid = '%s'""" % self.mpid
            cursor.execute(sql)
            results = cursor.fetchone()

            for row in results:
                # sql = """SELECT * from pricess where fid = '%s'""" % self.mpid
                # cursor.execute(sql)
                # results = cursor.fetchone()
                self.mpid = int(results[0])
                self.msymbol = results[1]
                self.meffective_date = results[2]
                self.mprices = results[3]
                self.msid = results[4]

            print("\npid:          {}".format(self.mpid))
            print("symbol =   {}".format(self.msymbol))
            print("sid =      {} ".format(self.msid))
            # print("1) name =       {}".format(self.mname))
            print("\n1) date =     {}".format(self.meffective_date))
            print("2) price =    {}".format(self.mprices))

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


class InsertPrices:

    def __init__(self, conn):
        self.conn = conn

    def insert_prices(self):
        #fixup symbol
        m_symbol = input('Enter stock symbol: ')
        m_symbol = m_symbol.replace("%", "")

        # fixup date
        m_date = input('Enter date: MM/DD/YYYY ')
        month, day, year = map(int, m_date.split('/'))
        m_date = datetime.date(year, month, day)

        m_price = input('Enter price:')

        cursor = self.conn.cursor()
        # this sql actually works!!!!
        sql = """INSERT INTO CurrentPrices (date, price, symbol) VALUES ('%s', 's', 's') """ % m_date, m_price, m_symbol
        cursor.execute(sql)
        self.conn.commit()

    def show_prices(self):
        # show prices for selected symbol
        """ find firm name, if already in firm table"""
        cursor = self.conn.cursor()
        self.firm_name = '%' + self.firm_name + '%'
        sql = """ SELECT fid, name FROM firms WHERE name LIKE '%s' """ % self.firm_name
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("ID-----FIRM NAME")
        for row in rows:
            print("{}".format(row[1]), "    ", "{}".format(row[0]))

        yn = input("Do you see your firm here ? (q=quit):")
        if yn == 'N' or yn == 'n':
            return yn



def main():
    # mysql connection
    conn = MakeConnection.get_config()
    e1 = EditPrices(conn)



    while True:
        # m_var = input("prices: ")
        # m_var = '%{}%'.format(m_var)

        # if m_var == "%%":
        #     print("line 92, %%")
        #     break


        system('clear')
    conn.close()


if __name__ == '__main__':
    main()
    system('clear')
