import random
'''1=snake
0= water
-1= gun'''

computer = random.choice([0,1,-1])

youstr= input("enter your choice: ")

youDict={"s":1, "w":0, "g":-1}
reversedDict={1:"snake", 0:"water", -1:"gun"}

you=youDict[youstr]

print(f"you chose:{reversedDict[you]} \ncomputer chose: {reversedDict[computer]}")

if(you==computer):
    print("its a draw!")
else:
    if(you==1 and computer==0):
        print("You won!")
    elif(you==0 and computer==1):
        print("You lose!")
    elif(you==-1 and computer==0):
        print("You won!")
    elif(you==0 and computer==-1):
        print("You lose!")
    elif(you==1 and computer==-1):
        print("You lose!")
    elif(you==-1 and computer==1):
        print("You won!")
    else:
        print("somthing went wrong")


