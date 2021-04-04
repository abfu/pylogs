import pandas as pd
import log_adv

n_log_entries = 25
for log_entry in range(0, n_log_entries):
    log_adv.get_random_log()

df = pd.read_csv('logs.csv', names=['timestamp', 'levelno', 'levelname', 'message'], index_col=None)