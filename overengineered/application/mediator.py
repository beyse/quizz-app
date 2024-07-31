from typing import Dict, Callable, Any


class Mediator:
    def __init__(self):
        self.handlers: Dict[str, Callable] = {}

    def register(self, request_type: str, handler: Callable) -> None:
        self.handlers[request_type] = handler

    def send(self, request_type: str, data: Any = None) -> Any:
        handler = self.handlers.get(request_type)
        if not handler:
            raise ValueError(f"No handler registered for request type {request_type}")
        return handler(data)
