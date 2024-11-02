def brain_quiz():
    questions = {
        "What is the capital of France?": {
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        "What is 5 + 7?": {
            "options": ["A) 10", "B) 12", "C) 14", "D) 15"],
            "answer": "B"
        },
        "What is the largest mammal in the world?": {
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "answer": "B"
        },
        "In which year did the Titanic sink?": {
            "options": ["A) 1905", "B) 1912", "C) 1915", "D) 1920"],
            "answer": "B"
        },
    }

    score = 0
    total_questions = len(questions)

    print("Welcome to the Brain Quiz!")
    print("Please answer the following questions:\n")

    for question, details in questions.items():
        print(question)
        for option in details["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == details["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {details['answer']}.\n")

    print(f"Quiz complete! Your score is {score} out of {total_questions}.")

if __name__ == "__main__":
    brain_quiz()
