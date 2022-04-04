#!/usr/bin/env python
# edit first, then if no price, insert
import MakeConnection
import os
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("L23 malformed date entry", date_text)
        return 0


class Find:
    cursor = ' '
    macct = ' '
    def __init__(self, conn):
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

    def find_symbol(self, m_aid, m_symbol):
    # def find_symbol(self, m_aid,  m_symbol, m_sid):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        # self.m_aid = m_aid
        # self.m_symbol = m_symbol
        # self.m_sid = m_sid
        m_var = 0
        while True:
            # def find_account(self):
            print("SID -SYMBOL NAME - ----------------LOT - -QTY - -PRICE")
            try:

                # m_aid = m_aid + ' collate utf8mb_general_ci'
                sql = "SELECT s.sid, s.stock_symbol, s.name, s.lot_number, s.quantity, s.price FROM stocks s WHERE s.aid LIKE %s AND s.stock_symbol LIKE %s "
                params = (self.m_aid, self.m_symbol)
                cursor.execute(sql, params)
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()
                m_sid = input("l101 If you see your stock symbol here, enter index number (sid), else enter 0...")
            except:
                print("-undetermined error")
                print("msid: ", m_sid)
                yn = input("waiting at line 85")
            finally:
                print("msid: ", m_sid)
                yn = input("waiting at line 88")
                return m_sid



class Insert:
    def __init__(self, conn, m_symbol ,m_effective_date, m_price, m_sid):
        self.conn = conn
        self.m_symbol = m_symbol
        self.m_effective_date = m_effective_date
        self.m_price = m_price
        self.m_sid = m_sid

    def insert_price(self, m_symbol, m_effective_date, m_price, m_sid):
        print("L102 m_sid: ", m_sid)
        yn = input("waiting at line 103")

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

        yn= input("waiting at line 124")
        # noinspection SqlResolve
        sql = """INSERT INTO test_prices (symbol, effective_date, prices, sid ) VALUES (%s, %s, %s, %s)"""
        params = (self.m_symbol, self.m_effective_date, self.m_price, self.m_sid)
        cursor.execute(sql, params)
        self.conn.commit()

        # self.m_fid = int(cursor.lastrowid)
        # return self.m_fid


def main(i1=None, f1=None):
    conn = MakeConnection.get_config()

    fa = Find(conn)

    if not conn:
        print("no connection")
    while True:
        m_aid = fa.find_acct(conn)
        # print("Aid: ", m_aid)

        # rp = Report(conn, m_aid)
        # rp.report()
        # yn = input('quit (y/n)')
        yn = input('L140 waiting')
        if yn == 'y' or yn == 'Y':
            break


if __name__ == '__main__':
    main()
