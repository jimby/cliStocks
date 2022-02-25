#!/usr/bin/env python3
import importlib

ans = Truef
while ans:add mysql to visual studio code
    print("""
        (F) Edit firm file
        (A) Edit account file
        (S) Edit stocks file
        (D) Edit dividends
        (M) return to main menu
        () Quit
    """)

    ans = input("Data entry: ")
    print(ans)
    if ans == "F" or ans == "f":
        print("\n Add an investing firm")
        importlib.import_module('insert_firms')
        import insert_firms
        t = insert_firms.main()
        print("Firm Added-")
    elif ans == "A" or ans == "a":
        print("Add an account")
        importlib.import_module('insert_accounts')
        import insert_accounts
        t = insert_firms.main()
        print("Account added")
    elif ans == "S" or ans == "s":
        print("edit stocks.")
        importlib.import_module('cliEdit.edit_stocks')
        import edit.edit_stocks
        t = edit.edit_stocks.main()
        print("edit stocks-")
    elif ans == "D" or ans == "d":
        print("Add dividends to file")
        importlib.import_module('insert_dividends')
        import insert_dividends
        t = insert_dividends.main()
        print("Dividends Added-")
    elif ans == "M" or ans == "m":
        print("return to main menu")
        importlib.import_module('menu')
        import menu
        t = menu()
        print("return")

    # elif ans == "R" or ans == 'r':
    #     print("return to main menu")
    #     importlib.import_module('menu')
    #     import menu
    #     t = menu()
    #     print("return")
    elif ans != "":
        print("Try again")
    elif ans == 'Q':
        break
