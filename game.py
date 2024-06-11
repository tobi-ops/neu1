import random



def play():

def save_score(score):
    pass


    while True:
        number = random.randint(1, 100)
        print(f"DEBUG: number ist {number}")
        user_wins = False
        anzahl = 0

        while not user_wins:
            anzahl += 1
            try:
                guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
                if guess < 1 or guess > 100:
                    raise ValueError
            except ValueError:
                print("Ungültige Eingabe! Bitte geben Sie eine Zahl zwischen 1 und 100 ein.")
                continue

            if number == guess:
                print(f"Ja, {number} ist die richtige Zahl! Du hast {anzahl} Versuche gebraucht.")
                user_wins = True
                print(f"Dein Highscore ist {anzahl}")
            elif number > guess:
                print("Die Zahl ist zu klein.")
            else:
                print("Die Zahl ist zu groß.")

#    restart = input("Möchten Sie das Spiel neu starten? (ja/nein): ").strip().lower()
#    if restart != 'ja':
#        print("Danke fürs Spielen! Auf Wiedersehen!")
#        break

while True:
    play()

    correctUserInput = False
    while correctUserInput:
        prompt = input("Wollen Sie noch eine Runde spielen y/n?")
        if prompt == "n":
            exit()
        elif prompt == "y":
            correctUserInput = True
        else:
            print("falsche eingabe nur y oder n erlaubt")