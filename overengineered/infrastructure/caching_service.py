from typing import Any, Optional
import time


class CachingService:
    def __init__(self, ttl: int = 300):
        self.cache = {}
        self.ttl = ttl

    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        self.cache[key] = (value, time.time())
