#! /bin/bash
PS3="Please enter your choice"
options=("Find firm" "Find symbol" "return")
echo "Find Menu"
select opt in "${options[@]}"

do
        
    case $opt in
        "Find firm")
            echo "open Find Firms"
            ./find_firm.sh
            ;;
        "Find symbol")
            echo "Find symbols"
            ./find_symbol.sh
            ;;
        
        "return")
            echo "return to main menu"
            ./MainMenu.sh
            ;;    
        
        *) echo "invalid option $REPLY";;
    esac
    
done
clear
