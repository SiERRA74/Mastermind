import random

def chiffremystere():
    intmystere = []
    for i in range(4):
        intmystere.append(random.randint(1,6))
    return intmystere

def play():
    guesses = []
    for t in range(4):
        x = int.input("Make a guess for the color of ball position: {}\n".format(t+1))
        guesses.append(x)
    return guesses
        
        
Win = False

while Win != True:
    toGuess = chiffremystere()
    print("you have 12 tries to guess the position and color of 4 different balls \n")
    print(toGuess)
    Guesses = play()
    print(guesses)
    common = []
    common_elements = list(set(common).intersection(toGuess, Guesses))


    perfect = 0
    for i in range(4):
            if Guesses[i] == toGuess[i]:
                perfect += 1
    
    print("You found {} perfect position".format(perfect))
    print("and there's {} ballz with common colors".format(common_elements))
    
    Win = True
