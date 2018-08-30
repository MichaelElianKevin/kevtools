#Developed by Michael Elian Kevin
#DON'T MODIFY ANYTHING FROM THIS PROJECT NOOBS
#IF U MODIFY THIS PROJECT, U ARE A FUCKING NOOBS KID
#DON'T SELL THIS PROJECT, THIS IS TOTALLY FREE, BUT DON'T MODIFY THIS

import os;

#header
h = open('header.txt', 'r');
header = h.read();
print(header);
h.close();

#main menu
menu = {};
menu[1]="Menu 1";
menu[2]="Menu 2";
menu[97]="Contribute";
menu[98]="About";
menu[99]="Exit";

#print menu
while True:
 print("");
 options=menu.keys();
 options.sort();
 for entry in options:
  print({entry}, menu[entry]);
   
#menu selection
 selection=raw_input("Choose: ");
 if selection == '1':
  os.system("shutdown -h now");
 elif selection == '2':
  print("Please wait until first version of this project released.");
 elif selection == '3':
  print("""
   Developer : Michael Elian Kevin
   Version   : Debug
    
   ***DON'T CHANGE THIS NOOBS***""");
 elif selection == '99':
  break
 else:
  print("You are STUPID and NOOBS. Choose correct menu.");
