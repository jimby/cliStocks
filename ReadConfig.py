import configparser
config = configparser.ConfigParser()
config.read('config.ini')
muser = config['DEFAULT']['muser']
mpwd = config['DEFAULT']['mpwd']
mhost = config['DEFAULT']['mhost']
mport = config['DEFAULT']['mport']
mfile = config['DEFAULT']['mfile']
print(mpwd)
