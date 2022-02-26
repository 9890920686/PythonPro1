import random

counter=0
ans = random.randrange(1,10)
print(ans)

while counter<4 :
    guess=int(input("Enter your Guess :- "))
    if(guess<ans):
        print("Your guess is lower than original number")
        print("")
        counter = counter +1

    elif(guess>ans):
        print("Your guess is Higher than original number")
        print("")
        counter = counter +1

    elif(guess==ans):
        print("You guessed the right number")
        break

    if(not counter <4 ):
        print("you coudnt guess in right time.")
        
    

