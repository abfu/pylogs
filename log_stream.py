"""
Available attributs:
https://docs.python.org/3.7/library/logging.html#logging.LogRecord


"""
import logging

logging.basicConfig(format='{levelno}, {levelname}, {message}, {asctime}',
                    style='{', level=logging.INFO, filename='logs.csv')

logging.info('info')
logging.warning('warn')


logging.info('debug')
logging.critical('crit')