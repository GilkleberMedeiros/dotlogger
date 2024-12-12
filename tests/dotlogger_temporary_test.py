from ..dotlogger import *
from typing import Any


# TODO: Realizar os testes da função log

def test():
    write_all_logs_to("./logs/")

    log("set1", "class1", "42", "Menssagem de teste 1", "ERROR")
    log("set1", "class2", "21", "Menssagem de teste 2", "WARNING")

    block_log_by_classifier("set2", "set")
    log("set2", "class3", "10.5", "Menssagem de teste 3", "PROCESS")
