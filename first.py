 #!/usr/bin/env python
# -*- coding: utf-8 -*-
age = input("How old are you?\n")
if age <= 7:
    print("You are baby")
elif 7 < age <= 18:
    print("You should study in school")
elif 18 < age <= 25:
    print("Welcom to University")
elif 25 < age <= 60:
    print("Do you work?")
elif 60 < age <= 120:
    print("You can have a rest all day long")
else: 
    print("Warning! \n")*5
    print("This is programm for humans")
    
raw_input()



x = int(input("Enter number from 1 to 9\n"))
if x <=3:
   s = str(input("Enter several numbers\n"))
   n = int(input("How many times repeat?\n"))
   print(s*n)

elif 4 <= x <= 6:
    m = input("Raising to the power  \n")
    print x**m

elif 7 <= x <= 9:
    z = 0
    while z < 10:
        x = x + 1
        z = z + 1
        print(x)
else:
    print("Error")

raw_input()