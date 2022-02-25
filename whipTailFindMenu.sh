#! /bin/bash


while [ 1 ]
do
CHOICE=$(
whiptail --title "Find data menu" --menu "Make your choice" 16 100 9 \
    "1)" "find firms."   \
    "2)" "find symbol"  \
    "3)" "unused" \
    "4)" "unused" \
    "5)" "main menu" \
    "6)" "unused" \
    "9)" "exit"  3>&2 2>&1 1>&3   
)


# result=$(whoami)
case $CHOICE in
    "1)")   
        python3 ./find_firm_cl2.py
    ;;
    "2)")   
        python3 ./find_symbol_cl.py
        # result="unused"
    ;;

    "3)")   
            
        result="unused"
        ;;

    "4)")   
        result="unused"
        ;;

    "5)")   
        result="main menu"
        ./whipTailMainMenu.sh
        break
        ;;

    "6)")   
        # interupts
        # read -r result < result
        result="unused"
        ;;

    "9)") exit
        ;;
esac
# whiptail --msgbox "$result" 20 78
done
exit
