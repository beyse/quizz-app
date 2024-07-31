from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar
from dataclasses import dataclass
from uuid import UUID, uuid4

T = TypeVar("T")


class Entity(Generic[T], ABC):
    def __init__(self, id: UUID):
        self._id = id

    @property
    def id(self) -> UUID:
        return self._id


@dataclass
class Answer(Entity[str]):
    text: str
    is_correct: bool

    def __init__(self, text: str, is_correct: bool):
        super().__init__(uuid4())
        self.text = text
        self.is_correct = is_correct


class Question(Entity[str], ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def get_answers(self) -> List[Answer]:
        pass


@dataclass
class SimpleQuestion(Question):
    text: str
    answers: List[Answer]

    def __init__(self, text: str, answers: List[Answer]):
        super().__init__(uuid4())
        self.text = text
        self.answers = answers

    def get_text(self) -> str:
        return self.text

    def get_answers(self) -> List[Answer]:
        return self.answers
