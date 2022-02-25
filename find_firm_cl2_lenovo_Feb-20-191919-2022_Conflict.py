import MakeConnection
import os


class FindFirm:

    def __init__(self, conn):
        #     self.name = name    # instance variable unique to each instance
        self.conn = conn

    def find_firm(self, conn):
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
        

def main():
    b = ''
    p1 = MakeConnection

    muser = ''
    mpwd = ''
    mfile = ''

    muser = input('Enter user name: ')
    mpwd = input('Enter password: ')
    mfile = input('Enter database name: ')

    b = p1.get_config()

    conn = p1.create_connection(b)
    FindFirm.find_firm
    if not conn:
        print("no connection l52")

    while True:
        m_var = input("Firm: ")
        m_var = '%{}%'.format(m_var)

        if m_var == "%%":
            print("line 92, %%")
            break

        a2 = FindFirm(m_var, conn)
        a2.find_firm()

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
