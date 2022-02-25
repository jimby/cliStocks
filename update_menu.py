#!/usr/bin/env python3
import importlib
import sys

ans = True
while ans:
    print("""
    update menu
        (P) update prices in prices table
        (M) return to main menu
        () Quit
    """)

    ans = input("choice: ")
    print(ans)
    if ans == "P" or ans == "p":
        print("\n update prices")
        importlib.import_module('UpdatePrices')
        import UpdatePrices
        t = UpdatePrices.main()
        print("UpdatePrices-")
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
