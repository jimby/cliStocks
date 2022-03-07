g#! /bin/bash


while [ 1 ]
do
CHOICE=$(
whiptail --title "Main Menu" --menu "Make your choice" 16 100 9 \
    "1)" "find data."   \
    "2)" "edit data."  \
    "3)" "add data." \
    "4)" "unused" \
    "5)" "unused" \
    "6)" "unused" \
    "9)" "quit"  3>&2 2>&1 1>&3   
)


# result=$(whoami)
case $CHOICE in
    "1)")   
        ./whipTailFindMenu.sh
        break
        
    ;;
    "2)")   
            
        result="edit data"
    ;;

    "3)")   
            
        result="add data"
        ;;

    "4)")   
        result="unused"
       
        ;;

    "5)")   
        result="unused"
        ;;

    "6)")   
        result="unused"
        ;;

    "9)") exit
        ;;
esac
# whiptail --msgbox "$result" 20 78
done
clear
exit
