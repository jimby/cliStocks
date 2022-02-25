class FindStock:
    def __init__(self, mvar, conn):
        #     self.name = name    # instance variable unique to each instance
        self.mvar = mvar
        self.conn = conn

    def find_stock(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        # sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % self.mvar

        # sql = "SELECT s.sid, s.stock_symbol,s.quantity,s.name, s.price, p.prices, a.long_acct, p.effective_date" \
        #      " FROM firms f, accounts a,  stocks s, prices p  WHERE p.sid=s.sid and s.aid=a.aid and a.fid=f.FID and  s.stock_symbol like '%s' " % self.mvar

        sql = "SELECT stocks.sid, stocks.stock_symbol, stocks.quantity, stocks.name, stocks.price, prices.prices," \
              " accounts.long_acct, prices.effective_date from prices" \
              " INNER JOIN stocks ON prices.sid = stocks.sid" \
              " INNER JOIN accounts ON stocks.aid=accounts.aid" \
              " INNER JOIN firms ON accounts.FID = firms.fid" \
              " WHERE stocks.stock_symbol LIKE '%s' ORDER BY stocks.name ASC" % self.mvar


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
            # print("ID-----FIRM NAME")
            print("-SID-SYM----QTY---NAME---------------------------price1 price2 acct-DATE---------GAIN")
            for row in data:
                # print("{}".format(row[1]),"    ","{}".format(row[0]))
                print("{:3d}".format(row[0]), "{0:5}".format(row[1]), "{:6.2f}".format(row[2]), "{0:30}".format(row[3]),
                "{:6.2f}".format(row[4]), "{:6.2f}".format(row[5]), "{0:15}".format(row[6]),
                "{:%m/%d/%Y}".format(row[7]), "{:6.1f}".format((100 * (row[5] - row[4]) / row[4])), "%")
        cursor.close()
        # self.conn.close()
