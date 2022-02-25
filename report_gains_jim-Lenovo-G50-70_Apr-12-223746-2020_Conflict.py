#!/usr/bin/env python
# ~/SynologyDrive/stocks/report/report_gains.py
from mysql.connector import (connection)


yn = ' '


def create_connection(db_user, db_pwd, db_host, db_port, db_file):
    try:
        conn = connection.MySQLConnection(user=db_user, password=db_pwd, host=db_host, port=db_port, database=db_file)
        return conn
    except Exception as e:
        print("cannot make connection to database")

def find_account(conn):
    while True:
        cursor = conn.cursor()
        m_acct = input("Account: ")
        m_acct = '%'+m_acct+'%'
        

        # print(val1)
        sql = """SELECT aid, long_acct FROM accounts WHERE long_acct LIKE '%s' """ % m_acct
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) > 0:
            for row in data:
                print(row)													# <<<---gui
            # answer = input("Do you see your "+msg+" here (y/n)")
            # if answer == 'y' or answer == 'Y':
            val = input("enter account index number (AID): ")				# <<<--- gui
            return val
        else:
            return 0


def report(conn, maid):
    cursor = conn.cursor()
    print(maid)
    sql = """select p.effective_date, s.trans_date, a.long_acct, s.name, p.symbol, \
        (100 * ((p.prices - s.price) / s.price) / (DATEDIFF(p.effective_date, s.trans_date) / 365.25)) as APR from\
        ((stocks s inner join accounts a on s.aid=a.aid) inner join prices p on s.sid=p.sid) where s.aid = '%s'\
         order by NAME asc;""" % maid
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("Date1-------Date2-----Acct------Name-------Symbol----------------APR")
    for row in rows:
        print("{:%m/%d/%Y}".format(row[1]), "{:%m/%d/%Y}".format(row[0]), row[2],"{:35s}".format(row[3]), "{:4s}".format(row[4]), "{:6.2f}".format(row[5])+'%')
        # print(row)

def main():
    db_user = 'jim'
    db_pwd = 'ttaskk'
    db_host = '192.168.1.115'
    db_port = 3307
    db_file = "stocks"

    conn = create_connection(db_user, db_pwd, db_host, db_port, db_file)
    while True:
        maid = find_account(conn)
        while True:
            report(conn, maid)
            yn = input("quit (y/n)? ")
            if yn == 'y' or yn == 'Y':
                break
        yn = input("Try another account or quit (a/q)")
        if yn == 'q' or yn == 'Q':
            break

if __name__ == '__main__':
    main()
