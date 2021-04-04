""" Notes

* Modes:
    - Mode 'a' -> append / Mode 'w' -> write

* Levels
    - DEBUG, INFO, ...
    - 10, 20, ...

* Set level by name


"""


import sys
import logging
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--log', default='DEBUG')
args = parser.parse_args()
loglevel = args.log

# noinspection PyArgumentList
logging.basicConfig(handlers=[logging.FileHandler('example.log', 'w', 'utf-8'), logging.StreamHandler(sys.stdout)],
                    level=getattr(logging, loglevel.upper()))

logging.basicConfig(handlers=[logging.FileHandler('example.log', 'w', 'utf-8'), logging.StreamHandler(sys.stdout)],
                    level=getattr(logging, loglevel.upper()))



# Mode 'a' -> append / Mode 'w' -> write
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


lvl = logging.getLevelName(logging.getLogger().level)
print(f'\n**Level**: {lvl}')

