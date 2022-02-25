# find_firm.py
from mysql.connector import (connection)
import sys
import configparser

class Connector:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
        self.muser = muser
        self.mpwd = mpwd
        self.mhost = mhost
        self.mport = mport
        self.mfile = mfile

    def create_connection(self):
        try:
            conn = connection.MySQLConnection(user=self.muser, password=self.mpwd, host=self.mhost, port=self.mport, database=self.mfile)
            # print("connected")
            return conn
        except:
            e = sys.exc_info()[0]
            # print("not connected", e)
            return 0


class FindFirm:
    def __init__(self, conn, mfirm):
        self.conn = conn
        self.mfirm = mfirm

    def find_firm(self):
        cursor = self.conn.cursor()
        
        sql = """SELECT FID, name  FROM firms WHERE name like '%s' """ % self.mfirm
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) > 0:
            return data
            # print("FID--NAME")
            # for row in data:
            #     print("{:3d}".format(row[0]), "{0:5}".format(row[1]))
        else:
            return 0

def main():
    # muser = 'jim'
    # mpwd = 'ttaskk'
    # mhost = '192.168.1.115'
    # mport = 3307
    # mfile = "stocks"
    config = configparser.ConfigParser()
    config.read('config.ini')
    muser = config['DEFAULT']['muser']
    mpwd = config['DEFAULT']['mpwd']
    mhost = config['DEFAULT']['mhost']
    mport = config['DEFAULT']['mport']
    mfile = config['DEFAULT']['mfile']
    
    conn = 0
    mfirm = ""

    a = Connector(muser, mpwd, mhost, mport, mfile)
    conn = a.create_connection()

    if conn:
        print("connected")
    else:
        print("not connected")
    while True:
        mfirm = input("Firm name: ")
        mfirm = '%'+mfirm+'%'
        if mfirm == "%%":
            break

        b = FindFirm(conn, mfirm)
        data = b.find_firm()
        if len(data) > 0:
            print("FID--NAME")
            for row in data:
                print("{:3d}".format(row[0]), "{0:5}".format(row[1]))
        
        yn = input('Continue (y/n)')
        if yn == 'n':
            break


if __name__ == '__main__':
    main()
