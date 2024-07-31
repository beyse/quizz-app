from typing import List, Dict
from domain.entities import Question, SimpleQuestion, Answer


class Database:
    def __init__(self):
        self.questions: Dict[str, Question] = {}

    def add_question(self, question: Question) -> None:
        self.questions[str(question.id)] = question

    def get_question(self, question_id: str) -> Question:
        return self.questions.get(question_id)

    def get_all_questions(self) -> List[Question]:
        return list(self.questions.values())
