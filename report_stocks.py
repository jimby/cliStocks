#!/usr/bin/env python
from mysql.connector import (connection)
import configparser

class MakeConnection:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
        #     self.name = name    # instance variable unique to each instance
        self.muser = muser
        self.mpwd = mpwd
        self.mhost = mhost
        self.mport = mport
        self.mfile = mfile


    def create_connection(self):
        try:
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport, database=self.mfile)
            cursor = conn.cursor()
            print("connected")
            return conn
        except Exception as e:
            print("no connection")
            return e

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.muser = config['DEFAULT']['muser']
        self.mpwd = config['DEFAULT']['mpwd']
        self.mhost = config['DEFAULT']['mhost']
        self.mport = config['DEFAULT']['mport']
        self.mfile = config['DEFAULT']['mfile']

        b = [self.muser, self.mpwd, self.mhost, self.mport, self.mfile]
        return b

class Find:
    def __init__(self, conn, m_find1, maid):
        self.conn = conn
        self.m_find1 = m_find1
        self.maid = maid
        
    def find_account(self):
        try:

            cursor = self.conn.cursor()

            # m_aid = m_aid + ' collate utf8mb_general_ci'
            sql = """SELECT accounts.aid, accounts.short_acct FROM accounts"""
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()
            self.m_find1 = input("If you see your account number, enter index number, else enter 0...")
        except:
            print("undetermined error")
        finally:
            return self.m_find1

    def find_stock(self):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("l92 find stock lot...")

        while True:

            try:

                cursor = self.conn.cursor()
                # print('conn: ',self.conn)
                # print('cursor: ', cursor)
                self.m_find1 = input("l132 Enter symbol : ")
                self.m_find1 = '%{}%'.format(self.m_find1)

                # print("l103, m_aid: ", m_aid)
                # print("104, symbol: ", self.m_find1)
                # yn = input("waiting at line 104")

                # sql = """SELECT s.sid, a.long_acct, s.quantity,s.price,s.stock_symbol, s.name,s.trans_date,
                #     FROM stocks s inner join accounts a on a.aid = s.aid WHERE s.stock_symbol like '%WMT%' AND s.aid = 1"""

                sql = "select s.sid, a.long_acct, f.name, s.quantity, s.price, s.stock_symbol, s.name, s.trans_date" \
                      "  from stocks s, accounts a, firms f  where s.aid=a.aid and  a.fid=f.FID and s.stock_symbol like %s and s.aid = %s "        # where stock_symbol like  %s and aid = %s "
                cursor.execute(sql, (self.m_find1, self.maid))
                format = "%m/%d/%Y"
                # print('cursor#2: ', cursor)
                row = cursor.fetchone()
                print('sid---acct--company-------------qty-----price---symbol-----name---------------------------date------')

                while row is not None:
                    print("{0:<5}".format(row[0]),"{0:<5}".format(row[1]), "{0:<15}".format(row[2]), "{0:>10}".format(row[3]), "{0:>8}".format(row[4]), "{0:<5}".format(row[5]), "{0:<35}".format(row[6]), "{0:%m/%d/%Y}".format(row[7]))
                    row = cursor.fetchone()
                # print("row:", row)
                self.m_find1 = input("do you see your stock lot here (y/n)")
            except :
                print('error...')
            finally:
                # cursor.close()
                return self.m_find1



# def report(conn):
#     cursor = conn.cursor()
#
#     sql = """select p.date as 'date', s.name, p.symbol, s.quantity, a.long_acct, \
#     s.price as cost, p.price as 'current price', concat(format(100 * ((p.price - s.price) / s.price), 1), '%') \
#     as 'gain' from accounts a, stocks s, prices p where a.aid = s.aid and s.sid = p.sid order by a.aid, s.sid, \
#     s.quantity, p.date; """
#
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)


def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    conn = ' '
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # class Find
    m_var = ' '

    f1 = Find(conn, m_var)


#     while True:
#         report(conn)
#
#         yn = input("quit? (y/n)? ")
#         if yn == 'y' or yn == 'Y':
#             break
    while True:
        # maid = f1.find_account()
        # print(m_aid)
        # m_aid = int(m_aid)

        yn = f1.find_stock()
        if yn == 'Y' or yn == 'y':
            yn = input("Do you want to search for more lots?")
            if yn == 'Y' or yn == 'y':
                continue
        # else:
        #     yn = input("Do you want to add another lot of  stocks? (y/n")

        if yn == 'N' or yn == 'n':
            break
    # find, insert account number
        # while True:
        #     m_sid = i1.insert_stock(m_aid)
        #     # print('m_aid: ', m_aid)
        #
        #     yn = input("Continue (y/n)?")
        #     if yn == 'y' or yn == 'Y':
        #         break
        #     else:
        #         return


if __name__ == '__main__':
    main()
