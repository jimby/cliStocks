#! /usr/bin/env python

import MakeConnection
from os import system
from datetime import datetime
import subprocess

class EditFirm:
    def __init__(self, mvar, conn, mname, mfid, mstreet, mCityStateZip, mAgent, mphone, memail):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn
        self.mname = mname
        self.mfid = mfid
        self.mstreet = mstreet
        self.mCityStateZip = mCityStateZip
        self.mAgent = mAgent
        self.mphone = mphone
        self.memail = memail

    def find_firms(self):

        """ find aid, stock_symbol, if already in stocks table"""
        manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.mname = input("enter firm name: ")
        self.mname = '%{}%'.format(self.mname)

        # sql = """SELECT sid,stock_symbol,name, quantity, price, trans_date.day") \
        # as 'date',buyorsell FROM stocks"""

        # choose record to edit
        sql = """SELECT f.fid, f.name FROM firms f  WHERE f.name like '%s' """ % self.mname
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print("ID| firm name")
            for row in results:
                print("{:3d}".format(row[0]), "{0:60s}".format(row[1]))

            self.mfid = input("Enter id or quit: (q)?")
            print('fid: ', self.mfid)
            yn = input('waiting at line 44')
            return self.mfid
        except Exception as e:
            print("Error: no data")
            return 0

    def edit_firms(self):

        # self.mfid = self.mvar
        cursor = self.conn.cursor()
        print('cursor', cursor)
        yn = 'Waiting at line 87'

        sql = """SELECT * from firms where fid = '%s'""" % self.mfid
        cursor.execute(sql)
        results = cursor.fetchone()

        for row in results:
            # sql = """SELECT * from firms where fid = '%s'""" % self.mfid
            # cursor.execute(sql)
            # results = cursor.fetchone()
            self.mfid = int(results[0])
            self.mname = results[1]
            self.mstreet = results[2]
            self.mCityStateZip = results[3]
            self.mAgent = results[4]
            self.mphone = results[5]
            self.memail = results[6]


        print("fid:          {}".format(self.mfid))
        # print("1) symbol =   {}".format(m_stock_symbol))
        print("1) name =       {}".format(self.mname))
        print("2) street =     {}".format(self.mstreet))
        print("3) city =       {}".format(self.mCityStateZip))
        print("4) advisor =    {}".format(self.mAgent))
        print("5) phone =      {} ".format(self.mphone))
        print("6) email =      {}".format(self.memail))
        mcolumn = input("Enter column number to edit (q=quit)")

        # choose fields to edit
        if mcolumn == '1':
            col = 'name'
        elif mcolumn == '2':
            col = 'street'
        elif mcolumn == '3':
            col = 'CityStateZip'
        elif mcolumn == '4':
            col = 'Agent'
        elif mcolumn == '5':
            col = 'phone'
        elif mcolumn == '6':
            col = 'email'
        elif mcolumn == 'Q':
            subprocess.run(["/home/jim/projects/cliStocks/EditMenu.sh"], shell=True)
        elif mcolumn == 'q':
            subprocess.run(["/home/jim/projects/cliStocks/EditMenu.sh"], shell=True)
        # get and insert values
        mnewdata = input("Enter new value: ")
        cursor.execute("""UPDATE firms set {}=%s where fid=%s""".format(col), (mnewdata, self.mfid))
        self.conn.commit()



def main():
    conn = MakeConnection.get_config()

    # firms columns
    mfid = 0
    mname = ''
    mstreet = ''
    mCityStateZip = ''
    mAgent = ''
    mphone = ''
    memail = ''

    mvar = ' '
    # conn = ' '
    mfirm = ' '


    # FIND DESIRED FIRM
    a2 = EditFirm(mvar, conn, mname, mfid, mstreet, mCityStateZip, mAgent, mphone, memail)
    # mfid = a2.find_firms()
    # a2 = EditFirm(mvar, conn, mname, mfid, mstreet, mCityStateZip, mAgent, mphone, memail)

    while True:
        # m_var = input("Firm: ")
        # m_var = '%{}%'.format(m_var)

        # if m_var == "%%":
        #     print("line 92, %%")
        #     break
        mfid = a2.find_firms()
        a2 = EditFirm(mvar, conn, mname, mfid, mstreet, mCityStateZip, mAgent, mphone, memail)

        a2.edit_firms()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break

    conn.close()
    
    # return to EditMenu.sh
    subprocess.run(["/home/jim/projects/cliStocks/EditMenu.sh"])


if __name__ == '__main__':
    main()
    system('clear')
    
