#!/usr/bin/env python
from mysql.connector import (connection)
import configparser
import os

# config = configparser.ConfigParser()
# config.read('config.ini')
# muser = config['DEFAULT']['muser']
# mpwd = config['DEFAULT']['mpwd']
# mhost = config['DEFAULT']['mhost']
# mport = config['DEFAULT']['mport']
# mfile = config['DEFAULT']['mfile']


def create_connection(muser, mpwd, mhost, mport, mfile):
    try:
        conn = connection.MySQLConnection(user=muser, password=mpwd, host=mhost, port=mport, database=mfile)
        return conn
    except:
        print('connection to database failed')
        return None


def create_firm(conn, firm_name):
    # mvar = firm_name
    # print('firm name', mvar)
    cursor = conn.cursor()
    # this sql actually works!!!!
    sql = """INSERT INTO firms (name) VALUES ('%s')""" % firm_name
    # sql = ("INSERT INTO firms (name) VALUES (%s) ")
    # sql = """ INSERT INTO firms (name) VALUES (%s) """
    cursor.execute(sql)
    conn.commit()


def find_firm(conn, firm_name):
    """ find firm name, if already in firm table"""
    
    cursor = conn.cursor()
    firm_name = '%'+firm_name+'%'
    
    sql = """ SELECT fid, name FROM firms WHERE name LIKE '%s';""" % firm_name
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not found")
    else:
        for row in rows:
            print(row)


def main():
    conn_user = 'jim'
    conn_pwd = 'ttaskk'
    conn_host = '192.168.1.115'
    conn_port = 3307
    conn_file = "stocks"
    conn = create_connection(muser, mpwd, mhost, mport, mfile)

    while True:
        # find_firm name already in file
        firm_name = input("Search for firm name:")
        fid = find_firm(conn, firm_name)
        yn = input("Do you see name here? (y/n)")
        if yn == 'n':
            firm_name = input("Enter newfirm name here:")
            create_firm(conn, firm_name)
        else:
            break

        yn = input('Continue (y/n)')
        if yn == 'n':
            conn.close()
            break


if __name__ == '__main__':
    main()
