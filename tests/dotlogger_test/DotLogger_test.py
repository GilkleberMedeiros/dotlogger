from dotlogger import DotLogger
from unittest.mock import patch, Mock, PropertyMock
from utils import DotLoggerTestCreator
from pytest import Pytester


# TODO: Testar comportamento interno do método get_func_to_Write_log 
# quando passado caminhos de arquivo ou diretório que exitem ou não
# TODO: Criar um creator e alguns factory methods para o attr logger
class TestDotLogger:
    LOG_SET = "set"
    LOG_CLASS = "class"
    LOG_ID = "id"
    LOG_TYPE = "ERROR"
    LOG_MSG = "MSG"
    LOG_DATETIME_STRING = "00.00.00"
    LOG_DEFAULT_LOCATION = "XXXX"
    LOG_DEFFAULT_RESOURCE = "YYYY"
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

    def test_assembleLog_whenDefaultParamsPassed_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = self.LOG_DATETIME_STRING + " "
        location = self.LOG_DEFAULT_LOCATION + " "
        resource = self.LOG_DEFFAULT_RESOURCE + " "
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenIncludeDateParamFalse_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = self.LOG_DATETIME_STRING + " "
        location = self.LOG_DEFAULT_LOCATION + " "
        resource = self.LOG_DEFFAULT_RESOURCE + " "
        expected_value = log_type + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, include_date=False)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenIncludeTimeParamFalse_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = self.LOG_DATETIME_STRING + " "
        location = self.LOG_DEFAULT_LOCATION + " "
        resource = self.LOG_DEFFAULT_RESOURCE + " "
        expected_value = log_type + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, include_time=False)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenInLocationParamPassed_returnsExpectedLogString(self) -> None:
        passed_location = "Locus"
        mock_params = {"get_default_location": {"return_value": passed_location}}
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log(mock_params=mock_params)
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = self.LOG_DATETIME_STRING + " "
        location = "IN " + passed_location + " "
        resource = self.LOG_DEFFAULT_RESOURCE + " "
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, in_location=passed_location)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenOnResourceParamPassed_returnsExpectedLogString(self) -> None:
        passed_resource = "Pocus"
        mock_params = {"get_default_resource": {"return_value": passed_resource}}
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log(mock_params=mock_params)
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = self.LOG_DATETIME_STRING + " "
        location = self.LOG_DEFAULT_LOCATION + " "
        resource = "ON "+ passed_resource + " "
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, on_resource=passed_resource)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"
        
