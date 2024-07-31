from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class QuizResult:
    correct_answers: int
    total_questions: int
    start_time: datetime
    end_time: datetime

    @property
    def duration(self) -> float:
        return (self.end_time - self.start_time).total_seconds()
