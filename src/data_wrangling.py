# libs
from _libs import *

# preprocessing
def get_data_summary(
        df: pd.DataFrame,
        title: str, summary_file_path: str) -> pd.DataFrame:
    with open(summary_file_path, 'w+') as f:
        buffer = io.StringIO()
        df.info(buf=buffer)

        print(f"{title}\
            \nShape: {df.shape}\
            \nHead:\n{tabulate(df.head(), headers='keys', tablefmt='psql')}\
            \nTail:\n{tabulate(df.tail(), headers='keys', tablefmt='psql')}\
            \nInfo:\n{buffer.getvalue()}", file=f)
        
    return df

def preprocess_category():
    pass

def preprocess():
    pass