from dotlogger import DotLogger
from unittest.mock import patch, Mock, PropertyMock
from utils import DotLoggerTestCreator, PathMockCreator
from pytest import Pytester

from pathlib import Path


class TestDotLogger:
    LOG_SET = "set"
    LOG_CLASS = "class"
    LOG_ID = "id"
    LOG_TYPE = "ERROR"
    LOG_MSG = "MSG"
    BASE_PATH = "C:/Users/Pichau/OneDrive/Documentos/Projetos/Dot_Logger/tests/dotlogger_test"
    DIR_PATH_THAT_NOT_EXIST = BASE_PATH + "/folder_for_tests/dir_that_not_exists/"
    DIR_PATH_THAT_EXIST = BASE_PATH + "/folder_for_tests/dir_that_exists/"
    FILE_PATH_THAT_NOT_EXIST = BASE_PATH + "/folder_for_tests/dir_that_exists/file_that_not_exists.txt"
    FILE_PATH_THAT_EXIST = BASE_PATH + "/folder_for_tests/dir_that_exists/file_that_exists.txt"
    NOT_EXIST_FILE_PATH_WITH_NOT_EXIST_PARENT = BASE_PATH + \
        "/folder_for_tests/dir_that_not_exists/file_that_not_exists.txt"
    
    # Scopes for dependency mock
    DOTLOGGER_LOGGERS_PATH_SCOPE = "dotlogger.loggers.Path"

    def test_getFuncToWriteLog_whenPrintStringPassed_returnsPrintFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        print_string = "print"

        actual_func = logger.get_func_to_write_log(print_string)

        assert actual_func == print, "DotLogger.get_func_to_write_log didn't returned print func."+ \
        " WhenPrintStringPassed."

    def test_getFuncToWriteLog_whenDirPathExistPassed_retunsInnerChildClosureFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        expected_func = logger.write_text_to_file(self.DIR_PATH_THAT_EXIST)
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        pathmock = PathMockCreator.fact_parcial_path_mocked()

        with patch(path_scope, pathmock, spec=Path) as pm:
            actual_func = logger.get_func_to_write_log(self.DIR_PATH_THAT_EXIST)

        assert actual_func.__code__ == expected_func.__code__, f"Expected {expected_func.__qualname__} not "+ \
        f"{actual_func.__qualname__}"

    def test_getFuncToWriteLog_whenDirPathNotExistPassed_retunsInnerChildClosureFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        expected_func = logger.write_text_to_file(self.DIR_PATH_THAT_NOT_EXIST)
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        pathmock = PathMockCreator.fact_parcial_path_mocked()

        with patch(path_scope, pathmock, spec=Path) as pm:
            actual_func = logger.get_func_to_write_log(self.DIR_PATH_THAT_NOT_EXIST)

        assert actual_func.__code__ == expected_func.__code__, f"Expected {expected_func.__qualname__} not "+ \
        f"{actual_func.__qualname__}"

    def test_getFuncToWriteLog_whenFilePathExistPassed_retunsInnerChildClosureFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        expected_func = logger.write_text_to_file(self.FILE_PATH_THAT_EXIST)
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        pathmock = PathMockCreator.fact_parcial_path_mocked()

        with patch(path_scope, pathmock, spec=Path) as pm:
            actual_func = logger.get_func_to_write_log(self.FILE_PATH_THAT_EXIST)

        assert actual_func.__code__ == expected_func.__code__, f"Expected {expected_func.__qualname__} not "+ \
        f"{actual_func.__qualname__}"

    def test_getFuncToWriteLog_whenFilePathNotExistPassed_retunsInnerChildClosureFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        expected_func = logger.write_text_to_file(self.FILE_PATH_THAT_NOT_EXIST)
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        pathmock = PathMockCreator.fact_parcial_path_mocked()

        with patch(path_scope, pathmock, spec=Path) as pm:
            actual_func = logger.get_func_to_write_log(self.FILE_PATH_THAT_NOT_EXIST)

        assert actual_func.__code__ == expected_func.__code__, f"Expected {expected_func.__qualname__} not "+ \
        f"{actual_func.__qualname__}"

    def test_getFuncToWriteLog_whenNotExistFilePathWithNEParentPassed_returnsInnerChildClosureFunc(self) -> None:
        logger = DotLoggerTestCreator.fact_logger()
        expected_func = logger.write_text_to_file(self.NOT_EXIST_FILE_PATH_WITH_NOT_EXIST_PARENT)
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        pathmock = PathMockCreator.fact_parcial_path_mocked()

        with patch(path_scope, pathmock, spec=Path) as pm:
            actual_func = logger.get_func_to_write_log(self.NOT_EXIST_FILE_PATH_WITH_NOT_EXIST_PARENT)

        assert actual_func.__code__ == expected_func.__code__, f"Expected {expected_func.__qualname__} not "+ \
        f"{actual_func.__qualname__}"
    
    def test_getFuncToWriteLog_whenDirPathExistPassed_performExpectedBehavior(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_get_func_to_write_log()
        pathmock = PathMockCreator.fact_parcial_path_mocked()
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        clfwdsn_mocked_return = DotLoggerTestCreator.CREATELOGFILEWITHDATESTRINGNAME_RETURN_VALUE

        with patch(path_scope, pathmock, spec=Path) as pm:
            logger.get_func_to_write_log(self.DIR_PATH_THAT_EXIST)

        logger.create_log_file_with_datestring_name.assert_called_once_with(self.DIR_PATH_THAT_EXIST)
        logger.write_text_to_file.assert_called_once_with(clfwdsn_mocked_return)

    def test_getFuncToWriteLog_whenDirPathNotExistPassed_performExpectedBehavior(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_get_func_to_write_log()
        pathmock = PathMockCreator.fact_parcial_path_mocked()
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE
        clfwdsn_mocked_return = DotLoggerTestCreator.CREATELOGFILEWITHDATESTRINGNAME_RETURN_VALUE

        with patch(path_scope, pathmock, spec=Path) as pm:
            logger.get_func_to_write_log(self.DIR_PATH_THAT_NOT_EXIST)

        pathmock.mkdir.assert_called_once_with(parents=True)
        logger.create_log_file_with_datestring_name.assert_called_once_with(self.DIR_PATH_THAT_NOT_EXIST)
        logger.write_text_to_file.assert_called_once_with(clfwdsn_mocked_return)

    def test_getFuncToWriteLog_whenFilePathExistPassed_performExpectedBehavior(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_get_func_to_write_log()
        pathmock = PathMockCreator.fact_parcial_path_mocked()
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE

        with patch(path_scope, pathmock, spec=Path) as pm:
            logger.get_func_to_write_log(self.FILE_PATH_THAT_EXIST)

        logger.write_text_to_file.assert_called_once_with(self.FILE_PATH_THAT_EXIST)

    def test_getFuncToWriteLog_whenFilePathNotExistPassed_performExpectedBehavior(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_get_func_to_write_log()
        pathmock = PathMockCreator.fact_parcial_path_mocked()
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE

        with patch(path_scope, pathmock, spec=Path) as pm:
            logger.get_func_to_write_log(self.FILE_PATH_THAT_NOT_EXIST)

        pathmock.touch.assert_called_once_with()
        logger.write_text_to_file.assert_called_once_with(self.FILE_PATH_THAT_NOT_EXIST)

    def test_getFuncToWriteLog_whenNotExistFileWithNEParentPassed_performExpectedBehavior(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_get_func_to_write_log()
        pathmock = PathMockCreator.fact_parcial_path_mocked()
        path_scope = self.DOTLOGGER_LOGGERS_PATH_SCOPE

        with patch(path_scope, pathmock, spec=Path) as pm:
            logger.get_func_to_write_log(self.NOT_EXIST_FILE_PATH_WITH_NOT_EXIST_PARENT)

        pathmock.mkdir.assert_called_once_with(parents=True)
        pathmock.touch.assert_called_once_with()
        logger.write_text_to_file.assert_called_once_with(self.NOT_EXIST_FILE_PATH_WITH_NOT_EXIST_PARENT)

    def test_assembleLog_whenDefaultParamsPassed_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = DotLoggerTestCreator.GETDATETIMENOW_RETURN_VALUE + " "
        location = DotLoggerTestCreator.GETDEFAULTLOCATION_RETURN_VALUE
        resource = DotLoggerTestCreator.GETDEFAULTRESOURCE_RETURN_VALUE
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenIncludeDateParamFalse_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = DotLoggerTestCreator.GETDATETIMENOW_RETURN_VALUE + " "
        location = DotLoggerTestCreator.GETDEFAULTLOCATION_RETURN_VALUE
        resource = DotLoggerTestCreator.GETDEFAULTRESOURCE_RETURN_VALUE
        expected_value = log_type + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, include_date=False)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenIncludeTimeParamFalse_returnsExpectedLogString(self) -> None:
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log()
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = DotLoggerTestCreator.GETDATETIMENOW_RETURN_VALUE + " "
        location = DotLoggerTestCreator.GETDEFAULTLOCATION_RETURN_VALUE
        resource = DotLoggerTestCreator.GETDEFAULTRESOURCE_RETURN_VALUE
        expected_value = log_type + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, include_time=False)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenInLocationParamPassed_returnsExpectedLogString(self) -> None:
        passed_location = "Locus"
        mock_params = {"get_default_location": {"return_value": passed_location}}
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log(mock_params=mock_params)
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = DotLoggerTestCreator.GETDATETIMENOW_RETURN_VALUE + " "
        location = "IN " + passed_location + " "
        resource = DotLoggerTestCreator.GETDEFAULTRESOURCE_RETURN_VALUE
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, in_location=passed_location)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"

    def test_assembleLog_whenOnResourceParamPassed_returnsExpectedLogString(self) -> None:
        passed_resource = "Pocus"
        mock_params = {"get_default_resource": {"return_value": passed_resource}}
        logger = DotLoggerTestCreator.fact_parcial_mocked_logger_for_assemble_log(mock_params=mock_params)
        log_type = self.LOG_TYPE + " "
        msg = self.LOG_MSG + " "
        datetime = DotLoggerTestCreator.GETDATETIMENOW_RETURN_VALUE + " "
        location = DotLoggerTestCreator.GETDEFAULTLOCATION_RETURN_VALUE
        resource = "ON "+ passed_resource + " "
        expected_value = log_type + datetime + datetime + msg + location + resource + "\n"

        actual_value = logger.assemble_log(self.LOG_MSG, self.LOG_TYPE, on_resource=passed_resource)

        assert actual_value == expected_value, f"Expected {expected_value} == {actual_value}"
        
