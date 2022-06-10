#!/usr/bin/env python3
import importlib
# import subprocess

class Menu:

    def main_menu(self):
        ans = True
        while ans:
            print("""
        Main Menu
            (E) Edit menu
            (A) Add menu
            (F) find menu
            (R) report menu
            (R) return to main menu
            (Q) Quit
        """)

            ans = input("choose: ")
            print('choice: ',ans)
            if ans == "E" or ans == "e":
                print("\n Edit menu")
                t = self.edit_menu()

            elif ans == "A" or ans == "a":
                print("\nAdd menu")
                importlib.import_module('insert_menu')
                import insert_menu
                t = insert_menu
                print("add menu")
            elif ans == "F" or ans == "f":
                print("find menu")
                importlib.import_module('find_menu')
                import find_menu
                t = find_menu.main()
                print("find menu")
            elif ans == "R" or ans == "r":
                print("report menu")
                importlib.import_module('report_menu')
                import report_menu
                t = report_menu.main()
                print("report menu-")
            elif ans == 'Q' or ans == 'q':
                print("Ans: ", ans)
                break


    def edit_menu(self):
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


    def insert_menu(self):
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


    def report_menu(self):
        ans = True
        while ans:
            print("""
            report menu
                (G) report gains
                (H) current holdings
                (F) Find data
                (M) return to main menu
                () Quit
            """)

            ans = input("choice: ")
            print(ans)
            if ans == "G" or ans == "g":
                print("\n report gains")
                importlib.import_module('cliReport.report_gains')
                import report.report_gains
                t = report.report_gains.main()
                print("Add data-")
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

                # print("return")

        # if ans == 'Q' or  ans == 'q':
        #     break


def main():
    m = Menu()                                                  # class declaration Menu
    mm = m.main_menu()                                          # main menu
    
if __name__ == '__main__':
        main()
