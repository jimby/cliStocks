#!/bin/bash
# MainMenu.sh
clear
PS3="Main Menu: please enter your choice"
options=("Edit menu" "Add menu" "Find menu" "Report menu" "Quit")


select opt in "${options[@]}"

# echo "$opt"
do

    case $opt in
        "Edit menu")
            echo "open EditMenu.sh"
            # python ./UpdatePrices.py
            ./EditMenu.sh
            break
            ;;
        "Add menu")
            echo "Insert Menu"
            ./insert_menu.py
	    break
            ;;

    "Find menu")
            echo "Find Menu"
	        # ./find_menu.sh
		./find_menu.sh
	        break
            ;;
        "Report menu")
            echo "Report Menu"
	        # ./report_menu.sh
	        report_menu.py
		break
            ;;
        "Quit") 
            echo "Quit now"
            # break
            # echo "$opt"
	    	exit 0
            ;;

        *) echo "invalid option $REPLY";;
    esac
    if [$opt -eq 5 ]; then
        break
    fi
done

