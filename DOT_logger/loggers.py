from typing import Any, Callable
from pathlib import Path
from datetime import date, datetime

from .settings import *


class DOTLogger():
    """
    Classe de logging principal, responsável por efetivamente fazer os logs.
    """
    def __init__(
            self, 
            set: str = "",
            log_class: str = "",
            write_to: str = "",
            *args: Any, **kwargs: Any
        ) -> None:
        self.set = set
        self.log_class = log_class
        self.write_to = write_to or WRITE_ALL_LOGS_TO

    def log(
            self,
            msg: str,
            log_type: str,
            include_date: bool = False,
            include_time: bool = True,
            origin_path: str = "",
            origin_resource: str = "",
            id: str = "",
        ) -> None:
        self.id = id

        if self.is_log_blocked(self.set, self.log_class, self.id):
            return None
        
        log = self.assemble_log(
            msg, log_type, 
            include_date, include_time,
            origin_path,
            origin_resource
        )
        
        pass

    def assemble_log(
        self,
        msg: str,
        log_type: str,
        include_date: bool = False,
        include_time: bool = True,
        origin_path: str = "",
        origin_resource: str = "",
    ) -> str:
        log = f"{log_type}"

        if include_date:
            log_date = ((datetime.now()).date()).strftime("%Y/%m/%d")
            log += f" {log_date}"

        if include_time:
            log_time = (datetime.now()).time().strftime("%H:%M:%S %p %Z")
            log += f" {log_time}"
        
        log += f" {msg}"

        if not origin_path:
            log += f" IN {origin_path}"

        if not origin_resource:
            log += f" ON {origin_resource}"

        return log

    def is_log_blocked(self, set: str, log_class: str, id: str) -> bool:
        """
        Retorna True se o log está bloqueado de alguma forma,
        False caso contrário.
        """
        if ALL_LOGS_BLOCKED:
            return True
        
        if set and set in BLOCKED_LOGS_SET:
            return True
        
        if log_class and log_class in BLOCKED_LOGS_CLASS:
            return True
        
        if id and id in BLOCKED_LOGS_ID:
            return True
        
        return False
    
    def write_log_logic(self) -> Callable[[str], None]:
        """
        Esse método implementa a lógica da hierarquia das configurações de escrita
        e chama get_write_log_method() para retornar o método que será usado na escrita do log.
        """
        if self.write_to:
            return self.get_write_log_method(self.write_to)
        elif self.id:
            if write_to_by_id := WRITE_LOGS_TO_BY_ID.get(self.id, ""):
                return self.get_write_log_method(write_to_by_id)
        elif self.log_class:
            if write_to_by_class := WRITE_LOGS_TO_BY_CLASS.get(self.log_class, ""):
                return self.get_write_log_method(write_to_by_class)
        elif self.set:
            if write_to_by_set := WRITE_LOGS_TO_BY_SET.get(self.set, ""):
                return self.get_write_log_method(write_to_by_set)
            
        return self.get_write_log_method("prompt")

    def get_write_log_method(self, write_to: str) -> Callable[[str], None]:
        """
        Define o método que será usado na escrita do log.
        """
        if write_to.lower() == "prompt":
            return print
        
        write_to_path = Path(write_to)
        self.log_path = write_to_path
        if write_to_path.is_dir():
            self.transform_path()
            return self.write_log
        elif write_to_path.is_file():
            return self.write_log
        
        raise ValueError(
            "Expected a keyword, like 'prompt', a file path or a dir path"+
            f", but {write_to} is no one of them."
            )

    def write_log(self, msg: str, path: str | Path = "") -> None:
        if not path:
            try: path = self.log_path
            except:
                raise Exception("No log path especified.")

        pass

    def transform_path(self) -> None:
        """
        Transforma um caminho de diretório em um caminho de arquivo
        com nome YYYY-MM-DD.log
        """
        current_date = date.today()
        str_date = current_date.isoformat()
        file_path = str_date + ".log"

        self.log_path.joinpath(file_path)
        
        