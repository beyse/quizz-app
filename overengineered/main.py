# main.py
import os
import sys

# Ensure the application directory is in the PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "application"))

import asyncio
from application.quiz_service import QuizService
from application.event_bus import EventBus
from application.command_bus import CommandBus
from application.mediator import Mediator
from infrastructure.repositories import QuestionRepository
from infrastructure.logging_service import LoggingService
from infrastructure.caching_service import CachingService
from domain.entities import SimpleQuestion, Answer
from application.command_bus import SubmitAnswerCommand
from infrastructure.database import Database
from presentation.cli import CLI


async def main():
    # Set up dependencies
    database = Database()
    event_bus = EventBus()
    command_bus = CommandBus()
    mediator = Mediator()
    question_repo = QuestionRepository(database)
    logger = LoggingService()
    cache = CachingService()

    # Set up event listeners
    event_bus.subscribe("quiz_started", lambda _: logger.log("Quiz started"))
    event_bus.subscribe(
        "question_presented",
        lambda q: logger.log(f"Question presented: {q.get_text()}"),
    )
    event_bus.subscribe(
        "answer_submitted",
        lambda data: logger.log(f"Answer submitted. Correct: {data['is_correct']}"),
    )
    event_bus.subscribe(
        "quiz_ended",
        lambda result: logger.log(
            f"Quiz ended. Score: {result.correct_answers}/{result.total_questions}"
        ),
    )

    # Set up command handlers
    command_bus.register(
        SubmitAnswerCommand,
        lambda cmd: quiz_service.quiz_aggregate.answer_current_question(
            cmd.answer_index
        ),
    )

    # Set up mediator handlers
    mediator.register("get_question", lambda _: question_repo.get_random_question())

    # Create QuizService
    quiz_service = QuizService(
        question_repo, event_bus, command_bus, mediator, logger, cache
    )

    # Create and run CLI
    cli = CLI(quiz_service)
    await cli.run()


if __name__ == "__main__":
    # Set up some initial questions in the database
    database = Database()
    database.add_question(
        SimpleQuestion(
            "What is the capital of France?",
            [
                Answer("Paris", True),
                Answer("London", False),
                Answer("Berlin", False),
                Answer("Madrid", False),
            ],
        )
    )
    database.add_question(
        SimpleQuestion(
            "What is 2 + 2?",
            [
                Answer("3", False),
                Answer("4", True),
                Answer("5", False),
                Answer("6", False),
            ],
        )
    )
    database.add_question(
        SimpleQuestion(
            "Who wrote 'To Kill a Mockingbird'?",
            [
                Answer("Mark Twain", False),
                Answer("Harper Lee", True),
                Answer("F. Scott Fitzgerald", False),
                Answer("Ernest Hemingway", False),
            ],
        )
    )

    # Run the main function
    asyncio.run(main())
