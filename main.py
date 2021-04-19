#!/usr/bin/env python

"""
LogRecord

    Loggers expose the interface that application code directly uses.

    Handlers send the log records (created by loggers) to the appropriate destination.
        https://docs.python.org/3/library/logging.handlers.html#
        https://pypi.org/project/slacker-log-handler/ – Spam Slack?

    Formatters specify the layout of log records in the final output.
        https://docs.python.org/3.7/library/logging.html#logging.LogRecord

    Filters provide a finer grained facility for determining which log records to output.


Levels
    10      DEBUG
    20      INFO
    30      WARNING
    40      ERROR
    50      CRITICAL

Filters

Config Files
"""

import pandas as pd
import logging
import sys
import log_adv


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.addHandler(logging.StreamHandler(sys.stderr))

    # Add file handler from log_adv to main
    logger.addHandler(log_adv.handler_file)

    n_log_entries = 25
    for log_entry in range(0, n_log_entries):
        log_adv.simulate_random_log_event()


    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

    # Get logger by name from log_adv.py
    logger_log_adv_1 = logging.getLogger('log_adv')
    logger_log_adv_2 = logging.getLogger('log_adv')

    df = pd.read_csv(log_adv.LOGFILE, names=['timestamp', 'levelno', 'name', 'levelname', 'message'], index_col=None)
