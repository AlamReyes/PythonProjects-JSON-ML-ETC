import requests
import simplejson
import rdm
import html

url = "https://opentdb.com/api.php?amount=5&category=20&difficulty=medium&type=multiple"
endGame = ""
score_correct = 0
score_incorrect = 0
while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input(("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game"))
    else:
        valid_answer = False
        answer_number = 1
        data = simplejson.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        rdm.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\nType the number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answers. Use only numbers")

        user_answer = answers[int(user_answer) - 1]

        if user_answer == correct_answer:
            print("\nCongratulations! that's the correct answer " +  html.unescape(correct_answer))
            score_correct += 1
        else:
            print("Sorry," +  html.unescape(user_answer) + " is incorrect. The correct answer is " + html.unescape(correct_answer))
            score_incorrect += 1

        print("\n###########################")
        print("Your score is: ")
        print("Correct answers: " + str(score_correct))
        print("Incorrect answers: " + str(score_incorrect))
        print("##########################")

        endGame = input("\nPress enter to play again or type 'quit' to end the game: ").lower()

print("\nThanks for playing.")


