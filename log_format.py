"""
Available attributs:
https://docs.python.org/3.7/library/logging.html#logging.LogRecord


"""
import logging


root = logging.getLogger(__name__)

handler = logging.StreamHandler()
root.addHandler(loggi)

logging.info('info')
logging.warning('warn')


logging.info('debug')
logging.critical('crit')