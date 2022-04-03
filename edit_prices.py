from mysql.connector import (connection)
import configparser
import os


class MakeConnection:

    def __init__(self, muser, mpwd, mhost, mport, mfile):
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


class EditPrices:
    def __init__(self, mvar, conn, mpid, msymbol, meffective_date, mprices, msid):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn
        self.mpid = mpid
        self.msymbol = msymbol
        self.meffective_date = meffective_date
        self.mprices = mprices
        self.msid = msid

    # noinspection SqlResolve
    def find_prices(self):

        """ find aid, stock_symbol, if already in stocks table"""
        manswer = ''
        # while True:
        cursor = self.conn.cursor()
        self.msymbol = input("enter stock symbol: ")
        self.msymbol = '%{}%'.format(self.msymbol)

        #  sql = """SELECT tp.pid, tp.symbol, tf.name, ta.long_acct, ts.quantity, ts.name, tp.effective_date, tp.prices
        # from test_prices tp
        # INNER JOIN test_stocks ts on ts.sid = tp.sid
        # INNER JOIN test_accounts ta on ta.aid = ts.aid
        # INNER JOIN test_firms tf on tf.FID = ta.fid
        sql = """select pid, symbol, price, date from Prices where symbol like '%s'"""% self.msymbol
        
        
        # WHERE tp.symbol LIKE '%s' ORDER BY tp.symbol ASC""" % self.msymbol

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("PID|   |symbol   Price             |Date")
            for row in results:
                print("{0:<5}".format(row[0]), "{0:<10}".format(row[1]), "{0:<10}".format(row[2]), "{0:10}".format(row[3]),
                      "{0:>10}".format(row[4]))

            self.mpid = input("Enter id or quit: (q)?")
            return self.mpid
            # print('pid: ', self.mpid)
        except Exception as e:
            print("l83 Error: no data")
            return 0

    def edit_prices(self):
        while True:
            cursor = self.conn.cursor()

            sql = """SELECT * from prices where pid = '%s'""" % self.mpid
            cursor.execute(sql)
            results = cursor.fetchone()

            for row in results:
                # sql = """SELECT * from pricess where fid = '%s'""" % self.mpid
                # cursor.execute(sql)
                # results = cursor.fetchone()
                self.mpid = int(results[0])
                self.msymbol = results[1]
                self.meffective_date = results[2]
                self.mprices = results[3]
                self.msid = results[4]

            print("\npid:          {}".format(self.mpid))
            print("symbol =   {}".format(self.msymbol))
            print("sid =      {} ".format(self.msid))
            # print("1) name =       {}".format(self.mname))
            print("\n1) date =     {}".format(self.meffective_date))
            print("2) price =    {}".format(self.mprices))

            # print("6) email =      {}".format())
            mcolumn = input("Enter column number to edit (q=quit)")

            # choose fields to edit
            # if mcolumn == '1':
            #    col = 'name'
            if mcolumn == '1':
                col = 'effective_date'
            elif mcolumn == '2':
                col = 'prices'
            # elif mcolumn == '4':
            #     col = 'Agent'
            # elif mcolumn == '5':
            #     col = 'phone'
            # elif mcolumn == '6':
            #    col = 'email'
            elif mcolumn =='q' or mcolumn == 'Q':
                break

            # get and insert values
            mnewdata = input("Enter new value: ")
            sql = "UPDATE test_prices SET prices = %s WHERE pid = $s"
            val = (mnewdata, col)
            cursor.execute("""UPDATE test_prices set {}=%s where pid=%s""".format(col), (mnewdata, self.mpid))
            self.conn.commit()


def main():
    # mysql connection
    muser = ''
    mpwd = ''
    mhost = ''
    mport = 0
    mfile = ''

    # prices columns
    mvar = ''
    conn = ''
    mpid = 0
    msymbol = ''
    meffective_date = ''
    mprices = ''
    msid = 0


    mvar = ' '
    conn = ' '
    mprices = ' '

    # CONNECT TO MYSQL DATABASE
    a1 = MakeConnection(muser, mpwd, mhost, mport, mfile)
    b = a1.get_config()
    a1 = MakeConnection(b[0], b[1], b[2], b[3], b[4])
    conn = a1.create_connection()

    # FIND DESIRED prices
    a2 = EditPrices(mvar, conn, mpid, msymbol, meffective_date, mprices, msid)
    # mpid = a2.find_pricess()
    # a2 = Editprices(mvar, conn, mname, mpid, msymbol, meffective_date, mprices, msid, )

    while True:
        # m_var = input("prices: ")
        # m_var = '%{}%'.format(m_var)

        # if m_var == "%%":
        #     print("line 92, %%")
        #     break
        mpid = a2.find_prices()
        print("mpid: ", mpid)
        yn = input("waiting at line 178")
        a2 = EditPrices(mvar, conn, mpid, msymbol, meffective_date, mprices, msid)

        a2.edit_prices()
        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        os.system('clear')
    conn.close()


if __name__ == '__main__':
    main()
    os.system('clear')
