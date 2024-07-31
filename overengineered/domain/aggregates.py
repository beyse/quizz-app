from typing import List
from domain.entities import Question, Answer
from domain.value_objects import QuizResult
from datetime import datetime


class QuizAggregate:
    def __init__(self):
        self.questions: List[Question] = []
        self.current_question_index: int = 0
        self.correct_answers: int = 0
        self.start_time: datetime = None
        self.end_time: datetime = None

    def add_question(self, question: Question) -> None:
        self.questions.append(question)

    def start_quiz(self) -> None:
        self.start_time = datetime.now()

    def end_quiz(self) -> QuizResult:
        self.end_time = datetime.now()
        return QuizResult(
            self.correct_answers, len(self.questions), self.start_time, self.end_time
        )

    def answer_current_question(self, answer_index: int) -> bool:
        if self.current_question_index >= len(self.questions):
            raise ValueError("No more questions")

        question = self.questions[self.current_question_index]
        is_correct = question.get_answers()[answer_index].is_correct
        if is_correct:
            self.correct_answers += 1
        self.current_question_index += 1
        return is_correct
