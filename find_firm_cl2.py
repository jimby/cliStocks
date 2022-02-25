import MakeConnection
import os


class FindFirm:
    def __init__(self, conn, mfirm):
        self.conn = conn
        self.mfirm = mfirm

    def find_firm(self):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        sql = "SELECT f.name, f.FID FROM firms f WHERE f.name like '%s'" % self.mfirm
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
        

def main():
    
    conn = MakeConnection.get_config()
    print("Conn: ", conn)
    mfirm = input('Enter firm name: ')
    ff = FindFirm(conn, mfirm)
    ff.find_firm()
    
    if not conn:
        print("no connection fl42")

    while True:
        # m_var = input("Firm: ")
        mfirm = '%{}%'.format(mfirm)

        if mfirm == "%%":
            print("no firm name fl49, %%")
            break

        ff.find_firm()

        yn = input('Continue (y/n)')
        if yn == 'n':
            break
        os.system('clear')
    # exit
    conn.close()
    return


if __name__ == '__main__':
    main()
    os.system('clear')

    # cursor.close
    # conn.close
    # import sys
    # find_menuNew
