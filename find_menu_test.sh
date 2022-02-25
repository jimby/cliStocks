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
      echo "find_menu_test.sh"
      echo " "
      echo "1. find_firm"
      echo "2. find_symbol"
      echo "3. "
      echo "4. "
      echo "5. Return"
      echo -n "choice:"
      read input
      echo $input
      # Perform the operation based on the selected value
      if [[ "$input" -eq "1" ]]
      then
          ./find_firm.sh
          # ((result=n1+n2))
      elif [[ "$input" -eq "2" ]]
      then
          ./find_symbol.sh
          # ((result=n1-n2))
      elif [[ "$input" -eq "3" ]]
      then
          ((result=$n1*$n2))
      elif [[ "$input" -eq "4" ]]
      then
          ((result=$n1/$n2))
      else
          break
      fi
    # echo "The result is $result"
done
    
clear
./menu_test.sh
