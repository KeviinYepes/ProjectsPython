#fourth class Python ("Project")
import random as rd 
AskName = input("What's your name? ")
numeros = list(range(1,101))
SecretNumber = rd.choice(numeros)
print("I select a random number to 1 to 100 only for you. Try to guess it (You only have 8 LIVES)")
for i in range(1,9): 
    ask = int(input("Give me 1 number: "))
    if(ask < 1 or ask > 100):
        print("I said 1 to 100")
        break
    elif(ask < SecretNumber):
        print("Give me a higher number ⬆️")
    elif(ask > SecretNumber):
        print("Give me a lower number ⬇️")
    elif(ask == SecretNumber): 
        print(f"👏🏻That's correct {SecretNumber}👏🏻")
print(f"💀G4M3 0V3R U LOST ALL YOUR LIVES💀")
