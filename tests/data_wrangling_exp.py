# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd() 
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

# exp
df_api = pd.read_csv('resource/data/api.csv', dtype={'sold_date': 'object'})
df_api.pipe(get_data_summary, "Overviews of raws data from API", cwd + "/resource/output/logs/dw.txt")