#!/usr/bin/env python
# insert_dividends.py
from mysql.connector import (connection)


def create_connection(db_user, db_pwd, db_host, db_file):
    try:
        conn = connection.MySQLConnection(user=db_user, password=db_pwd, host=db_host, database=db_file)
        cursor = conn.cursor()
        return conn
    except Exception as e:
        print(e)
        return None


def find_account(conn, account_number):
    """ find firm name, if already in firm table"""
    cursor = conn.cursor()
    cursor.execute("SELECT aid, short_acct FROM accounts WHERE short_acct LIKE %s", ('%' + account_number + '%',))
    data = cursor.fetchall()
    print('AID-- ACCT#')

    if len(data) == 0:
        print('no account number found')
    else:
        for row in data:
            print(row)

    # show user data
    maid = input('Enter AID here: ')
    return maid


def find_stock(conn, aid,  stock_symbol):

    """ find firm name, if already in from table"""

    msymbol = '%' + msymbol + '%'

    cursor = conn.cursor()

    cursor.execute(
        "select sid, aid, quantity, stock_symbol, name, price, trans_date, buyorsell from stocks where aid = %s  and stock_symbol = %s" % (aid, stock_symbol,))
    answer = cursor.fetchall()
    print('SID-AID--QTY-SYMBOL-NAME-------------------PRICE-----DATE----------------------BUY/SELL')
    if len(answer) == 0:
        print('no stock symbol found')
        return 0
    else:
        for row in answer:
            print(row)
    msid = input("Select sid:")
    return msid

def update_dividend(conn, maid, msid):

    cursor = conn.cursor()
    t = input("line 58")
    sql ="""select d.did, a.short_acct, s.quantity,s.stock_symbol,d.share_dividend, d.settle_date from accounts a, stocks s, dividends d where a.aid=s.aid and s.sid = d.sid"""
    cursor.execute(sql)
    t = input("line 61")
    print("DivID--acct---qty--symbol---div/share-----SettleDate")
    # print("account--s.sid-qty--symbol--d.did-iishares---date div")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    mdid = input("Select dividend-id (did): ")
    mdividend = input("Enter new dividend per share:")
    mdate = input("Enter the settlement date:")

    cursor.execute("""UPDATE dividends SET  share_dividend = %s, settle_date = %s WHERE did= %s """, (mdividend, mdate, mdid, ))

    sql = """SELECT d.did,a.short_acct, s.quantity, s.stock_symbol,  d.share_dividend, d.settle_date from accounts a, stocks s, dividends d where s.sid=d.sid"""
    cursor.execute(sql)
    print("DivID--acct---qty--symbol---div/share-----SettleDate")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    yn = input("this is is your edited dividend file")
    conn.commit()
    yn = input('[C]ontinue or [q]uit?')
    if yn == 'q':
        return



def main():
    # connecto to database
    db_user = 'jim'
    db_pwd = 'ttaskk'
    db_host = '192.168.1.105'
    db_file = "stocks"
    conn = create_connection(db_user, db_pwd, db_host, db_file)
    while True:
        # find account number
        while True:
            # find account index number
            account_number = input("Enter account number: ")
            maid = find_account(conn, account_number)



            yn = input('find another acct? (y/n): ')
            if yn == 'y':
                continue
            elif yn == 'n':
                break

        # find symbol for this account
        while True:
            msymbol = input('Enter symbol:')
            msid = find_stock(conn, maid, msymbol)
            if not msid:
                continue

            update_dividend(conn, maid, msid)

        yn = input('repeat or quit r/q?  ')
        if yn == 'r':
            continue
        elif yn == 'q':
            conn.commit()
            cursor.close()
            conn.close()
            break


if __name__ == '__main__':
    main()
