from typing import Dict, Callable
from dataclasses import dataclass


@dataclass
class Command:
    pass


@dataclass
class SubmitAnswerCommand(Command):
    answer_index: int


class CommandBus:
    def __init__(self):
        self.handlers: Dict[type, Callable] = {}

    def register(self, command_type: type, handler: Callable) -> None:
        self.handlers[command_type] = handler

    def handle(self, command: Command):
        handler = self.handlers.get(type(command))
        if not handler:
            raise ValueError(f"No handler registered for command {type(command)}")
        return handler(command)
