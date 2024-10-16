# libs
from _libs import *

# preprocessing
class DataPreprocessor():
    def __init__(self, 
                 raw_csv_path: str, target_path: str) -> None:
        self.raw_csv_path = raw_csv_path
        self.raw_df = pd.read_csv(raw_csv_path)
        self.target_path = target_path

    def generate_overviews(self):
        print(f"{self.raw_csv_path}\
            \nShape: {self.df.shape}\
            \nHead:\n{tabulate(self.df.head(), headers='keys', tablefmt='psql')}\
            \nTail:\n{tabulate(self.df.tail(), headers='keys', tablefmt='psql')}\
            \nInfo:")
        print(self.df.info())

    def general_processing(self):
        pass