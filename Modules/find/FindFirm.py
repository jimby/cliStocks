class FindFirm:
    def __init__(self, conn):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn

    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""
        m_firm_name = input("Enter firm name: ")
        cursor = self.conn.cursor()
        sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % m_firm_name
        # cursor.execute(sql)
        # data = cursor.fetchall()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("ID| firm name")
            for row in results:
                print("{}".format(row[0]), "{0:60s}".format(row[1]))

            mfid = input("Enter id or quit: (q)?")
            return mfid
            # print('fid: ', self.mfid)
            # yn = input('waiting at line 74')
        except (ValueError, Exception):
            print("Error: no data")
            return 0

        cursor.close()
