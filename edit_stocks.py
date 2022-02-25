#!/usr/bin/env python
# edit_stocks.py
# __all__ = ['datetime']
from mysql.connector import (connection)

import datetime

# noinspection PyUnresolvedReferences
# import datetime
# global yn
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except:
        print("wrong date", date_text)
        return 0


def create_connection(conn_user, conn_pwd, conn_host, conn_port, conn_file):
    try:
        conn = connection.MySQLConnection(user=conn_user, password=conn_pwd, host=conn_host, port=conn_port, database=conn_file)
        return conn
    except Exception as e:
        print(e)
        return None


def find_stock(conn):

    """ find aid, stock_symbol, if already in stocks table"""

    # while True:
    cursor = conn.cursor()

    m_name = input("enter stock name: ")
    m_name = '%{}%'.format(m_name)

    # sql = """SELECT sid,stock_symbol,name, quantity, price, trans_date.day") \
    # as 'date',buyorsell FROM stocks"""

    sql = """SELECT s.sid, s.stock_symbol, s.name, s.quantity, s.price, s.trans_date, a.long_acct FROM (stocks s inner join accounts a on s.aid=a.aid) WHERE name like '%s' """ % m_name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("SID|symbol-|firm name--------------------|qty---|price|date------|acct")
        for row in results:
            print("{:3d}".format(row[0]), "{0:5s}".format(row[1]), "{0:30s}".format(row[2]), "{0:6.2f}".format(row[3]), "{0:6.2f}".format(row[4]), "{:%m/%d/%Y}".format(row[5]), "{}".format(row[6]))

        manswer = input("Enter sid: ")

        return manswer
    except:
        print("Error: unable to find data")


def edit_stock(db, val):

    cursor = db.cursor()
    # print("line 53 sid: ", val)
    # val = int(val)
    sql = """SELECT * from stocks where sid = '%s'""" % val
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchone()
    print("results: ", results)
    print("results[1]", results[0])# fetch one
    for row in results:
        m_sid = results[0]
        m_stock_symbol = results[1]
        m_name = results[2]
        m_qty = float(results[3])
        m_price = float(results[4])
        m_fee = float(results[5])
        m_trans_date = results[6]
        m_bs = results[7]
        m_aid = int(results[8])

    print("\nsid:          {}".format(m_sid))
    print("1) symbol =     {}".format(m_stock_symbol))
    print("2) name =       {}".format(m_name))
    print("3) quantity =   {0:.3f}".format(m_qty))
    print("4) price =      ${0:5.3f}".format(m_price))
    print("5) fee =        ${0:5.3f}".format(m_fee))
    print("6) date =       {:%b %d, %Y} ".format(m_trans_date))
    print("7) buyorsell =  {}".format(m_bs))
    mcolumn = input("\nEnter column number to edit or [q]uit")
    if mcolumn == '1':
        col = 'stock_symbol'
    elif mcolumn == '2':
        col = 'name'
    elif mcolumn == '3':
        col = 'quantity'
    elif mcolumn == '4':
        col = 'price'
    elif mcolumn == '5':
        col = 'fee'
    elif mcolumn == '6':
        col = 'trans_date'
    elif mcolumn == '7':
        col = 'buyorsell'
    elif mcolumn == 'Q' or mcolumn == 'q':
        return
    if mcolumn == 'Q' or mcolumn == 'q':
        return
        #get new values
    mnewdata = input("Enter new value: ")

        #update stocks
        #sql = """ UPDATE stocks SET `%s` = %s WHERE sid = %s"""
    cursor.execute("""UPDATE stocks set {}=%s where sid=%s""" .format(col), (mnewdata, m_sid))
        #cursor.execute(sql, (col, mnewData, sid))

    db.commit()

    # show changes




def main():
    db_user = 'jim'
    db_pwd = 'ttaskk'
    db_host = '192.168.1.115'
    db_port = 3307
    db_file = "stocks"

    conn = create_connection(db_user, db_pwd, db_host, db_port, db_file)
    while True:
        answer = find_stock(conn)
        edit_stock(conn, answer)
        yn = input("quit? (y/n)")
        if yn == 'Y' or yn == 'y':
            break

            
    conn.close()
    exit()

if __name__ == '__main__':
    main()
