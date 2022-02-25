#!/usr/bin/env python3
import importlib

ans = True
while ans:
    print("""
        (A) Add stocks
        (E) Edit stocks
        (L) List securities
        (S) Reports
        (D) Add dividends
        (R) Reports
        () Quit
    """)

    ans = input("Data entry: ")
    print(ans)
    if ans == "A" or ans == "a":
        print("\n Add stocks")
        importlib.import_module('insert_stocks')
        import insert_stocks
        t = insert_stocks.main()
        print("add stocks-")
    elif ans == "E" or ans == "e":
        print("\nEdit stocks data")
        importlib.import_module('edit_stocks')
        import edit_stocks
        t = edit_stocks.main()
        # print("")
    elif ans == "L" or ans == "l":
        print("\nList securities data")
        importlib.import_module('list_stocks')
        import list_stocks
        t = list_stocks.main()
        # print("")
    # elif ans == "S":
        # print("Add stocks to file.")
        # importlib.import_module('insert_stocks')
        # import insert_stocks
        # t = insert_stocks.main()
        # print("Stocks Added-")
    # elif ans == "D":
        # print("Add dividends to file")
        # importlib.import_module('insert_dividends')
        # import insert_dividends
        # t = insert_dividends.main()
        # print("Dividends Added-")
    # elif ans == "R" or ans == "r":
        #print("report earnings")
        # importlib.import_module('report')
        # import report
        # report.main()
        # print("Report gains")

    elif ans != "":
        print("Try again")
    elif ans == 'Q':
        break
