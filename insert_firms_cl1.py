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


# def create_connection(muser, mpwd, mhost, mport, mfile):
#     try:
#         conn = connection.MySQLConnection(user=muser, password=mpwd, host=mhost, port=mport, database=mfile)
#         return conn
#     except:
#         print('connection to database failed')
#         return None

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
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport,
                                              database=self.mfile)
            cursor = conn.cursor()
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


class CreateFirm:
    def __init__(self, firm_name, conn):
        self.firm_name = firm_name
        self.conn = conn

    def create_firm(self):
        self.firm_name = self.firm_name.replace("%", "")
        # print('firm name', self.firm_name)
        # yn=input('line 65, wait')
        cursor = self.conn.cursor()
        # this sql actually works!!!!
        sql = """INSERT INTO firms (name) VALUES ('%s') """ % self.firm_name
        cursor.execute(sql)
        self.conn.commit()

    def show_firm(self):
        """ find firm name, if already in firm table"""
        cursor = self.conn.cursor()
        self.firm_name = '%' + self.firm_name + '%'
        sql = """ SELECT fid, name FROM firms WHERE name LIKE '%s' """ % self.firm_name
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("ID-----FIRM NAME")
        for row in rows:
            print("{}".format(row[1]), "    ", "{}".format(row[0]))

        yn = input("Do you see your firm here ? (q=quit):")
        if yn == 'N' or yn == 'n':
            return yn


def main():
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''
    firm_name = ' '

    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])

    # vmvar = ' '
    # conn = ' '

    conn = a1.create_connection()
    manswer = ''

    while True:
        firm_name = input("Enter new firm name:")
        a2 = CreateFirm(firm_name, conn)

        yn = a2.show_firm()  # firm name on file?

        if (yn == 'n') or (yn == 'N'):  # no firm name on file
            yn = input("Are you ready to add this firm ? (y/n/q)")
            if (yn == 'y') or (yn == 'Y'):
                # firm_name = input("Enter firm name:")
                a2.create_firm()
                a2.show_firm()
            elif (yn == 'n') or (yn == 'N'):
                continue
            else:
                break

                break

        yn = input('Continue (y/n)')
        if (yn == 'n') or (yn == 'N'):
            break
        os.system('clear')
    exit()
    conn.close()


if __name__ == '__main__':
    main()

    os.system('clear')
