import logging
import sys
import random
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

BASIC_FORMAT = '{levelname}:{name}:{message}'
LOGFILE = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_logs.csv'

# Formatter
csv_format = logging.Formatter(fmt='{asctime},{levelno},{name},{levelname},{message}', style='{', datefmt='%H:%M:%S')
basic_format = logging.Formatter(fmt=BASIC_FORMAT, style='{')


# Handlers
handler_stderr = logging.StreamHandler(sys.stderr)
handler_stderr.setFormatter(basic_format)
handler_stderr.setLevel(logging.ERROR)


handler_file = logging.FileHandler(LOGFILE, mode='w')
handler_file.setFormatter(csv_format)


logger.addHandler(handler_file)
logger.addHandler(handler_stderr)


levels = [f'logger.{level}("{level} log message")' for level in ['debug', 'info', 'warning', 'error', 'critical']]


def simulate_random_log_event():
    choice = random.choice(levels)
    eval(choice)
