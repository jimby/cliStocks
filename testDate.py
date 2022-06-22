
# translate date  format from "%m/%d/%y" to "%Y-%m-%d"
from datetime import datetime
def GetDate():
    strdate = input("date: ")

    txt = strdate[-4:]
    x = txt.isnumeric()
    if x:
    	format_date = '%m/%d/%Y'
    else:
    	format_date = '%m/%d/%y'
 
    date = datetime.strptime(strdate,format_date)
    return date
 

