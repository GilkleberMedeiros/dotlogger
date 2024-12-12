from ..dotlogger import *
from typing import Any


# TODO: Realizar os testes da função log

def test():
    write_all_logs_to("./logs/")

    log("set1", "class1", "42", "Menssagem de teste 1", "ERROR")
    log("set1", "class2", "21", "Menssagem de teste 2", "WARNING")

    block_log_by_classifier("set2", "set")
    log("set2", "class3", "10.5", "Menssagem de teste 3", "PROCESS")

    write_all_logs_to("./other_logs/abc.logs")

    log("set3", "class4", "5.25", "Menssagem de teste 4", "PROCESS")
    log("set3", "class4", "2.125", "Menssagem de teste 5", "PROCESS")

    log("set4", "class5", "1", "Menssagem de teste 6", "PROCESS", write_to="./abc.logs")

    log("set5", "class6", "2", "Menssagem de teste 4", "PROCESS", include_date=False)
    log("set5", "class6", "2", "Menssagem de teste 4", "PROCESS", include_time=False)
    log("set5", "class6", "2", "Menssagem de teste 4", "PROCESS", in_location="def")
    log("set5", "class6", "2", "Menssagem de teste 4", "PROCESS", on_resource="brade")

