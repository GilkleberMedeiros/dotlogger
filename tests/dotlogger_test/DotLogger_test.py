from dotlogger import DotLogger
from unittest.mock import patch, Mock, PropertyMock
from utils import DotLoggerTestCreator


# TODO: Testar comportamento interno do método get_func_to_Write_log 
# quando passado caminhos de arquivo ou diretório que exitem ou não
# TODO: Criar um creator e alguns factory methods para o attr logger
class TestDotLogger:
    LOG_SET = "set"
    LOG_CLASS = "class"
    LOG_ID = "id"
    DIR_PATH_THAT_NOT_EXIST = "./folder_for_tests/dir_that_not_exist/"
    DIR_PATH_THAT_EXIST = "./folder_for_tests/dir_that_exist/"
    FILE_PATH_THAT_NOT_EXIST = "./folder_for_tests/dir_that_exist/file_that_not_exists.txt"
    FILE_PATH_THAT_EXIST = "./folder_for_tests/dir_that_exist/file_that_exists.txt"

    def test_getFuncToWriteLog_whenPrintStringPassed_returnsPrintFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        print_string = "print"

        actual_func = logger.get_func_to_write_log(print_string)

        assert actual_func == print, "DotLogger.get_func_to_write_log didn't returned print func."+ \
        " WhenPrintStringPassed."
