#!/usr/bin/env python
from mysql.connector import (connection)
import pwinput
import configparser
# this is attempt to ass configparser as function in class FindFirm

mhost = ''
mport = 0
mstring = ''
muser = ''
mpwd = ''
mfile = ''

def get_config():
        
    muser = input('Enter user: ')
    mpwd = pwinput.pwinput('Password: ')
    mfile = input("Enter database: ")
    
        
    config = configparser.ConfigParser()
    config.read('config.ini')

    mhost = config['DEFAULT']['mhost']
    mport = config['DEFAULT']['mport']

    mstring = [muser, mpwd, mhost, mport, mfile]

    try:
        conn = connection.MySQLConnection(user=muser, password=mpwd, host=mhost, port=mport, database=mfile)
        # cursor = conn.cursor()
        # print("connected")
        # return cursor
        # print("Successful", conn)
        return conn
    except Exception as e:
        # print("no connection")
        return 0



