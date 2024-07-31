import random
from typing import List
from domain.entities import Question, SimpleQuestion, Answer
from infrastructure.database import Database


class QuestionRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_random_question(self) -> Question:
        questions = self.database.get_all_questions()
        return random.choice(questions)

    def add_question(self, question: Question) -> None:
        self.database.add_question(question)
