#!/usr/bin/env python
# insert_stocks.py

import MakeConnection
import time
#noinspection PyUnresolvedReferences
import datetime

g_name = ''
# global yn

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        print("wrong date", date_text)
        return 0

def find_account(conn):
    msg = "account"
    """ find firm name, if already in firm table"""
    while True:
        cursor = conn.cursor()
        val1 = input("Enter account number: ")
        val1 = '%'+val1+'%'

        # print(val1)
        sql = """SELECT aid, long_acct FROM test_accounts WHERE long_acct LIKE '%s' """ % val1
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) > 0:
            sfound = 1
        elif len(data) == 0:
            sfound = 0

        if sfound == 1:
            for row in data:
                print(row)
            # answer = input("Do you see your "+msg+" here (y/n)")
            # if answer == 'y' or answer == 'Y':
            val = input("enter account index number (AID): ")
            return val


def find_stock(conn, aid):
    """ find aid, stock_symbol, if already in stocks table"""
    # print("aid,stock_symbol", aid, stock_symbol)
    while True:
        cursor = conn.cursor()
        m_aid = aid
        m_symbol = input("Enter symbol : ")
        m_symbol = '%{}%'.format(m_symbol)

        sql = """SELECT s.sid, a.short_acct, s.quantity,s.price,s.stock_symbol name,s.trans_date, a.long_acct\
           FROM (test_stocks s inner join test_accounts a on s.aid = a.aid) WHERE stock_symbol LIKE '%s' """ % m_symbol

        cursor.execute(sql, (m_symbol))
        data = cursor.fetchall()

        if len(data) > 0:
            sfound = 1
        elif len(data) == 0:
            sfound = 0

        if sfound == 1:
            print("SID ACCT QTY     PRICE  SYMBOL DATE    ACCOUNT")
            for row in data:
                print("{}".format(row[0]),  "{}".format(row[1]), "{0:.3f}".format(row[2]), "{0:.3f}".format(row[3]),\
                      "{}".format(row[4]), "   ", "{:%m/%d/%Y} ".format(row[5]), "{}".format(row[6]))

            answer = input("\nIf you see your stock lot here, or search again, or no, enter (y/a/n)")

            if answer == 'y' or answer == 'Y':
                return 1
            elif answer == 'N' or answer == 'n':
                return 0    
            elif answer == 'A' or answer == 'a':
            	return 'a'
        elif sfound == 0:
            return 0                                     # symbol


def insert_stock(conn, aid):
    cursor = conn.cursor()
    global g_name
    m_symbol = input("Add lot- Enter symbol again:")
    if g_name:
        print("name: ", g_name)
        yn = input("ok? (y/n)")
        if yn == 'y' or yn == 'Y':
            m_name = g_name
        else:
            m_name = input("Enter stock name: ")
            g_name = m_name
    else:
        m_name = input("Enter stock name: ")
        g_name = m_name

    m_quantity = input("Enter original quantity: ")
    m_cost = input("Enter unit cost: ")
    m_fee = input("Enter commission or fee: ")
    if m_fee is None:
        m_fee = 0

    while True:
        # t = 1
        m_date= input("Enter date (YYYY-MM-DD): ")
        t = validate(m_date)
        if t:
            break

    # val6 = input("Enter date of transaction (YYYY-MM-DD): ")
    m_bs = input("Is this a buy or sell (buy/sell) ?: ")
    m_aid = aid

    sql = """INSERT INTO test_stocks (stock_symbol, name, quantity, price, fee, trans_date, buyorsell, aid)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (m_symbol, m_name, m_quantity, m_cost, m_fee, m_date, m_bs, m_aid))
    conn.commit()
    return cursor.lastrowid


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
            answer = find_stock(conn, maid)
            if answer == 1:
                print('Stock lot on file')
            elif answer == 0:
                print("stock lot not found in  database: ")
                time.sleep(2)
                insert_stock(conn, maid)
            elif answer == 'a':
                continue
            else:
                yn = input('[r] repeat,[q]quit')
                if yn == 'q' or yn == 'Q':
                    break

        yn = input('Use another account? (y/n)')
        if yn == 'n' or yn == 'N':
            conn.close()
            break


if __name__ == '__main__':
    main()
