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
            echo "edit firms"
            ./edit_firms_cl2.py
            break
            ;;
        "edit stocks")
            echo "edit stocks"
            ./edit_stocks.py
            break
            ;;
        "edit accounts")
            echo "edit accounts"
            ./edit_accts_cls2.py
            break
            ;;
          "main menu")
            echo "return to main menu"
            ./menu.sh
            ;;

        *) echo "invalid option $REPLY";;
    esac

done

