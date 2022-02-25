#! /bin/bash


while [ 1 ]
do
CHOICE=$(
whiptail --title "Edit data" --menu "Make your choice" 16 100 9 \
    "1)" "find firms."   \
    "2)" "find accounts."  \
    "3)" "find stock symbols." \
    "4)" "unused" \
    "5)" "main menu" \
    "6)" "Number of interupts in the last secound." \
    "9)" "exit"  3>&2 2>&1 1>&3   
)


result=$(whoami)
case $CHOICE in
    "1)")   
        # python ./find_firm.py
    ;;
    "2)")   
            
        result="unused"
    ;;

    "3)")   
            
        result="unused"
        ;;

    "4)")   
        result="unused"
        ;;

    "5)")   
        # result="main menu"
        ./whipTailMainMenu.sh
        break
        ;;

    "6)")   
        interupts
        read -r result < result
        ;;

    "9)") exit
        ;;
esac
whiptail --msgbox "$result" 20 78
done
exit
