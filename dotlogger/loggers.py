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
            *args: Any, **kwargs: Any
        ) -> None:
        self.set = set
        self.log_class = log_class

    def log(
            self,
            msg: str,
            log_type: str,
            include_date: bool = False,
            include_time: bool = True,
            origin_path: str = "",
            origin_resource: str = "",
            write_to: str = "",
            id: str = "",
        ) -> None:
        self.id = id
        self.write_to = write_to

        if self.is_log_blocked(self.set, self.log_class, self.id):
            return None
        
        log = self.assemble_log(
            msg, log_type, 
            include_date, include_time,
            origin_path,
            origin_resource
        )

        write_log_to = self.get_log_write_to_priority(
            self.write_to, self.set, 
            self.log_class, self.id
            )
        write_log_method = self.get_write_log_method(write_log_to)
        write_log_method(log)

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
        if get_all_logs_blocked():
            return True
        
        if set and get_log_blocked_by_classifier(set, "set"):
            return True
        
        if log_class and get_log_blocked_by_classifier(log_class, "class"):
            return True
        
        if id and get_log_blocked_by_classifier(id, "id"):
            return True
        
        return False
    
    def get_log_write_to_priority(self, write_to: str, set: str, log_class: str, id: str) -> str:
        """
        Esse método retorna uma string que pode ser o caminho de onde o 
        log será escrito ou outra indicação de onde o log será escrito.
        """
        if write_to:
            return self.write_to
        elif id:
            if (write_to_by_id := 
                get_write_log_to_by_classifier(self.id, "id")):
                return write_to_by_id
        elif log_class:
            if (write_to_by_class := 
                get_write_log_to_by_classifier(self.log_class, "class")):
                return write_to_by_class
        elif set:
            if (write_to_by_set := 
                get_write_log_to_by_classifier(self.set, "set")):
                return write_to_by_set
        elif (write_all_logs_to := get_write_all_logs_to()):
            return write_all_logs_to

        return "prompt"     

    def get_write_log_method(self, write_to: str) -> Callable[[str], None]:
        """
        Define o método que será usado na escrita do log.
        """
        if write_to.lower() == "prompt":
            return print
        
        write_to_path = Path(write_to)
        self.log_path = write_to
        if write_to_path.is_dir():
            self.transform_path()
            return self.write_log
        elif write_to_path.is_file():
            return self.write_log
        
        raise ValueError(
            "Expected a keyword, like 'prompt', a file path or a dir path"+
            f", but {write_to} is no one of them."
            )

    def write_log(self, msg: str, path: str = "") ->None:
        if not path:
            try: path = self.log_path
            except:
                raise Exception(
                    "self.log_path does not exist and no path was especified to this method."
                    )


        log_file = path.open("a") # type: ignore
        log_file.write(msg)
        log_file.close()

    def transform_path(self, path: str = "") -> None:
        """
        Transforma um caminho de diretório em um caminho de arquivo
        com nome YYYY-MM-DD.log
        """
        if path:
            try: self.log_path = path
            except: raise Exception(
                "self.log_path does not exist and no path was especified to this method."
                )

        current_date = date.today()
        str_date = current_date.isoformat()
        file_path = str_date + ".log"

        log_path = Path(self.log_path).joinpath(file_path)

        self.log_path = str(log_path)
      
        