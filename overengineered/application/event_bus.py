import asyncio
from typing import Dict, List, Callable, Any, Coroutine, Union


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Union[Callable, Coroutine]]] = {}

    def subscribe(self, event_type: str, callback: Union[Callable, Coroutine]) -> None:
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def publish(self, event_type: str, data: Any = None) -> None:
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                if asyncio.iscoroutinefunction(callback):
                    await callback(data)
                else:
                    callback(data)
