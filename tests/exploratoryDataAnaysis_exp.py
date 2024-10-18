# libs
import os, sys
cwd = os.getcwd()
os.chdir('src'); path_to_src = os.getcwd()
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

# exp
csv_path = cwd + "/resource/data/cleaned.csv"
summary_file_path = cwd + "/resource/output/logs/summary_statistics.txt"
title = "Summarized Statistics"

with open(summary_file_path, 'w') as f:
    f.write('')
df = pd.read_csv(csv_path)\
    .pipe(summarize_statistics, title, summary_file_path)

# exp: plottings
plottings = ['hist', 'box', 'qq']
