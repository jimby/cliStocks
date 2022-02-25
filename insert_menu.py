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
        importlib.import_module('cliAdd.insert_stocks')
        import add.insert_stocks
        t = add.insert_stocks.main()
        print("Add stocks-")
    elif ans == "P" or ans == "p":
        print("\nAdd prices")
        importlib.import_module('cliAdd.insert_prices')
        import add.insert_prices
        t = add.insert_prices.main()
        print("Add prices-")
    elif ans == "D" or ans == "d":
        print("\nAdd dividends")
        importlib.import_module('cliAdd.insert_dividends')
        import add.insert_dividends
        t = add.insert_dividends.main()
        print("Add dividends-")
    elif ans == "F" or ans == 'f':
        print("Add firms")
        importlib.import_module('cliAdd.insert_firms')
        import add.insert_firms
        t = add.insert_firms.main()
        print("Add firms-")
    elif ans == "A" or ans == 'a':
        print("Add accounts")
        importlib.import_module('cliAdd.insert_account')
        import add.insert_account
        t = add.insert_account.main()
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
