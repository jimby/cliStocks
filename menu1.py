#!/usr/bin/env python
import insert_firms_cl1
import insert_account_cl1
import find_firm_cl2
import find_symbol_cl
import find_acct_cl2
import report_gains
import report_stocks
import insert_dividends
import update_prices
import report_acct
import insert_stocks_cl2

while True:
    print("Choose:")
    print("  1. add firm: ")
    print("  2. add account")
    print("  3. find firm")
    print("  4. find symbol")
    print("  5. find account")
    print("  6. report gains")
    print("  7. report stocks")
    print("  8. add dividends")
    print("  9. update prices")
    print("  10. display accounts' equities" )
    print("  11. insert stocks")
    print("  q.  quit")
    yn = input("choose->")
    if yn == '1':
        insert_firms_cl1.main()
    elif yn == '2':
        insert_account_cl1.main()
    elif yn == '3':
        find_firm_cl2.main()
    elif yn == '4':
        find_symbol_cl.main()
    elif yn == '5':
        find_acct_cl2.main()
    elif yn == '6':
        report_gains.main()
    elif yn == '7':
        report_stocks.main()
    elif yn == '8':
        insert_dividends.main()
    elif yn == '9':
        update_prices.main()
    elif yn == '10':
        report_acct.main()
    elif yn == '11':
        insert_stocks_cl2.main()
    elif yn == 'q' or yn == 'Q':
        break
