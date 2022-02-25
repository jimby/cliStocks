
from mysql.connector import (connection)
# import importlib
import configparser
# import find_menuNew

config = configparser.ConfigParser()
config.read('config.ini')
muser = config['DEFAULT']['muser']
mpwd = config['DEFAULT']['mpwd']
mhost = config['DEFAULT']['mhost']
mport = config['DEFAULT']['mport']
mfile = config['DEFAULT']['mfile']
print(muser)
# yn=input("stop at line 14")

class FindFirm:

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def create_connection(db_user, db_pwd, db_host, db_port, db_file):
        try:
            conn = connection.MySQLConnection(user=db_user, password=db_pwd, host=db_host, port=db_port, database=db_file)
            cursor = conn.cursor()
            return conn
        except Exception as e:
            return e
        

    def find_firm(conn, m_var):
        """ find aid, stock_symbol, if already in stocks table"""
        # print("aid,stock_symbol", aid, stock_symbol)
        cursor = conn.cursor()
        # m_symbol = input("Symbol: ")
        # m_symbol = '%{}%'.format(m_symbol)
        # print(m_symbol)
        sql = """ SELECT f.name, f.FID FROM firms f WHERE f.name like '%s';""" % m_var  
        # sql = """SELECT s.sid, s.stock_symbol,s.quantity,s.name, s.price,p.prices, a.long_acct, s.transwer_date FROM ((stocks s inner join accounts a on s.aid=a.aid) inner join prices p on s.sid=p.sid) WHERE  s.stock_symbol like '%s' """ % m_firm
        # sql = """select s.sid, s.price from stocks s where s.stock_symbol like '%s';""" % m_symbol
        cursor.execute(sql)
        data = cursor.fetchall()

        if len(data) == 0:
            # print(len(data))
            # t = input("line: 51")
            # print('not found')
            print(m_var, "not found...")
            # yn = '0'
            return 0
        else:
            print("ID-----FIRM NAME")
            for row in data:
                print("{}".format(row[1]),"    ","{}".format(row[0]))

def main():
    
    d = FindFirm

    conn = d.create_connection(muser, mpwd, mhost, mport, mfile)

    while True:
        m_var = input("Firm: ")
        m_var = '%{}%'.format(m_var)
        if m_var == "%%":
            break
        d.find_firm(conn, m_var)
        yn = input('Continue (y/n)')
        if yn == 'n':
            break
    exit                   


if __name__ == '__main__':
    main()
    # import sys
    # find_menuNew

