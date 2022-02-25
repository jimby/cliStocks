#!/usr/bin/env python
# InsertAccount.py, ver 2.0
# from mysql.connector import (connection)

from mysql.connector import (connection)
import configparser
import os
global yn


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

class InsertAcct:
    def __init__(self, conn, maid, mshort_acct, mlong_acct, macct_type, mfid):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn
        self.maid = maid
        self.mshort_acct = mshort_acct
        self.mlong_acct = mlong_acct
        self.macct_type = macct_type
        self.mfid = mfid

    def find_account(self):
        # """ find firm name, if already in firm table"""
        cursor = self.conn.cursor()
        self.mlong_acct = input("Full account #: ")
        cursor.execute("SELECT f.fid, a.long_acct, f.name FROM test_accounts a, test_firms f WHERE a.fid=f.fid and a.long_acct LIKE %s", ('%' + self.mlong_acct + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        if not rows:
            yn = 0

        yn = input("Enter firm id (fid) or 0 if not found: ")
        return yn

    def insert_account(self):
        cursor = self.conn.cursor()
        print('line 71-self.mfid:', self.mfid)
        yn = input('waiting at line 72')

        self.mshort_acct = input("Enter short account number: ")
        self.mlong_acct = input("Enter long account number: ")
        self.macct_type = input("Enter account type: ")


        sql = """INSERT INTO test_accounts (short_acct, long_acct, acct_type, fid) VALUES (%s, %s, %s, %s) """
        cursor.execute(sql, (self.mshort_acct, self.mlong_acct, self.macct_type, self.mfid))
        self.conn.commit()

class InsertFirm:
    def __init__(self, conn, m_fid, m_agent, m_CityStateZip, m_email, m_name, m_phone, m_street):
        self.conn = conn
        self.m_fid = m_fid
        self.m_agent = m_agent
        self.m_CityStateZip = m_CityStateZip
        self.m_email = m_email
        self.m_name = m_name
        self.m_phone = m_phone
        self.m_street = m_street

    def insert_firm(self):
        sql = """INSERT INTO test_firms (name, street, city_state_zip, Agent, phone, email) VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (self.m_name, self.m_street, self.m_CityStateZip, self.m_agent, self.m_phone, self.m_email))
        self.conn.commit()
        self.m_fid = cursor.lastrowid
        return self.m_fid

    def find_firm(self):
        cursor = self.conn.cursor()

        self.m_name = input("Search for firm name: ")
        self.m_name = '%'+self.m_name+'%'
        sql = """SELECT fid, name FROM test_firms WHERE name LIKE '%s' """ % self.m_name
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        yn = input("Do you see your firm's name here (y/n)?")

        if not yn:
            return 0
        else:
            yn = input("Enter firm index number (fid):")
            return yn




def main():
    input("waiting at line 125")
    #connect to database
    muser = '';mpwd = '';mhost = '';mport = 0;mfile = ''
    connect1 = MakeConnection(muser, mpwd, mhost, mport, mfile)

    b = connect1.get_config()
    mfid = ' '

    connect1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = connect1.create_connection()

    # initialize InsertAcct
    mvar=''; maid = 0; mshort_acct=' ';mlong_acct=' '; macct_type=' ';mfid=0; mname=' '
    insert_acct1 =InsertAcct(conn, maid, mshort_acct, mlong_acct, macct_type, mfid)

    # initialize InsertFirm
    m_fid = 0; m_agent='';m_CityStateZip='';m_email='';m_name='';m_phone='';m_street=''
    insert_firm1 = InsertFirm(conn, m_fid, m_agent, m_CityStateZip, m_email, m_name, m_phone, m_street)

    while True:
    # find if firm on file
        mfid = insert_acct1.find_account()
        # if firm not found, insert firm
        if mfid == '0':
            print("No firm found")
            m_name = input("Enter new firm name: ")
            m_street = input("Street: ")
            m_CityStateZip= input("City, State, zip: ")
            m_Agent = input("Enter Financial Advisor: ")
            m_phone = input("Enter advisor's phone number: ")
            m_email = input("advisor's email address: ")
            insert_firm1 = InsertFirm(conn, m_fid, m_agent, m_CityStateZip, m_email, m_name, m_phone, m_street)
            mfid = insert_firm1.insert_firm()
            print("l 157-mfid: ", mfid)
            yn=input("waiting at line 158")


            # insert account

            insert_acct1=InsertAcct(conn, maid, mshort_acct, mlong_acct, macct_type, mfid)
            insert_acct1.insert_account()
    # if firm found
        else:
            yn = input('Add another account (y/n) ?')
            if yn == 'n' or yn == 'N':
                break




if __name__ == '__main__':
    main()
    os.system('clear')
