import random
Win = False
def chiffremystere():
    intmystere = []
    for i in range(4):
        intmystere.append(random.randint(1, 6))
    return intmystere

def play():
    guesses = []
    for t in range(4):
        while True:
            x = int(input("Make a guess for the color of ball position: {}\n".format(t + 1)))
            if x > 6 or x < 1 or type(x) != int:
                "Make a guess for the color of ball position: {}\nit's supposed to be a number between 1 and 6".format(
                    t + 1)
            else:
                # cas où la valeur entré est valide
                # sortie de boucle while
                break
        guesses.append(x)
    return guesses

def Mastermind(tries=12,toGuess=chiffremystere()):
    Win = False
    if tries == 0:
        return print("You are out of tries, you can retry playing by typing : 'yes'\nin console log")
    while Win != True:
        print("you have {} tries to guess the position and color of 4 different balls \n".format(tries))
        print(toGuess)
        Guesses = play()
        print(Guesses)
        common_elements = list(set(toGuess).intersection(Guesses))
        perfect = 0
        for i in range(4):
            if int(Guesses[i]) == toGuess[i]:
                perfect += 1
                pass
        print("You found {} perfect position".format(perfect))
        print("and there's {} ballz with common colors\n \n".format(len(common_elements) - perfect))
        tries = tries - 1
        
        if perfect == 4:
            Win = True
            print("You won !\n the right code was actually\n {}".format(toGuess))
        else:
            Mastermind(tries-1,toGuess)
            
Mastermind()
