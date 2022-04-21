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


class EditAcct:
    def __init__(self, mvar, conn, maid, mshort_acct, mlong_acct, macct_type, mfid, mname):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn
        self.maid = maid
        self.mshort_acct = mshort_acct
        self.mlong_acct = mlong_acct
        self.macct_type = macct_type
        self.mfid = mfid
        self.mname = mname

    def find_accts(self,conn):
        """ find aid, stock_symbol, if already in stocks table"""
        manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.mlong_acct = input("enter account#: ")
        self.mlong_acct = '%{}%'.format(self.mlong_acct)
        print(self.mlong_acct)
        yn = input('line 58')

        # choose record to edit
        sql = """SELECT a.aid, f.name, a.short_acct, a.long_acct, a.acct_type  FROM accounts a, firms f WHERE f.FID = a.fid AND a.long_acct LIKE '%s' """ % self.mlong_acct
        print('sql:', sql)
        yn = input('waiting at line 64')

        try:
            yn = input('Waiting at line 67')
            cursor.execute(sql)
            results = cursor.fetchall()
            # print("ID| firm name", "{0:60s}".format(row[0]))
            print("AID__AcctName__________________ShortAcct______________________Long account__________account type")
            for row in results:
                # print("%-4d %-25s %-30s %-25s %-25s" % (row[0], row[1], row[2], row[3], row[4]))
                print(row)
            self.maid = input("Enter id or quit: (q)?")
            return self.maid
            # print('fid: ', self.mfid)
            # yn = input('waiting at line 74')
        except Exception as e:
            print("Error: no data")
            return 0

    def edit_accts(self):
        while True:
            # self.mfid = self.mvar
            cursor = self.conn.cursor()
            # print('self.maid', self.maid)
            # yn = 'Waiting at line 99'
            sql = """SELECT a.aid, f.name, a.short_acct, a.long_acct, a.acct_type  FROM accounts a, firms f WHERE f.FID = a.fid AND a.aid = '%s' """ % self.maid
            # sql = """SELECT a.aid, a.short_acct, a.long_acct, f.name, f.FID from accounts a, firms f where aid = '%s'""" % self.maid
            cursor.execute(sql)
            results = cursor.fetchone()

            for row in results:
                # sql = """SELECT * from firms where fid = '%s'""" % self.mfid
                # cursor.execute(sql)
                # results = cursor.fetchone()
                self.maid = int(results[0])
                self.mname = results[1]
                self.mshort_acct = results[2]
                self.mlong_acct = results[3]
                self.macct_type = results[4]
                # self.mfid = results[4]
                # self.mphone = results[5]
                # self.memail = results[6]
                # m_bs = results[7]
                # m_aid = int(results[8])

            # print("\nfid:        {}".format(self.mfid))
            # print("1) symbol =   {}".format(m_stock_symbol))
            print(" ID =           {}".format(self.maid))
            print("Firm name:) =   {}".format(self.mname))
            print("1) short account number =     {}".format(self.mshort_acct))
            print("2) long_acct =  {}".format(self.mlong_acct))
            print("3) account type =             {}".format(self.macct_type))
            # print("firms ID =      {} ".format(self.mfid))
            # print("6) email =      {}".format(self.memail))
            mcolumn = input("Enter column number to edit (q=quit)")

            # choose fields to edit
            if mcolumn == '1':
                col = 'short_acct'
            elif mcolumn == '2':
                col = 'long_acct'
            elif mcolumn == '3':
                col = 'acct_type'
            # elif mcolumn == '4':
            #     col = 'Agent'
            # elif mcolumn == '5':
            #     col = 'phone'
            # elif mcolumn == '6':
            #     col = 'email'
            elif mcolumn =='q' or mcolumn == 'Q':
                break

            # get and insert values
            mnewdata = input("Enter new value: ")
            cursor.execute("""UPDATE accounts set {}=%s where aid=%s""".format(col), (mnewdata, self.maid))
            self.conn.commit()
            # print("6) email =      {}".format(self.email))
            # break

            # yn = input('l138 continue (y/n)')  # <-- move: doesn't allow last edit to print
            # if yn == 'n' or yn == 'N':
            #     break

            # show changes


def main():
    # mysql connection
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''

    # accounts columns
    maid = 0
    mshort_acct = ''
    mlong_acct = ''
    macct_type = ''
    mfid = 0

    # firm columns
    mname = ''
    mvar = ' '
    conn = ' '

    # CONNECT TO MYSQL DATABASE
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # FIND DESIRED ACCOUNT
    a2 = EditAcct(mvar, conn, maid, mshort_acct, mlong_acct, macct_type, mfid, mname)


    while True:
        maid = a2.find_accts(conn)
        a2 = EditAcct(mvar, conn, maid, mshort_acct, mlong_acct, macct_type, mfid, mname)

        a2.edit_accts()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        os.system('clear')
    exit
    conn.close()


if __name__ == '__main__':
    main()
    os.system('clear')
