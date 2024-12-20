from dotlogger import DotLogger
from unittest.mock import Mock


class DotLoggerTestCreator:
    @classmethod
    def fact_logger(cls, log_set: str ="set", log_class: str ="class") -> DotLogger:
        return DotLogger(log_set, log_class)

class PathMockCreator:
    @classmethod
    def fact_pathmock(cls) -> Mock:
        return Mock()
    