from ..dotlogger import *
from typing import Any


def test():
    print("test func executed")
    logger = DotLogger("set1", "class1")

    write_all_logs_to("./logs/")

    logger.log("42", "Menssagem de teste 1", "ERROR")
    logger.log("21", "Menssagem de teste 2", "WARNING")

    block_log_by_classifier("set2", "set")
    logger.set = "set2"
    logger.log("10.5", "Menssagem de teste 3", "PROCESS")
    
    logger.set = "set3"
    write_all_logs_to("./other_logs/abc.txt")

    logger.log("5.25", "Menssagem de teste 4", "PROCESS")
    logger.log("2.125", "Menssagem de teste 5", "PROCESS")

    logger.log("1", "Menssagem de teste 6", "PROCESS", write_to="./abc.txt")

    logger.log("2", "Menssagem de teste 4", "PROCESS", include_date=False)
    logger.log("2", "Menssagem de teste 4", "PROCESS", include_time=False)
    logger.log("2", "Menssagem de teste 4", "PROCESS", in_location="def")
    logger.log("2", "Menssagem de teste 4", "PROCESS", on_resource="brade")


class Test:
    def test():
        logger = DotLogger("set1", "class1")

        write_all_logs_to("./new_logs/")
        print(Path("./new_logs/").absolute())

        logger.log("id1", "Log chamado diretamente de uma classe 1", "Process")
        logger.log("id2", "Log chamado diretamente de uma classe 2", "Process")