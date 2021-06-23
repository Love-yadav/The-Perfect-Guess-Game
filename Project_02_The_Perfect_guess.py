import random

print("Computer choosed a number:from (1 to 100)")
randomnumber=random.randint(1,100)

print("\n")
print("now it is your turn:")
userguess=None
guesses=0
while randomnumber != userguess:
            userguess=int(input("enter the number from 1 to 100:"))
            guesses+=1
            if randomnumber==userguess:
                print("😊😊😊😊wow you choose the right number: Are you Mathes stuent ?")
            else:
                if(randomnumber>userguess):
                    print("you guessed it wrong please enter a larger number")
                else:
                    print("you guessed it wrong please enter the smaller number:")
            
            
print(f"you guess the number at :{guesses} guess")
with open("perfectguess.txt","r")as f:
    high=int(f.read())
    print(high)
    
if high>guesses:
    print("you have just broken the high score")
    with open("perfectguess.txt","w")as f:
         f.write(str(guesses))