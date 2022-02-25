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
    def __init__(self, mvar, conn):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn

    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % self.mvar
        cursor.execute(sql)

        data = cursor.fetchall()

        if len(data) == 0:
            # print(len(data))
            # t = input("line: 51")
            # print('not found')
            # print(m_var, "not found...")
            # yn = '0'
            return 0
        else:
            print("ID-----FIRM NAME")
            for row in data:
                print("{}".format(row[1]), "    ", "{}".format(row[0]))
        cursor.close()
        # self.conn.close()


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
        self.email = memail

    def edit_firms(self):
        self.mfid = self.mvar
        cursor = self.conn.cursor()

        sql = """SELECT * from firms where fid = '%s'""" % self.mfid
        cursor.execute(sql)
        results = cursor.fetchone()
        print("results: ", results)
        print("results[1]", results[0])  # fetch one
        for row in results:
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
        print("6) email =      {}".format(self.email))
        mcolumn = input("\nEnter column number to edit (q=quit, no change) ")
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
        # elif mcolumn == '7':
        #     col = 'buyorsell'
        elif mcolumn == 'q' or mcolumn == 'Q':
            return

            # get new values
        mnewdata = input("Enter new value: ")

        # update stocks
        # sql = """ UPDATE stocks SET `%s` = %s WHERE sid = %s"""
        cursor.execute("""UPDATE firms set {}=%s where fid=%s""".format(col), (mnewdata, self.mfid))
        # cursor.execute(sql, (col, mnewData, sid))

        db.commit()

        # show changes
