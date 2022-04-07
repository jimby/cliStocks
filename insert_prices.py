#!/usr/bin/env python
import MakeConnection
import os


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

class edit:


class insert:




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

