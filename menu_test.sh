#!/bin/bash
# Take two numbers
# echo "Enter a number"
# read n1
#echo "Enter a number"
# read n2

# Declare an infinite loop
while true
  do

    # Display the menu
    echo "menu_test.sh"
    echo " "
    echo "1. find_menu_test"
    echo "2. add_menu"
    echo "3. report_menu"
    echo "4. Division"
    echo "5. Exit"
    echo -n "choice:"
    read input

    # Perform the operation based on the selected value
    if [[ "$input" -eq "1" ]]
    then
      # echo $input
      ./find_menu_test.sh
      # ((result=n1+n2))
    elif [[ "$input" -eq "2" ]]
    then
      ((result=n1-n2))
    elif [[ "$input" -eq "3" ]]
    then
      ((result=$n1*$n2))
    elif [[ "$input" -eq "4" ]]
    then
      ((result=$n1/$n2))
    elif [[ "$input" -eq "5" ]]
    then
      echo "input: "
      echo $input
      break    # exit     #break
    else
      echo "Invalid input"
    fi
  # echo "The result is $result"
  done

clear
exit
