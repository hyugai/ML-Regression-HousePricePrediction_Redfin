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
columns_to_drop = ['address', 'sale_type', 'sold_date', 'days_on_market', 
                   'status', 'next_open_house_start_time', 'next_open_house_end_time', 'url', 
                   'source', 'mls', 'favorite', 'interested', 'location']
with open(summary_file_path, 'w+') as f:
    f.write('')

df_api_cleaned = df_api.pipe(get_data_summary, "Overviews of raws data from API", summary_file_path)\
    .pipe(preprocess_category, summary_file_path)\
        .pipe(preprocess, summary_file_path, columns_to_drop)\
            .pipe(get_data_summary, "Overviews of cleaned data from API", summary_file_path)

df_html = pd.read_csv('resource/data/html.csv')
renamed_columns = {'streetLine': 'address', 'hoa': 'hoa_per_month', 'sqFt': 'square_feet', 'pricePerSqFt': 'dollars_per_square_feet', 
                   'lotSize': 'lot_size', 'yearBuilt': 'year_built', 'propertyType': 'property_type', 'zip': 'zip_or_postal_code'}
columns_to_drop = ['address', 'countryCode', 'postalCode']
df_html_cleaned = df_html.rename(columns=renamed_columns)\
        .pipe(get_data_summary, "Overviews of raws data from HTML", summary_file_path)\
            .pipe(preprocess_category, summary_file_path)\
                .pipe(preprocess, summary_file_path, columns_to_drop)\
                    .pipe(get_data_summary, "Overviews of cleaned data from HTML", summary_file_path)

both_cleaned_csv_path = cwd + "/resource/data/cleaned.csv"
df_both_cleaned = pd.concat([df_api_cleaned, df_html_cleaned], join='inner', axis=0)\
    .pipe(get_data_summary, "Overviews of concatenated csv files", summary_file_path)\
        .to_csv(both_cleaned_csv_path, index=False)

