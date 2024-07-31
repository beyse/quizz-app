from typing import List
from domain.aggregates import QuizAggregate
from domain.entities import Question
from domain.value_objects import QuizResult
from application.event_bus import EventBus
from application.command_bus import CommandBus, SubmitAnswerCommand
from application.mediator import Mediator
from infrastructure.repositories import QuestionRepository
from infrastructure.logging_service import LoggingService
from infrastructure.caching_service import CachingService


class QuizService:
    def __init__(
        self,
        question_repo: QuestionRepository,
        event_bus: EventBus,
        command_bus: CommandBus,
        mediator: Mediator,
        logger: LoggingService,
        cache: CachingService,
    ):
        self.question_repo = question_repo
        self.event_bus = event_bus
        self.command_bus = command_bus
        self.mediator = mediator
        self.logger = logger
        self.cache = cache
        self.quiz_aggregate = QuizAggregate()

    async def start_quiz(self) -> None:
        self.logger.log("Quiz started")
        await self.event_bus.publish("quiz_started")
        self.quiz_aggregate.start_quiz()

    async def get_next_question(self) -> Question:
        cache_key = f"question_{self.quiz_aggregate.current_question_index}"
        cached_question = self.cache.get(cache_key)
        if cached_question:
            return cached_question

        question = self.question_repo.get_random_question()
        self.quiz_aggregate.add_question(question)
        self.cache.set(cache_key, question)
        await self.event_bus.publish("question_presented", question)
        return question

    async def submit_answer(self, answer_index: int) -> bool:
        command = SubmitAnswerCommand(answer_index)
        return self.command_bus.handle(command)

    async def end_quiz(self) -> QuizResult:
        result = self.quiz_aggregate.end_quiz()
        self.logger.log(
            f"Quiz ended. Score: {result.correct_answers}/{result.total_questions}"
        )
        await self.event_bus.publish("quiz_ended", result)
        return result
