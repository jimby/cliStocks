import os
mdate = ' '
while True:

    print(mdate)
    mdate = input('Date: ')
    print(mdate)
    ## print('Date: ', mdate)
    yn = input("[Q]uit")
    # os.system('clear')
    if yn == 'q' or yn == 'Q':
        break