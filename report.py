#!/usr/bin/env python
# insert_prices.py
import datetime
from typing import Any, Tuple, Union

from mysql.connector import (connection)


yn = ' '


def create_connection(db_user, db_pwd, db_host,db_port, db_file):
    try:
        conn = connection.MySQLConnection(user=db_user, password=db_pwd, host=db_host,db_port, database=db_file)
        cursor = conn.cursor()
        return conn
    except Exception as e:
        print(e)
        return None


def report(conn):
    cursor = conn.cursor()

    sql = """select date_format(p.effective_date,"%m/%d/%Y") as 'date', s.name, p.symbol, s.quantity, a.long_acct, \
    s.price as cost, p.prices as 'current price', concat(format(100 * ((p.prices - s.price) / s.price), 1), '%') \
    as 'gain' from accounts a, stocks s, prices p where a.aid = s.aid and s.sid = p.sid order by a.aid, s.sid, \
    s.quantity, p.effective_date; """

    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    db_user = 'jim'
    db_pwd = '8uhb(IJN'
    db_host = '192.168.1.115'
    db_port = 3307
    db_file = "stocks"

    conn = create_connection(db_user, db_pwd, db_host,db_port, db_file)

    while True:
        report(conn)

        yn = input("quit? (y/n)? ")
        if yn == 'y' or yn == 'Y':
            break


if __name__ == '__main__':
    main()
