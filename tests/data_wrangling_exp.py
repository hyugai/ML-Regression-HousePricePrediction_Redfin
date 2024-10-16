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
summary_file_path = cwd + "/resource/output/logs/dw.txt"
df_api_cleaned = df_api.pipe(get_data_summary, "Overviews of raws data from API", summary_file_path)\
    .pipe(preprocess_category, summary_file_path)\
        .pipe(preprocess, summary_file_path)