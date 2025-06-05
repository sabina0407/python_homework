# Task 5: Extending a Class
import pandas as pd

class DFPlus(pd.DataFrame):

    @property
    def _constructor(self):
        return DFPlus
    
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        total_rows = len(self) # Total number of rows in df

        for start in range(0, total_rows, 10): # loop in steps of 10 
            end = start + 10
            chunk = super().iloc[start:end]  # self -> DFPlus object(the df); super -> original DataFrame 
            print('\n' + '-' * 45)
            print(chunk.to_string(index=False)) # converts 10 row chunk to nice looking string

if __name__ == "__main__":
    dfp = DFPlus.from_csv('../csv/products.csv')
    dfp.print_with_headers()