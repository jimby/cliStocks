#! /usr/bin/env python3
import MakeConnection
import os
# form a column with print out
# add formatted column names


class FindFirm:
    cursor = ''
    mfirm = ''
    def __init__(self, conn):
        self.conn = conn
        
    def find_firm(self, conn):
        """ find aid, stock_symbol, if already in stocks table"""

        cursor = self.conn.cursor()
        
        while True:
            mfirm = input("enter firm name: ")
            mfirm = '%{}%'.format(mfirm)
            os.system('clear')
            # print('fl15 conn: ', self.conn)
            # print('fl17 firm: ', mfirm)
            sql = "SELECT f.FID, f.name, f.street, f.city_state_zip, f.agent, f.phone, f.email FROM firms f WHERE f.name like '%s'" % mfirm
            cursor.execute(sql)
            
            data = cursor.fetchall()
            
            if len(data) == 0:
                # yn = input("fl20 sql fails")
                print ("No firm found")
            else:
                for row in data:
                    print(
                    "{a:<15}".format(a='record number:'),"{}".format(row[0]),"\n",
                    "{a:<15}".format(a='firm name:'),"{}".format(row[1]),"\n",
                    "{a:<15}".format(a='street:'),"{}".format(row[2]),"\n",
                    "{a:<15}".format(a='city:'),"{}".format(row[3]),"\n",
                    "{a:<15}".format(a='agent:'),"{}".format(row[4]),"\n",
                    "{a:<15}".format(a='phone:'),"{}".format(row[5]),"\n",
                    "{a:<15}".format(a='email:'),"{}".format(row[6]),"\n\n")
                    
            yn = input("continue y/n")
        
            if (yn == 'N' or yn == 'n'):
                break
            else:
                continue
        
        
        
                
        # self.conn.close()
        

def main():
    
    conn = MakeConnection.get_config()
    
    
    ff = FindFirm(conn)
    
    
    if not conn:
        print("no connection fl65")

    ff.find_firm(conn)
    
            

if __name__ == '__main__':
    main()
    # conn.close()
    os.system('clear')

    # cursor.close
    # conn.close
    # import sys
    # find_menuNew
