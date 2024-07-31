from typing import Dict, List, Callable
import asyncio


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable) -> None:
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def publish(self, event_type: str, data=None) -> None:
        if event_type in self.subscribers:
            await asyncio.gather(
                *[callback(data) for callback in self.subscribers[event_type]]
            )
