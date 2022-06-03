#!/usr/bin/env python3
import importlib

def edit_menu():
    ans = True
    while ans:
        print("""Edit Menu
        (F) Edit firm file
        (A) Edit account file
        (S) Edit stocks file
        (D) Edit dividends
        (M) return to main menu""")
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
            # del edit_menu
            print("return to main menu")
            importlib.import_module('MainMenu')
            import MainMenu
            t = MainMenu.main()
            # print("return")

def main():
    edit_menu()
    
if __name__ == '__main__':
        main()
