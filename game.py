import random
computer = random.choice([1 , -1 , 0])
hstr =input("Enter your choice: ")
hDict ={"s" : 1 , "c" : -1 , "p" : 0}
reverseDict= {1:"stone"  , -1 :"scissor"  , 0 :"paper" }

h = hDict[hstr]

print(f"You choose {reverseDict[h]}\nComputer choose {reverseDict[computer]}")

if(computer == h):
    print("it a draw")
else:    

 if(h ==1 and computer==-1):
    print("you win")

 elif(h==-1 and computer==1):
    print("you lost")

 elif(h==1 and computer==-0):
    print("you lost")

 elif(h==0 and computer==1):
    print("you win")

 elif(h==0 and computer==-1):
    print("you lost")
    
 elif(h==-1 and computer==-0):
    print("you win")
    
    