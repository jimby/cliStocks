
class Edit:

    def create_connection(self, conn_user, conn_pwd, conn_host, conn_port, conn_file):
        from mysql.connector import (connection)
        try:
            conn = connection.MySQLConnection(user=conn_user, password=conn_pwd, host=conn_host, port=conn_port, database=conn_file)
            return conn
        except Exception as e:
            print(e)
            return None

    def edit_dividend(self, conn, maid, msid):
        cursor = conn.cursor()
        t = input("line 58")
        sql ="""select d.did, a.short_acct, s.quantity,s.stock_symbol,d.share_dividend, d.settle_date from accounts a, stocks s, dividends d where a.aid=s.aid and s.sid = d.sid"""
        cursor.execute(sql)
        t = input("line 61")
        print("DivID--acct---qty--symbol---div/share-----SettleDate")
    # print("account--s.sid-qty--symbol--d.did-iishares---date div")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        mdid = input("Select dividend-id (did): ")
        mdividend = input("Enter new dividend per share:")
        mdate = input("Enter the settlement date:")

        cursor.execute("""UPDATE dividends SET  share_dividend = %s, settle_date = %s WHERE did= %s """, (mdividend, mdate, mdid, ))

        sql = """SELECT d.did,a.short_acct, s.quantity, s.stock_symbol,  d.share_dividend, d.settle_date from accounts a, stocks s, dividends d where s.sid=d.sid"""
        cursor.execute(sql)
        print("DivID--acct---qty--symbol---div/share-----SettleDate")
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
        yn = input("this is is your edited dividend file")
        conn.commit()
        yn = input('Continue or quit? (c/q)')
        if yn == 'q':
            return

    