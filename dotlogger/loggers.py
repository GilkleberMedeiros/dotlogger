from .settings import (
    get_all_logs_blocked, 
    block_all_logs, 
    get_log_blocked_by_classifier, 
    block_log_by_classifier,
    write_all_logs_to, get_write_all_logs_to
)

from typing import Any, TypeVar, Callable
from datetime import datetime
from pathlib import Path
from abc import ABC



# TODO: Realizar os testes para saber se essa função está funcionando
# TODO: Transformar essa função em uma classe
def log(
        set: str, 
        log_class: str, 
        id: str,
        msg: str,
        type: str,
        include_date: bool = True,
        include_time: bool = True,
        in_location: str = "",
        on_resource: str = "",
        write_to: str = "",
        ) -> bool:
    # Stop if this log is blocked
    if get_all_logs_blocked():
       return False 
    elif get_log_blocked_by_classifier(set, "set"):
        return False
    elif get_log_blocked_by_classifier(log_class, "class"):
        return False
    elif get_log_blocked_by_classifier(id, "id"):
        return False
    
    # Get correct location to write the log
    local_to_write_log = write_to or get_write_all_logs_to() or "print"

    # assemble log string
    caller_file = Path(".")
    log_string = ""
    log_string += type + " "
    date_log_format = r"%d/%m/%Y"
    time_log_format = r"%H:%M:%S"
    log_string += (datetime.now()).date().strftime(date_log_format) + " " if include_date else ""
    log_string += (datetime.now()).time().strftime(time_log_format) + " " if include_time else ""
    log_string += msg + " "
    log_string += "IN " + in_location + " " if in_location else "IN " + str(caller_file.absolute()) + " "
    log_string += "ON " + on_resource + " " if on_resource else ""
    log_string += "\n"
    del(caller_file)

    # Select method to write log
    local_to_write_log_path_obj = Path(local_to_write_log)
    func_to_write_log = print
    if local_to_write_log != "print":
        if local_to_write_log_path_obj.exists():
            print(f"{local_to_write_log_path_obj.absolute()}")
            print("path exists")
            if local_to_write_log_path_obj.is_dir():
                print("path is dir")
                date_filename_format = r"%d_%m_%Y"

                filename = (datetime.now()).date().strftime(date_filename_format) + ".logs"
                local_to_write_log_path_obj = local_to_write_log_path_obj.joinpath(filename)
                local_to_write_log_path_obj.touch()
                print(str(local_to_write_log_path_obj))

                local_to_write_log = str(local_to_write_log_path_obj)
                func_to_write_log = write_to_file(local_to_write_log)
            else:
                func_to_write_log = write_to_file(local_to_write_log)
        else:
            local_to_write_log_path_obj.mkdir(parents=True)
            
            if local_to_write_log_path_obj.is_dir():
                print("is dir not created")
                date_filename_format = r"%d_%m_%Y"

                filename = (datetime.now()).date().strftime(date_filename_format) + ".logs"
                local_to_write_log_path_obj = local_to_write_log_path_obj.joinpath(filename)
                local_to_write_log_path_obj.touch()
                print(str(local_to_write_log_path_obj))

                local_to_write_log = str(local_to_write_log_path_obj)
                func_to_write_log = write_to_file(local_to_write_log)
            else:
                local_to_write_log_path_obj.touch()
                func_to_write_log = write_to_file(local_to_write_log)
        
    # write the log
    func_to_write_log(log_string)

    return True


def write_to_file(path: str) -> Callable[[str], bool]:
    def inner_write_to_file(msg: str) -> bool:
        try: 
            path_obj = Path(path)
            file = path_obj.open("a")
            file.write(msg)
            file.flush()
            file.close()
        except Exception as e:
            raise Exception(f"An error {e} occured while writing to log file.")
        
        return True
    
    return inner_write_to_file
    
class AbstractLogger(ABC):
    """Abstract base logger class"""


class DotLogger(AbstractLogger):
    def __init__() -> None:
        pass