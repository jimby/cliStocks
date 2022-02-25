# list stocks
from mysql.connector import (connection)

import datetime

# noinspection PyUnresolvedReferences
# import datetime
# global yn

def create_connection(conn_user, conn_pwd, conn_host, conn_port, conn_file):
    try:
        conn = connection.MySQLConnection(user=conn_user, password=conn_pwd, host=conn_host, port=conn_port, database=conn_file)
        return conn
    except Exception as e:
        print(e)
        return None


def find_account(conn):
    msg = "account"
    # print(conn)
    # cursor = conn.cursor
    """ find firm name, if already in firm table"""
    while True:
        cursor = conn.cursor()
        val1 = input("Enter account number: ")
        val1 = '%'+val1+'%'

        # print(val1)
        sql = """SELECT aid, long_acct FROM accounts WHERE long_acct LIKE '%s' """ % val1
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


def list_stock(conn, val):

    cursor = conn.cursor()
    print("line 53 sid: ", val)
    val = int(val)
    sql = """SELECT * from stocks where aid = '%s' order by name""" % val
    try:
        cursor.execute(sql)
        # results = cursor.fetchall()  # fetch one
        # for row in results:
        #    print("{0:5}".format(row[1]), "{:6.2f}".format(row[3]), "{0:25}".format(row[2]), \
        #          "{:6.2f}".format(row[4]),"{:%m/%d/%Y} ".format(row[6]))
    except Exception as e:
        print("Error: unable to find data")

    results = cursor.fetchall()  # fetch one
    print("symbol-qty---name-----------------------price-date acquired")
    for row in results:
        # print("{0:5}".format(row[1]), "{:6.2f}".format(row[3]), "{0:25}".format(row[2]), \
        #      "{:6.2f}".format(row[4]), "{:%m/%d/%Y} ".format(row[6]))
        print("{0:5}".format(row[1]), "{:6.2f}".format(row[3]), "{0:25}".format(row[2]),\
            "{:6.2f}".format(row[4]), "{:%m/%d/%Y} ".format(row[6]))

    # sid = int(sid)
    #   print("\nsid", sid, "\nsymbol", stock_symbol)


def main():
    conn_user = 'jim'
    conn_pwd = '8uhb(IJN'
    conn_host = '192.168.1.115'
    conn_port = 3307
    conn_file = "securities"

    conn = create_connection(conn_user, conn_pwd, conn_host, conn_port, conn_file)

    m_aid = find_account(conn)
        
    # answer = find_stock(conn, m_aid)
    list_stock(conn, m_aid)


if __name__ == '__main__':
    main()
