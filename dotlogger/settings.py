"""
Configurações para biblioteca de logs.

Como colisões de configurações são resolvidas:
    - IDs tem sempre a maior prioridade sobre configurações.
    - Classes tem maior prioridade do que SETs.
    - SETs tem a menor prioriade.
"""

global_logs_settings: dict[str, bool | str] = {} 

logs_settings_by_set: dict[str, dict[str, bool | str]] = {}
logs_settings_by_class: dict[str, dict[str, bool | str]] = {}
logs_settings_by_id: dict[str, dict[str, bool | str]] = {}

logs_settings_by_classifiers = {
    "set": logs_settings_by_set,
    "class": logs_settings_by_class,
    "id": logs_settings_by_id,
}

KEY_OPTIONS_FOR_SETTINGS = ["blocked", "write_to"]


def raise_invalid_classifier_opt(classifier_opt: str) -> None:
    raise ValueError(
            f"Option {classifier_opt} is not a valid option of classifier."+
            " Valid options are set, class or id."
        )

def get_classifier_dict(
    classifier_opt: str
    ) -> dict[str, dict[str, bool | str]]:
    """
    Get correct classifier dict given a classifier option.
    """
    co_lowered = classifier_opt.lower()
    
    try:
        classifier_dict = logs_settings_by_classifiers[co_lowered]
    except:
        raise_invalid_classifier_opt(classifier_opt)

    return classifier_dict

# Funcs to manipulate above vars
def block_all_logs(block: bool = True) -> None:
    """
    Block all logs if param block=True.
    Deblock all logs if param block=False.
    """
    block_opt = KEY_OPTIONS_FOR_SETTINGS[0]

    global_logs_settings[block_opt] = block

def get_all_logs_blocked() -> bool:
    """
    Get all logs blocked.
    if all logs blocked return True, else return False
    """
    block_opt = KEY_OPTIONS_FOR_SETTINGS[0]

    return global_logs_settings.get(block_opt, False)

def block_log_by_classifier(classifier: str, classifier_opt: str) -> None:
    """
    Configure a classifier to block a log if that log receive the classifier.
    """
    classifier_dict = get_classifier_dict(classifier_opt)
    
    block_opt = KEY_OPTIONS_FOR_SETTINGS[0]
    write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]

    write_to_config = get_write_log_to_by_classifier(classifier, classifier_opt)

    classifier_dict[classifier] = {
        block_opt: True, 
        write_to_opt: write_to_config
        }
    
def get_log_blocked_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> bool:
    """
    Get if the classifier(set, class, id) is configured to block logs.
    Return True if is blocking, otherwise False.
    """
    classifier_dict = get_classifier_dict(classifier_opt)
    
    block_opt = KEY_OPTIONS_FOR_SETTINGS[0]
    
    return classifier_dict.get(classifier, {}).get(block_opt, False)

def remove_log_blocked_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> None:
    """
    Remove the blocking config for the given classifier.
    """
    classifier_dict = get_classifier_dict(classifier_opt)

    if specific_c_config_dict := classifier_dict.get(classifier, {}):
        block_opt = KEY_OPTIONS_FOR_SETTINGS[0]
        specific_c_config_dict[block_opt] = False

        return
    
def write_all_logs_to(path: str) -> None:
    """
    Configure all logs to be written to param path.
    """
    write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]

    global_logs_settings[write_to_opt] = path

def get_write_all_logs_to() -> str:
    """
    Get where all logs were configured to be written.
    """
    write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]

    return global_logs_settings.get(write_to_opt, "")

def write_log_to_by_classifier(
        classifier: str, 
        path: str, 
        classifier_opt: str
    ) -> None:
    """
    Configure a classifier(set, class, id) to 
    configure where a log will be written.
    """
    classifier_dict = get_classifier_dict(classifier_opt)
    
    block_opt = KEY_OPTIONS_FOR_SETTINGS[0]
    write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]

    block_config = get_log_blocked_by_classifier(classifier, classifier_opt)

    classifier_dict[classifier] = {
        block_opt: block_config, 
        write_to_opt: path
        }
    
def get_write_log_to_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> str:
    """
    Get the path that was configured for a classifier(set, class, id).
    """
    classifier_dict = get_classifier_dict(classifier_opt)
    
    write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]

    return classifier_dict.get(classifier, {}).get(write_to_opt, "")

def remove_write_log_to_by_classifier(
        classifier: str, 
        classifier_opt: str
    ) -> None:
    """
    Remove the path (write_to config) configured for the given classifier.
    """
    classifier_dict = get_classifier_dict(classifier_opt)

    if specific_c_config_dict := classifier_dict.get(classifier, {}):
        write_to_opt = KEY_OPTIONS_FOR_SETTINGS[1]
        specific_c_config_dict[write_to_opt] = ""

        return
    