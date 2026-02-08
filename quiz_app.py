def run_quiz(questions: list) -> None:
    """
    Run a multiple-choice quiz and track the user's score.
    """
    score = 0

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {question['answer']}")

    print(f"\n🎯 Quiz Finished! Your score: {score}/{len(questions)}")


def main():
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility",
                "D. Control Processing Unit"
            ],
            "answer": "A"
        },
        {
            "question": "Which language is commonly used for AI?",
            "options": [
                "A. HTML",
                "B. CSS",
                "C. Python",
                "D. SQL"
            ],
            "answer": "C"
        }
    ]

    print("🧠 Welcome to the Quiz App!")
    run_quiz(questions)


if __name__ == "__main__":
    main()
