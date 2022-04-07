#!/usr/bin/env python
import MakeConnection
import os
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("malformed date entry", date_text)
        return 0


class FindAcct:
    cursor = ''
    macct = ''

    def __init__(self, conn):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn

    def find_acct(self, conn):
        cursor = self.conn.cursor()

        while True:
            # macct = input("enter account ")
            # macct = '%{}%'.format(macct)
            os.system('clear')
            sql = "SELECT a.aid, a.short_acct, f.name FROM accounts a, firms f  WHERE a.fid = f.FID"  # " like '%s' AND f.FID=a.fid" % macct"

            try:

                cursor.execute(sql)
                results = cursor.fetchall()
                print("AID | account| firm name")
                for row in results:
                    print("{:3d}".format(row[0]), "{:^8s}".format(row[1]), "{:>15s}".format(row[2]))
                manswer = input("Enter account id ")
                print("id: ", manswer)
                yn = input('wait')
                return manswer
            except:
                print('error: unable to find data')
                yn = input('line 33')
                return 0

#EditPrices
class EditPrices:
    def __init__(self, mvar, conn, mpid, msymbol, meffective_date, mprices, msid):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn
        self.mpid = mpid
        self.msymbol = msymbol
        self.meffective_date = meffective_date
        self.mprices = mprices
        self.msid = msid

    # noinspection SqlResolve
    def find_prices(self):

        """ find aid, stock_symbol, if already in stocks table"""
        manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.msymbol = input("enter stock symbol: ")
        self.msymbol = '%{}%'.format(self.msymbol)

        #  sql = """SELECT tp.pid, tp.symbol, tf.name, ta.long_acct, ts.quantity, ts.name, tp.effective_date, tp.prices
        # from test_prices tp
        # INNER JOIN test_stocks ts on ts.sid = tp.sid
        # INNER JOIN test_accounts ta on ta.aid = ts.aid
        # INNER JOIN test_firms tf on tf.FID = ta.fid
        sql = """select pid, symbol, price, date from Prices where symbol like '%s'""" % self.msymbol

        # WHERE tp.symbol LIKE '%s' ORDER BY tp.symbol ASC""" % self.msymbol

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("PID|   |symbol   Price             |Date")
            for row in results:
                print("{0:<5}".format(row[0]), "{0:<10}".format(row[1]), "{0:<10}".format(row[2]),
                      "{0:10}".format(row[3]),
                      "{0:>10}".format(row[4]))

            self.mpid = input("Enter id or quit: (q)?")
            return self.mpid
            # print('pid: ', self.mpid)
        except Exception as e:
            print("l83 Error: no data")
            return 0

    def edit_prices(self):
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

##InserPrices
class Insert:
    def __init__(self, conn, m_symbol ,m_effective_date, m_price, m_sid):
        self.conn = conn
        self.m_symbol = m_symbol
        self.m_effective_date = m_effective_date
        self.m_price = m_price
        self.m_sid = m_sid

    def insert_price(self, m_symbol, m_effective_date, m_price, m_sid):
        print("1121 m_sid: ", m_sid)
        yn = input("waiting at line 122")

        cursor = self.conn.cursor(buffered=True)

        # print("symbol: ", m_symbol)
        self.m_symbol = m_symbol
        self.m_price = input("Enter current stock price:  ")
        # self.m_effective_date = input("Enter date of new price (YYYY-MM-DD): ")
        self.m_sid = m_sid

        while True:
            self.m_effective_date = input("Enter date of price (YYYY-MM-DD) : ")
            t = validate(self.m_effective_date)
            if t:
                break

        print("m_symbol", self.m_symbol)
        print("price: ", self.m_price)
        print("date: ", self.m_effective_date)
        print("stock index #: ", self.m_sid)

        yn= input("waiting at line 125")
        # noinspection SqlResolve
        sql = """INSERT INTO test_prices (symbol, effective_date, prices, sid ) VALUES (%s, %s, %s, %s)"""
        params = (self.m_symbol, self.m_effective_date, self.m_price, self.m_sid)
        cursor.execute(sql, params)
        self.conn.commit()

        # self.m_fid = int(cursor.lastrowid)
        # return self.m_fid






class Report:
    def __init__(self, conn, maid):
        self.conn = conn
        self.maid = maid

    def report(self):
        cursor = self.conn.cursor()
        print(self.maid)
        sql = """select p.effective_date, s.trans_date, a.long_acct, s.name, p.symbol, \
            (100 * ((p.prices - s.price) / s.price) / (DATEDIFF(p.effective_date, s.trans_date) / 365.25)) as APR from\
            ((stocks s inner join accounts a on s.aid=a.aid) inner join prices p on s.sid=p.sid) where s.aid = '%s'\
            order by NAME asc;""" % self.maid
        cursor.execute(sql)
        rows = cursor.fetchall()
        # print(rows.rowcount())
        print("Bought-------Latest-----Acct------Name-------Symbol----------------APR")
        for row in rows:
            print("{:%m/%d/%Y}".format(row[0]), "{:%m/%d/%Y}".format(row[1]), row[2], "{:35s}".format(row[3]),
                  "{:4s}".format(row[4]), "{:6.2f}".format(row[5]) + '%')
            # print(row)

        # yn = input("continue?")


def main():
    conn = MakeConnection.get_config()

    fa = FindAcct(conn)

    if not conn:
        print("no connection")
    while True:
        m_aid = fa.find_acct(conn)
        # print("Aid: ", m_aid)

        rp = Report(conn, m_aid)
        rp.report()
        yn = input('quit (y/n)')

        if yn == 'y' or yn == 'Y':
            break


if __name__ == '__main__':
    main()
    os.system('clear')
    # cursor.close
    # conn.close
    # import sys
    # find_menuNew

