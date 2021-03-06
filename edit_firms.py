from mysql.connector import (connection)
import configparser
import os


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

        sql = """SELECT f.fid, f.name FROM firms f  WHERE f.name like '%s' """ % self.mname
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("ID| firm name")
            for row in results:
                print("{}".format(row[0]), "{0:60s}".format(row[1]))

            self.mfid = input("Enter id or quit: (q)?")
            return self.mfid
            # print('fid: ', self.mfid)
            yn = input('waiting at line 74')
        except Exception as e:
            print("Error: no data")
            return 0

    def edit_firms(self):
        while True:
            cursor = self.conn.cursor()

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
                # m_bs = results[7]
                # m_aid = int(results[8])

            print("\nfid:          {}".format(self.mfid))
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
            elif mcolumn =='q' or mcolumn == 'Q':
                break

            # get and insert values
            mnewdata = input("Enter new value: ")
            cursor.execute("""UPDATE firms set {}=%s where fid=%s""".format(col), (mnewdata, self.mfid))
            self.conn.commit()


def main():
    # mysql connection
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''

    # firms columns
    mfid = 0
    mname = ''
    mstreet = ''
    mCityStateZip = ''
    mAgent = ''
    mphone = ''
    memail = ''

    mvar = ' '
    conn = ' '
    mfirm = ' '

    # CONNECT TO MYSQL DATABASE
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

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
        print("mfid: ", mfid)
        yn = input("waiting at line 173")
        a2 = EditFirm(mvar, conn, mname, mfid, mstreet, mCityStateZip, mAgent, mphone, memail)

        a2.edit_firms()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        os.system('clear')
    conn.close()


if __name__ == '__main__':
    main()
    os.system('clear')
