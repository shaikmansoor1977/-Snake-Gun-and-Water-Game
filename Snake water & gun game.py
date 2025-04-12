"PROJECT 1"
"""SNAKE WATER & GUN GAME"""

import random                              #importing random function
name=input("ENTER NAME OF THE PLAYER : ")  #taking name of player as input                                               
computer=random.choice([-1,1,0])           #shuffle the numbers using random
youstr=input("ENTER YOUR CHOICE : ")       #taking choice from given option as input 
youstrdict={"snake":1,"water":-1,"gun":0}  #created a dictonary for words and values
reversedict={1:"snake",-1:"water",0:"gun"} #reverse that dictionary

you=youstrdict[youstr]                     #assaining choise input in dictonary which is asssin to variable you

print(f"YOU CHOSE : {reversedict[you]}\nCOMPUTER CHOSE : {reversedict[computer]}")       #it is used to show whom chose waht
if (computer==you):                                                                   #all below code is related to conditional statements which you know alrady
    print("IT IS DRAW")
else:
    if (computer==-1 and you==1):
        print("DEAR",name,"YOU WIN THIS : BECAUSE SNAKE WILL DRINK'S THE WATER !!!")
    elif (computer==-1 and you==0):
        print("COMPUTER WINS : BECAUSE GUN WILL BE SINK IN WATER !!!")

    elif (computer==1 and you==-1):
        print("COMPUTER WINS : BECAUSE SNAKE DRINKS WATER !!!")
    elif (computer==1 and you==0):
        print("DEAR",name,"YOU WIN THIS : BECAUSE WE CAN SHOOT SNAKE WITH GUN !!!")

    elif(computer==0 and you==-1):
        print("DEAR",name,"YOU WIN THIS : BECAUSE GUN WILL BE SINK IN WATER !!!")
    elif (computer==0 and you==1):
        print("COMPUTER WINS : BECAUSE WE CAN SHOOT SNAKE WITH GUN !!!")
    else:
        print("something went wrong")

