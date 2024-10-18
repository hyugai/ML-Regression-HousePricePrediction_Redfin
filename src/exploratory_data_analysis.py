# libs
from _libs import *

# summary statistics
def summarize_statistics(
        df: pd.DataFrame, 
        title: str, summary_file_path: str) -> pd.DataFrame:
    num_stats = df.select_dtypes(np.number).describe([.01, .25, .5, .75, .99]).T
    cat_stats = df.select_dtypes('object').describe().T

    with open(summary_file_path, 'a+') as f:
        print(f"{title}\
              \nNumeric features:\n{tabulate(num_stats, headers='keys', tablefmt='psql')}\
              \nCategorical features:\n{tabulate(cat_stats, headers='keys', tablefmt='psql')}", file=f)
    
    return df

# plottings
# histogram
def plot_hist(df: pd.DataFrame,
              column: str, ax) -> None:
    log_scale_names = ['price']
    mask = df[column].notnull()
    if column in log_scale_names:
        g = sns.histplot(df[column][mask], bins=100, kde=True, log_scale=True, ax=ax)
        g.axes.lines[0].set_color('red')
        g.set_ylabel(None)
    else:
        g = sns.histplot(df[column][mask], bins=100, kde=True, ax=ax)
        g.axes.lines[0].set_color('red')
        g.set_ylabel(None)