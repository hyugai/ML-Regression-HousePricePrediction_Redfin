# libs
from _libs import *

# preprocessing
def get_data_summary(
        df: pd.DataFrame,
        title: str, summary_file_path: str
) -> pd.DataFrame:
    with open(summary_file_path, 'w+') as f:
        buffer = io.StringIO()
        df.info(buf=buffer)

        print(f"{title}\
            \nShape: {df.shape}\
            \nHead:\n{tabulate(df.head(), headers='keys', tablefmt='psql')}\
            \nTail:\n{tabulate(df.tail(), headers='keys', tablefmt='psql')}\
            \nInfo:\n{buffer.getvalue()}", file=f)
        
    return df

def preprocess_category(
    df: pd.DataFrame) -> pd.DataFrame:
    # stripping white spaces
    df.columns = [name.strip() for name in df.columns.tolist()]

    cat_cols = df.select_dtypes('object').columns.tolist()

    # null strings
    null_strings_columns = (df[cat_cols] == '').sum(axis=0).to_frame('count')\
        .query("count != 0").index.tolist()
    if null_strings_columns:
        df[null_strings_columns] = df[null_strings_columns].map(lambda x: np.nan if x == '' else x)


def preprocess(
    df: pd.DataFrame, 
    columns_to_drop: list[str]
) -> pd.DataFrame:
    pass