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
BLOCKED_LOGS_SET: set[str] = set()
BLOCKED_LOGS_CLASS: set[str] = set()
BLOCKED_LOGS_ID: set[str] = set()

# Set all logs to be write to an especified dir or file.
# This setting can be overriden when calling .log() method.
WRITE_ALL_LOGS_TO = ""

# Set where logs will be writen based on their set, class and id.
WRITE_LOGS_TO_BY_SET: dict[str, str] = {}
WRITE_LOGS_TO_BY_CLASS: dict[str, str] = {}
WRITE_LOGS_TO_BY_ID: dict[str, str] = {}
