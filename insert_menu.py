#!/usr/bin/env python3
import importlib

ans = True
while ans:
    print("""
        (S) Add stocks
        (P) Add Prices
        (D) Add dividends
        (F) Add firms
        (A) add accounts
        (M) return to main menu
        () Quit
    """)

    ans = input("Data entry: ")
    print(ans)
    if ans == "S" or ans == "s":
        print("\n Add stocks")
        importlib.import_module('insert_stocks_cl2')
        import insert_stocks_cl2
        t = insert_stocks_cl2.main()
        print("Add stocks-")
    elif ans == "P" or ans == "p":
        print("\nAdd prices")
        importlib.import_module('insert_prices')
        import insert_prices
        t = insert_prices.main()
        print("Add prices-")
    elif ans == "D" or ans == "d":
        print("\nAdd dividends")
        importlib.import_module('insert_dividends')
        import insert_dividends
        t = insert_dividends.main()
        print("Add dividends-")
    elif ans == "F" or ans == 'f':
        print("Add firms")
        importlib.import_module('insert_firms_cl1')
        import insert_firms_cl1
        t = insert_firms_cl1.main()
        print("Add firms-")
    elif ans == "A" or ans == 'a':
        print("Add accounts")
        importlib.import_module('insert_account_cl2')
        import insert_account_cl2
        t = insert_account_cl2.main()
        print("Add accounts-")
    elif ans == "M" or ans == "m":
        print("return to main menu")
        importlib.import_module('menu')
        import menu
        t = menu()
        print("return")

    elif ans != "":
        print("Try again")
    elif ans == 'Q':
        break
