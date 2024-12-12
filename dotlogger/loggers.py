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
import inspect



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
    def __init__(
            self, 
            set: str, 
            log_class: str, 
            date_log_format: str = r"%d/%m/%Y", 
            time_log_format: str = r"%H:%M:%S",
            date_filename_format: str = r"%d_%m_%Y", 
        ) -> None:
        self.set = set
        self.log_class = log_class
        self.date_log_format = date_log_format
        self.time_log_format = time_log_format
        self.date_filename_format = date_filename_format
    
    def log(
            self,
            id: str,
            msg: str,
            type: str,
            include_date: bool = True,
            include_time: bool = True,
            in_location: str = "",
            on_resource: str = "",
            write_to: str = "",
        ) -> bool:
        self.id = id

        if not self.is_log_blocked():
            return False

        stack = inspect.stack()
        self.caller_frame = stack[1] if len(stack) > 1 else 0

        log_msg = self.assemble_log(msg, type, include_date, include_time, in_location, on_resource)

        place_to_write_log = self.get_place_to_write_log(write_to)
        func_to_write_log = self.get_func_to_write_log(place_to_write_log)

        return func_to_write_log(log_msg)

    def is_log_blocked(self) -> bool:
        """
        Return True if log is blocked in some way, 
        otherwise False.
        """
        return get_all_logs_blocked() or self.is_blocked_by_set() or \
            self.is_blocked_by_class() or self.is_blocked_by_id()
    
    def is_blocked_by_set(self) -> bool:
        """Return True if log is blocked by classifier set, otherwise False"""
        return get_log_blocked_by_classifier(self.set, "set")
    
    def is_blocked_by_class(self) -> bool:
        """Return True if log is blocked by classifier class, otherwise False"""
        return get_log_blocked_by_classifier(self.log_class, "class")
    
    def is_blocked_by_id(self) -> bool:
        """Return True if log is blocked by classifier id, otherwise False"""
        return get_log_blocked_by_classifier(self.id, "id")
    
    def assemble_log(
        self, 
        msg: str, 
        type: str, 
        include_date: bool = True, 
        include_time: bool = True,
        in_location: str = "",
        on_resource: str = "",
        ) -> str:
        """
        Assemble the log string and return it.
        """
        log_string = ""
        log_string += type + " "

        now_date_str = self.get_datetime_now(self.date_log_format)
        now_time_str = self.get_datetime_now(self.time_log_format)
        log_string += f"{now_date_str} " if include_date else ""
        log_string += f"{now_time_str} " if include_time else ""

        log_string += msg + " "

        location = self.get_default_location()
        resource = self.get_default_resource()
        log_string += f"IN {in_location} " if in_location else location
        log_string += f"ON {on_resource} " if on_resource else resource

        log_string += "\n"

        return log_string

    def get_datetime_now(format: str) -> str:
        """
        Return the now datetime as string formated with format param.
        """
        now = datetime.now()
        
        return now.strftime(format)
    
    def get_default_location(self) -> str:
        """Get and return default log location already formated."""
        return f"IN {self.caller_frame.filename} " if self.caller_frame != 0 else ""
    
    def get_default_resource(self) -> str:
        """Get and return default log resource already formated."""
        return f"ON {self.caller_frame.resource} " if self.caller_frame != 0 else ""
    
    def get_place_to_write_log(write_to_param: str) -> str:
        """Return the correct place to write log."""
        return write_to_param or get_write_all_logs_to() or "print"
    
    def get_func_to_write_log(self, place_to_write_log: str) -> Callable[[str], bool] | print:
        """
        Return the correct function to write log based 
        on place param passed.
        """
        func_to_write_log = print
        place = place_to_write_log

        place_path_obj = Path(place)
        if place != "print":
            if place_path_obj.exists():
                if place_path_obj.is_file():
                    func_to_write_log = self.write_text_to_file(place)
                elif place_path_obj.is_dir():
                    place = self.get_log_file_path(place)
                    func_to_write_log = self.write_text_to_file(place)
                else:
                    raise Exception(
                        "Path passed is not a dir or file path."+
                        f" in log {self.log_repr()}"
                        )
            else:
                place_path_obj.mkdir(parents=True)

                if place_path_obj.suffix:
                    place_path_obj.touch()
                    func_to_write_log = self.write_text_to_file(place)
                elif place_path_obj.is_dir():
                    place = self.get_log_file_path(place)
                    func_to_write_log = self.write_text_to_file(place)
                else:
                    raise Exception(
                        "Path passed is not a dir or file path."+
                        f" in log {self.log_repr()}"
                        )
                
        return func_to_write_log
    
    def write_text_to_file(self, path: str) -> Callable[[str], bool]:
        """
        Parent closure function.
        """
        def inner(msg: str) -> bool:
            """
            Child closure function. Receive msg param and write it 
            to path param from parent closure function;
            """
            path_obj = Path(path)
            try:
                with path_obj.open("a") as f:
                    f.write(msg)
                    f.flush()
            except Exception as e:
                raise Exception(
                    f"Exception: {e} occured while writing log"+ 
                    f" {self.log_repr()}"
                    )
            
            return True
        
        return inner
    
    def get_log_file_path(self, dir_path: str) -> str:
        """
        Receive a dir path and return a path (as plain string) for an already created log file.
        filename will be as the date_filename_format passed in constructor.
        """
        path_obj = Path(dir_path)
        log_filename = self.get_datetime_now(self.date_filename_format) + ".logs"
        path_obj = path_obj.joinpath(log_filename)
        path_obj.touch()

        return str(path_obj)

    def log_repr(self) -> str:
        """Return a log repr."""
        return f"(set: {self.set}, class: {self.log_class}, id: {self.id})"
    