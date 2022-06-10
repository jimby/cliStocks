# menu4.sh
# bash menu with two sub-menus
submenu1 () {
  
  local PS3='edit menu: '
  local options=("EditAddCurrentPrices.py" "Sub menu1 item 2" "Sub menu1 quit")
  local opt
  clear
  echo 'edit menu'
  select opt in "${options[@]}"
  do
      case $opt in
          "EditAddCurrentPrices.py")
              echo "waiting ..."
              /home/jim/projects/cliStocks/EditAddCurrentPrices.py
              ;;
          "Sub menu1 item 2")
              echo "you chose submenu1 item 2"
              ;;
          "Sub menu1 quit")
              return

              ;;
          *) echo "invalid option $REPLY";;
      esac
  done
}

# submenu2
submenu2 () {
  
  local PS3='add menu: '
  local options=("Sub menu2 item 1" "Sub menu2 item 2" "Sub menu2 quit")
  local opt
  clear
  echo 'add menu'
  select opt in "${options[@]}"
  do
      case $opt in
          "Sub menu2 item 1")
              echo "you chose submenu2 item 1"
              ;;
          "Sub menu2 item 2")
              echo "you chose submenu2 item 2"
              ;;
          "Sub menu2 quit")
              return
              ;;
          *) echo "invalid option $REPLY";;
      esac
  done
}

# submenu3
submenu3 () {
  
  local PS3='find menu: '
  local options=("Sub menu3 item 1" "Sub menu3 item 2" "Sub menu3 quit")
  local opt
  clear
  echo 'find menu'
  select opt in "${options[@]}"
  do
      case $opt in
          "Sub menu3 item 1")
              echo "you chose submenu3 item 1"
              ;;
          "Sub menu3 item 2")
              echo "you chose submenu3 item 2"
              ;;
          "Sub menu3 quit")
              return
              ;;
          *) echo "invalid option $REPLY";;
      esac
  done
}

# submenu4
submenu4 () {
  
  local PS3='find menu: '
  local options=("Sub menu4 item 1" "Sub menu4 item 2" "Sub menu4 quit")
  local opt
  clear
  echo 'find menu'
  select opt in "${options[@]}"
  do
      case $opt in
          "Sub menu4 item 1")
              echo "you chose submenu3 item 1"
              ;;
          "Sub menu4 item 2")
              echo "you chose submenu3 item 2"
              ;;
          "Sub menu4 quit")
              return
              ;;
          *) echo "invalid option $REPLY";;
      esac
  done
}

# main menu

PS3='main menu'
options=("Main menu item 1" "Edit menu" "Submenu3" "Submenu4" "Main menu quit")
clear
echo 'main menu'
select opt in "${options[@]}"
do
    case $opt in
        "Main menu item 1")
            echo "you chose main item 1"
            ;;
    	"Edit menu")
            submenu1
            ;;
        "Submenu2")    
            submenu2
            ;;
                        
        "Submenu3")    
            submenu3
            ;;
        
        "Submenu4")    
            submenu4
            ;;

        "Main menu quit")
            clear       
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac

done
