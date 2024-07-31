import random

# Sample pool of questions
questions = [
    {
        "question": "What is the capital of France?",
        "correct_answer": "Paris",
        "wrong_answers": ["London", "Berlin", "Madrid"],
    },
    {
        "question": "What is 2 + 2?",
        "correct_answer": "4",
        "wrong_answers": ["3", "5", "6"],
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "correct_answer": "Harper Lee",
        "wrong_answers": ["Mark Twain", "F. Scott Fitzgerald", "Ernest Hemingway"],
    },
]


def ask_question():
    question_data = random.choice(questions)
    question = question_data["question"]
    correct_answer = question_data["correct_answer"]
    wrong_answers = question_data["wrong_answers"]

    # Combine and shuffle answers
    all_answers = wrong_answers + [correct_answer]
    random.shuffle(all_answers)

    # Display question and answers
    print("\n" + question)
    for i, answer in enumerate(all_answers):
        print(f"{i + 1}. {answer}")

    return correct_answer, all_answers


def main():
    print("Welcome to the Quiz App! Type 'quit' to exit at any time.")

    while True:
        correct_answer, all_answers = ask_question()

        # Get user input
        user_input = input("\nEnter the number of your answer: ")
        if user_input.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            break

        try:
            user_choice = int(user_input)
            if 1 <= user_choice <= 4:
                chosen_answer = all_answers[user_choice - 1]
                if chosen_answer == correct_answer:
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
