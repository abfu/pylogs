import logging
import sys
import random
import pandas as pd

root = logging.getLogger(__name__)

BASIC_FORMAT = '%(levelname)s:%(name)s:%(message)s'


# Formatter
formatter = logging.Formatter(fmt='{asctime},{levelno},{levelname},{message}', style='{', datefmt='%H%M')
basic_format = logging.Formatter(fmt=BASIC_FORMAT)


# Handlers
handler_stderr = logging.StreamHandler(sys.stderr)
handler_stderr.setFormatter(basic_format)

handler_file = logging.FileHandler('logs.csv', mode='w')
handler_file.setFormatter(formatter)

root.addHandler(handler_file)
root.addHandler(handler_stderr)

levels = [f'root.{level}("{level} log message")' for level in ['debug', 'info', 'warning', 'error', 'critical']]


def get_random_log():
    choice = random.choice(levels)
    eval(choice)


###
n_log_entries = 25
for log_entry in range(0, n_log_entries):
    get_random_log()

df = pd.read_csv('logs.csv', names=['timestamp', 'levelno', 'levelname', 'message'], index_col=None)
