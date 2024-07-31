import asyncio
from application.quiz_service import QuizService
from domain.value_objects import QuizResult


class CLI:
    def __init__(self, quiz_service: QuizService):
        self.quiz_service = quiz_service

    async def run(self) -> None:
        print(
            "Welcome to the Extremely Overengineered Quiz App! Type 'quit' to exit at any time."
        )
        self.quiz_service.start_quiz()

        while True:
            question = self.quiz_service.get_next_question()
            print(f"\n{question.get_text()}")
            for i, answer in enumerate(question.get_answers()):
                print(f"{i + 1}. {answer.text}")

            user_input = await self.get_user_input(
                "\nEnter the number of your answer: "
            )
            if user_input.lower() == "quit":
                break

            try:
                user_choice = int(user_input) - 1
                if 0 <= user_choice < len(question.get_answers()):
                    is_correct = self.quiz_service.submit_answer(user_choice)
                    if is_correct:
                        print("Correct!")
                    else:
                        print(
                            f"Wrong! The correct answer was: {next(a.text for a in question.get_answers() if a.is_correct)}"
                        )
                else:
                    print("Invalid choice. Please select a valid answer number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        result = self.quiz_service.end_quiz()
        print(
            f"Thanks for playing! Your final score: {result.correct_answers}/{result.total_questions}"
        )
        print(f"Time taken: {result.duration:.2f} seconds")

    async def get_user_input(self, prompt: str) -> str:
        return await asyncio.get_event_loop().run_in_executor(None, input, prompt)
