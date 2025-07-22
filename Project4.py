#fourth class Python ("Project")
import random as rd 
AskName = input("What's your name? ")
numeros = list(range(1,101))
SecretNumber = rd.choice(numeros)
print("🎲 I’ve picked a secret number between 1 and 100! Can you guess it? You’ve got 8 ❤️ lives—don’t waste them!")
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
