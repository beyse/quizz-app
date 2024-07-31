import logging
from typing import Any


class LoggingService:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def log(self, message: str, level: str = "INFO", **kwargs: Any) -> None:
        log_method = getattr(self.logger, level.lower())
        log_method(message, extra=kwargs)
