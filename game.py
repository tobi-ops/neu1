import random

def play():
    number = random.randint(1, 100)
    print(f"Die gesuchte Zahl ist: {number}")
    user_wins = False
    score = 0

    while not user_wins:
        score += 1

        try:
            guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            print("Falsche Eingabe!")
            continue

        if number == guess:
            print(f"Yes, {number} ist die gesuchte Zahl. Score: {score}")
            user_wins = True
        elif guess > number:
            print("Die gesuchte Zahl ist kleiner.")
        else:
            print("Die gesuchte Zahl ist größer.")

    save_score(score)


def save_score(score):
    try:
        with open("scores.txt", "a") as file:
            file.write(f"Score: {score}\n")
        print("Score erfolgreich gespeichert!")
    except Exception as e:
        print(f"Fehler beim Speichern des Scores: {e}")


while True:
    play()

    correctUserInput = False
    while not correctUserInput:
        prompt = input("Wollen Sie noch eine Runde spielen? [y/n] ")

        if prompt == 'n':
            exit()
        elif prompt == 'y':
            correctUserInput = True
        else:
            print("Falsche Eingabe, nur 'y' oder 'n' erlaubt.")