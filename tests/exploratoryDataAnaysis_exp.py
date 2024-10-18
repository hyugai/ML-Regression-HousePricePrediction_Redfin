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

## exp: plottings
#num_cols = df.select_dtypes(np.number).columns.tolist()
#num_cols = np.array(num_cols).reshape(2, 5)
#cat_cols = df.select_dtypes('object').columns.tolist()
#cat_cols = np.array(cat_cols).reshape(2, 2)
#
#plottings = ['hist', 'box', 'qq']
#figs, axes = dict(), dict()
#for name in plottings:
#    figs[name], axes[name] = plt.subplots(2, 5, sharex=False, sharey=False, 
#                                          figsize=(20, 15))
#    
#for i in range(2):
#    for j in range(5):
#        plot_hist(df, num_cols[i, j], axes['hist'][i, j])
#
#for name in plottings:
#    figs[name].savefig(cwd + f"/resource/output/images/{name}.png")