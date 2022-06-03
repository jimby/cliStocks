#!/bin/bash
# MainMenu.sh

PS3="please enter your choice"
options=("Edit menu" "Add menu" "Find menu" "Report menu" "Quit")
clear
echo "Main Menu"
select opt in "${options[@]}"
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
            break
            ;;

        "Find menu")
            echo "Find Menu"
	        # ./find_menu.sh
	        break
            ;;
        "Report menu")
            echo "Report Menu"
	        # ./find_menu.sh
	        break
            ;;
        "Quit") 
	    echo "Quit now"
	    break
	    echo "break doesn't work!"
		# exit 0
            ;;

        *) echo "invalid option $REPLY";;
    esac

done

