import random


number=random.randint(1,9)
chances=0



while chances < 5:
    guess=int(input('Guess any number between 1-9:'))
    if guess==number:
        print("You have won! Congratulations") 
        break
    elif guess<number:
        print("Your guess was too low. Guess a number higher than", guess)
    else:
        print("Your guess was too high.Guss a number lower than",guess)
    chances+=1
if not chances < 5:
    print("You lose!The number was ",number)



