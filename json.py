import requests
import simplejson
import time
print("This is a quiz program about greek mythology")
r = requests.get("https://opentdb.com/api.php?amount=5&category=20&difficulty=medium&type=multiple")
quiz = simplejson.loads(r.text)
mistakes =0
corrects =0
questions = ["A minotaur is half human half what?", "According to the Egyptian Myth of Osiris, who murdered Osiris?", "In African mythology, Anansi is a trickster and storyteller who takes the shape of which animal?", "Hel was the daughter of which Norse Mythological figure?", "What animal did Queen Pasipahe sleep with before she gave birth to the Minotaur in Greek Mythology?"]
print(input("Press enter and the game will start in 5 sec."))
time.sleep(5)
nquestions = []
while len(nquestions) < 5:
    print("The first question is:")
    print(questions[0])
    guess = input()
    if guess.lower() == "bull":
        corrects += 1
        print("The answer is correct!!")
    else:
        mistakes += 1
        print("The answer is incorrect!!")
    play_again = input("Let's play another round?. Type 'no' to quit")

    if play_again.lower() == 'no':
        break



    print("The next question is:")
    print(questions[1])
    guess = input()
    if guess.lower() == "set":
        corrects += 1
        print("The answer is correct!!")
    else:
        mistakes += 1
        print("The answer is incorrect!!")
    play_again = input("Let's play another round?. Type 'no' to quit, else just press enter")

    if play_again.lower() == 'no':
        break


    print("The next question is:")
    print(questions[2])
    guess = input()
    if guess.lower() == "spider":
        corrects += 1
        print("The answer is correct!!")
    else:
        mistakes += 1
        print("The answer is incorrect!!")
    play_again = input("Let's play another round?. Type 'no' to quit, else just press enter")

    if play_again.lower() == 'no':
        break


    print("The next question is:")
    print(questions[3])
    guess = input()
    if guess.lower() == "loki":
        corrects += 1
        print("The answer is correct!!")
    else:
        mistakes += 1
        print("The answer is incorrect!!")
    play_again = input("Let's play another round?. Type 'no' to quit, else just press enter")

    if play_again.lower() == 'no':
        break


    print("The final question is:")
    print(questions[4])
    guess = input()
    if guess.lower() == "bull":
        corrects += 1
        print("The answer is correct!!")
    else:
        mistakes += 1
        print("The answer is incorrect!!")
    break

print("Thanks for playing!!", " You made " + str(mistakes) + " mistakes", " and you have " + str(corrects) + " correct answers")








