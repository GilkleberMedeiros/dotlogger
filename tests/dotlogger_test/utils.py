from dotlogger import DotLogger
from unittest.mock import Mock

from pathlib import Path
from typing import Callable


class DotLoggerTestCreator:
    @classmethod
    def fact_logger(cls, log_set: str ="set", log_class: str ="class") -> DotLogger:
        return DotLogger(log_set, log_class)
    
    @classmethod
    def fact_parcial_mocked_logger_for_assemble_log(
            cls, 
            log_set: str = "set", 
            log_class: str = "class",
            mock_params: dict[str, any] = {},
        ) -> DotLogger:
        gdn = {"return_value": "00.00.00"}
        gdl = {"return_value": "XXXX "}
        gdr = {"return_value": "YYYY "}

        logger = cls.fact_logger(log_set, log_class)

        if mock_params.get("get_datetime_now", False):
            gdn = mock_params["get_datetime_now"]
        if mock_params.get("get_default_location", False):
            gdl = mock_params["get_default_location"]
        if mock_params.get("get_default_resource", False):
            gdr = mock_params["get_default_resource"]

        logger.get_datetime_now = Mock(**gdn)
        logger.get_default_location = Mock(**gdl)
        logger.get_default_resource = Mock(**gdr)

        return logger
    
    @classmethod
    def fact_parcial_mocked_logger_for_get_func_to_write_log(
            cls, 
            log_set: str = "set", 
            log_class: str = "class",
            mock_params: dict[str, any] = {},
        ) -> DotLogger:
        clfwdsn = {"return_value": "GGGG"}
        wttf = {"return_value": Callable[[str], bool]}

        if mock_params.get("create_log_file_with_datestring_name", False):
            clfwdsn = mock_params["create_log_file_with_datestring_name"]
        if mock_params.get("write_text_to_file", False):
            wttf = mock_params["write_text_to_file"]

        logger = cls.fact_logger(log_set, log_class)
        logger.create_log_file_with_datestring_name = Mock(**clfwdsn)
        logger.write_text_to_file = Mock(**wttf)

        return logger

class PathMockCreator:
    @classmethod
    def fact_pathmock(cls) -> Mock:
        return Mock()
    
    @classmethod
    def fact_parcial_path_mocked(cls) -> Path:
        Path.mkdir = Mock()
        Path.touch = Mock()

        return Path