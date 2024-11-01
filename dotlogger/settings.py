"""
Configurações para biblioteca de logs.

Como colisões de configurações são resolvidas:
    - IDs tem sempre a maior prioridade sobre configurações.
    - Classes tem maior prioridade do que SETs.
    - SETs tem a menor prioriade.
"""

# Block all logs if True.
ALL_LOGS_BLOCKED = False

# Block logs by their sets, classes or ids.
BLOCKED_LOGS_SET: dict[str, bool] = {}
BLOCKED_LOGS_CLASS: dict[str, bool] = {}
BLOCKED_LOGS_ID: dict[str, bool] = {}

# Set all logs to be write to an especified dir or file.
# This setting can be overriden when calling .log() method.
WRITE_ALL_LOGS_TO = ""

# Set where logs will be writen based on their set, class and id.
WRITE_LOGS_TO_BY_SET: dict[str, str] = {}
WRITE_LOGS_TO_BY_CLASS: dict[str, str] = {}
WRITE_LOGS_TO_BY_ID: dict[str, str] = {}


# Funcs to manipulate above vars
def block_all_logs(block: bool = True) -> None:
    """
    Block all logs if param block=True.
    Deblock all logs if param block=False.
    """
    const_name = "ALL_LOGS_BLOCKED" 
    globals()[const_name] = block

def get_all_logs_blocked() -> bool:
    """
    Get all logs blocked.
    if all logs blocked return True, else return False
    """
    const_name = "ALL_LOGS_BLOCKED"
    return globals()[const_name]

def block_log_by_classifier(classifier: str, classifier_opt: str) -> None:
    """
    Set a classifier to block a log if that log receive the classifier.
    """
    classifier_var_preffix = "BLOCKED_LOGS_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()
    
    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    
    classifier_var[classifier] = True
    
def get_log_blocked_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> bool:
    """
    Get if a is set classifier(set, class, id) to block logs.
    Return True if is blocking, otherwise
    False.
    """
    classifier_var_preffix = "BLOCKED_LOGS_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()

    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    
    return classifier_var.get(classifier, False)

def remove_log_blocked_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> None:
    """
    Remove a classifier(set, class, id) that was set to block logs.
    Raise KeyError if classifier doesn't exist.
    """
    classifier_var_preffix = "BLOCKED_LOGS_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()

    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    
    try: classifier_var.pop(classifier)
    except:
        raise KeyError(f"Classifier {classifier}, "+
                       f"doesn't exists in blockeds {classifier_opt.upper()}s")
    
def write_all_logs_to(path: str) -> None:
    """
    Set all logs to be written to param path.
    """
    const_name = "WRITE_ALL_LOGS_TO" 
    globals()[const_name] = path

def get_write_all_logs_to() -> str:
    """
    Get where all logs were set to be written.
    """
    const_name = "WRITE_ALL_LOGS_TO" 
    return globals()[const_name]

def write_log_to_by_classifier(
        classifier: str, 
        path: str, 
        classifier_opt: str
    ) -> None:
    """
    Set a classifier(set, class, id) to set where a log will be written.
    """
    classifier_var_preffix = "WRITE_LOGS_TO_BY_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()

    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    
    classifier_var[classifier] = path
    
def get_write_log_to_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> str:
    """
    Get the path of a classifier(set, class, id).
    """
    classifier_var_preffix = "WRITE_LOGS_TO_BY_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()

    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    
    return classifier_var.get(classifier, "")

def remove_write_log_to_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> None:
    """
    Remove a classifier path and raise KeyError if 
    classifier path's was not set.
    """
    classifier_var_preffix = "WRITE_LOGS_TO_BY_"
    classifier_var_name = classifier_var_preffix + classifier_opt.upper()

    try:
        classifier_var = globals()[classifier_var_name]
    except:
        raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )
    

    try: classifier_var.pop(classifier)
    except:
        raise KeyError(f"Classifier {classifier}, "+
                       f"doesn't exists in blockeds {classifier_opt.upper()}s")