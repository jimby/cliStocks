#!/usr/bin/env python3
#find_menu.py

import importlib
import sys

ans = True
while ans:
    print("""
    find menu
        (F) find firm
        (H) find account
        (F) find stocks
        (M) return to main menu
        () Quit
    """)

    ans = input("choice: ")
    print(ans)
    if ans == "F" or ans == "f":
        print("\n find firm")
        importlib.import_module('find_firm_cl2')
        import find_firm_cl2
        t = find_firm_cl2.py
        print("find firm")
    elif ans == "H" or ans == "h":
        print("\nCurrent holding")
        importlib.import_module('cliReport.report_stocks')
        import report.report_stocks
        t = report.report_stocks.main()
        print("Edit data-")
    elif ans == "F" or ans == "f":
        print("\nFind data")
        importlib.import_module('cliFind.find_menu')
        import find_menu
        t = find_menu.main()
        print("Find menu-")
    # elif ans == "M" or ans == 'm':
    #      print("return to main menu")
    #      importlib.import_module('menu')
    #      import menu
    #      t = menu()
    #      print("return-")
    elif ans == "M" or ans == "m":
        print("return to main menu")
        importlib.import_module('menuNew')
        import menuNew
        t = menuNew.main()
        print("return")


    elif ans != "":
        print("Try again")
    elif ans == 'Q':
        break
