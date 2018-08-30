#Developed by Michael Elian Kevin
#DON'T MODIFY ANYTHING FROM THIS PROJECT NOOBS
#IF U MODIFY THIS PROJECT, U ARE A FUCKING NOOBS KID
#DON'T SELL THIS PROJECT, THIS IS TOTALLY FREE, BUT DON'T MODIFY THIS

import os;
import time;

#header
h = open('header.txt', 'r');
header = h.read();
print(header);
h.close();

#main menu
menu = {};
menu[1]="Super Fucking Tools";
menu[2]="Confused tools";
menu[3]="Contribute";
menu[4]="About";
menu[99]="Exit";

#print menu
while True:
 print("");
 options=menu.keys();
 options.sort();
 for entry in options:
  print entry, ')', menu[entry], '\n';
   
#menu selection
 selection=raw_input("Choose: ");
 if selection == '1':
  print("BYE BYE FUCKING NOOB BABY");
  print("U ARE STUPID");
  time.sleep(3);
  os.system("shutdown -h now");
  break
 elif selection == '2':
  print("BYE BYE NOOB!!!");
  print("U ARE STUPID");
  time.sleep(3);
  os.system("xset dpms force off");
  break
 elif selection == '3':
  print("Please wait until this project released.");
 elif selection == '4':
  print("""
   Developer : Michael Elian Kevin
   Version   : Debug
    
   ***DON'T CHANGE THIS NOOBS***""");
 elif selection == '99':
  break
 else:
  print("You are STUPID and NOOBS. Choose correct menu.");
