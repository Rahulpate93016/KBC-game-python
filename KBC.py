import random

questions = {
    "Who invented telephone?": {
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
        "answer": "Alexander Graham Bell"
    },
    "What is the currency of Japan?": {
        "options": ["Yuan", "Yen", "Dollar", "Euro"],
        "answer": "Yen"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Jupiter", "Mars", "Venus", "Mercury"],
        "answer": "Mars"
    },
    "Who is the current CEO of Google?": {
        "options": ["Jeff Bezos", "Tim Cook", "Sundar Pichai", "Mark Zuckerberg"],
        "answer": "Sundar Pichai"
    },
    "What is the capital of Australia?": {
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    }
}

prize_money = {
    1: 5000,
    2: 10000,
    3: 20000,
    4: 40000,
    5: 80000,
    6: 160000,
    7: 320000,
    8: 640000,
    9: 1250000,
    10: 2500000,
    11: 5000000,
    12: 10000000
}

def ask_question(question):
    options = questions[question]["options"]
    random.shuffle(options)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        answer = input("Enter your answer (A/B/C/D): ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Invalid answer, please try again.")
    user_answer = options[ord(answer) - ord("a")]
    correct_answer = questions[question]["answer"]
    if user_answer == correct_answer:
        print("Congratulations, you have won Rs.", prize_money[list(questions.keys()).index(question) + 1])
        return True
    else:
        print("Sorry, that is incorrect.")
        return False

print("Welcome to KBC!")
print("Answer 12 questions correctly to win Rs. 1 crore.")

question_numbers = list(range(1, 13))
random.shuffle(question_numbers)
for i, question_number in enumerate(question_numbers):
    question = list(questions.keys())[i]
    if ask_question(question):
        continue
    else:
        print("Game Over!")
        break
else:
    print("Congratulations, you have won Rs. 1 crore!")
