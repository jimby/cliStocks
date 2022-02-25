#!/bin/bash
# Bash Menu Script Example
PS3="please enter your choice"
options=("Edit" "Add" "Find" "Quit")
echo "Main Menu"
select opt in "${options[@]}"
do
        
    case $opt in
        "Edit")
            echo "open UpdatePrices.py"
            python ./UpdatePrices.py
            break
            ;;
        "Add")
            echo "you chose choice 2"
            break
            ;;
        
        "Find")
            echo "you chose choice $REPLY which is $opt"
	        ./find_menu.sh
	        break
            ;;
        "Quit")
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
    
done
clear
