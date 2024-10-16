# libs
from _libs import *

# preprocessing
def get_data_summary(
        df: pd.DataFrame,
        title: str, summary_file_path: str
) -> pd.DataFrame:
    with open(summary_file_path, 'a+') as f:
        buffer = io.StringIO()
        df.info(buf=buffer)

        print(f"{title}\
            \nShape: {df.shape}\
            \nHead:\n{tabulate(df.head(), headers='keys', tablefmt='psql')}\
            \nTail:\n{tabulate(df.tail(), headers='keys', tablefmt='psql')}\
            \nInfo:\n{buffer.getvalue()}", file=f)
        
    return df

def preprocess_category(
    df: pd.DataFrame, 
    summary_file_path: str) -> pd.DataFrame:
    f = open(summary_file_path, 'a+')
    print("Preprocessing", file=f)
    # stripping white spaces
    df.columns = [name.strip() for name in df.columns.tolist()]

    cat_cols = df.select_dtypes('object').columns.tolist()

    # null strings
    null_strings_columns = (df[cat_cols] == '').sum(axis=0).to_frame('count')\
        .query("count != 0").index.tolist()
    if null_strings_columns:
        df[null_strings_columns] = df[null_strings_columns].map(lambda x: np.nan if x == '' else x)
        print(f"Columns with null strings:\n{null_strings_columns}", file=f)
    else:
        print("Columns with null strings: None", file=f)
    
    f.close()
    
    return df

def preprocess(
    df: pd.DataFrame, 
    summary_file_path: str, columns_to_drop: list[str]=[]) -> pd.DataFrame:
    f = open(summary_file_path, 'a+')

    # drop irrelavant columns
    if columns_to_drop:
        df.drop(columns_to_drop, axis=1, inplace=True)

    # single-value columns
    single_value_columns = df.nunique().to_frame('nuique')\
        .query("nuique == 1").index.tolist()
    if single_value_columns:
        df.drop(single_value_columns, axis=1, inplace=True)
        print(f"Columns with only 1 value: {', '.join(single_value_columns)}", file=f)

    # duplications
    df.drop_duplicates(inplace=True)
    
    # missing values
    missing_values_columns = df.isnull().sum(axis=0).to_frame('count')\
        .query("count != 0")
    if missing_values_columns.index.tolist():
        print(f"Missing values per column:\
            \n{tabulate(missing_values_columns, headers='keys', tablefmt='psql')}", file=f)
    else:
        print("Missing values: None", file=f)
    
    f.close()

    return df