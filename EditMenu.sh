#!/bin/bash
#Editmenu
PS3="please enter your choice"
options=("EditAddCurrentPrice" "test")
echo "Edit Menu"
select opt in "${options[@]}"
do 
  case $opt in 
  	"test")
  		echo "test"
  		break
  		;;
  	esac
done
