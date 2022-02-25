class FindAcct:
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
		cursor.close()  
