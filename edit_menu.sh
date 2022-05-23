#!/bin/bash
PS3="Please enter your choice"
options=("edit prices" "edit firms" "edit stocks" "edit accounts" "main menu")
echo "Edit Menu"
select opt in "${options[@]}"
do

    case $opt in
        "edit prices")
            echo "EditAddCurrentprices.py"
            python ./EditAddCurrentPrices.py
	    break
            ;;
        "edit firms")
            echo "edit menu"
            ./EditMenu.sh
            break
            ;;
        "edit stocks")
            echo "edit menu"
            ./EditMenu.sh
            break
            ;;
        "edit accounts")
            echo "edit menu"
            ./EditMenu.sh
            break
            ;;
          "main menu")
            echo "return to main menu"
            ./menu.sh
            ;;

        *) echo "invalid option $REPLY";;
    esac

done
clear
