from typing import Any, Callable
from pathlib import Path

from .settings import *


class DOTLogger():
    """
    Classe de logging principal, responsável por efetivamente fazer os logs.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def log(
            self,
            msg: str,
            log_type: str,
            include_date: bool = False,
            include_time: bool = True,
            origin_path: str = "",
            origin_resource: str = "",
            set: str = "",
            log_class: str = "",
            id: str = "",
            write_to: str = "",
        ) -> None:
        if self.log_is_blocked(set, log_class, id):
            return None
        
        pass

    def log_is_blocked(self, set: str, log_class: str, id: str) -> bool:
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
    
    def write_log(self, set: str, log_class: str, id: str, write_to: str) -> Callable[[str], None]:
        """
        Esse método implementa a lógica da hierarquia das configurações de escrita
        e chama write_log_method() para retornar o método que será usado na escrita do log.
        """
        if write_to:
            return self.write_log_method(write_to)
        elif id:
            if write_to_by_id := WRITE_LOGS_TO_BY_ID.get(id, ""):
                return self.write_log_method(write_to_by_id)
        elif log_class:
            if write_to_by_class := WRITE_LOGS_TO_BY_CLASS.get(log_class, ""):
                return self.write_log_method(write_to_by_class)
        elif set:
            if write_to_by_set := WRITE_LOGS_TO_BY_SET.get(set, ""):
                return self.write_log_method(write_to_by_set)
            
        return self.write_log_method("prompt")

    def write_log_method(self, write_to: str) -> Callable[[str], None]:
        """
        Define o método que será usado na escrita do log.
        """
        if write_to.lower() == "prompt":
            return print
        
        write_to_path = Path(write_to)
        if write_to_path.is_dir():
            # Adicionar func correta
            return print
        elif write_to_path.is_file():
            # Adicionar func correta
            return print
        
        raise ValueError(
            "Expected a keyword, like 'prompt', a file path or a dir path"+
            f", but {write_to} is no one of them."
            )
        