import pandas as pd 
from pandasgui import show

csv_lp = "/Users/max/coding_resources/finance_loan_project/flp_df/flp_df1_dtype.csv" 
df_t2 = pd.read_csv(csv_lp) 

class DataFrameInfo: 
    def __init__ (self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a Pandas DataFrame.")
        self.df = df 
    
    def col_dtypes(self):
        return pd.DataFrame({
            "Colmuns": self.df.columns,
            "Datatype": self.df.dtypes
        }).reset_index(drop=True) 
    
    def extract_stats(self):
        numeric_cols = self.df.select_dtypes(include=['number'])
        stats = pd.DataFrame({
            "Median": numeric_cols.median(),
            "Mean": numeric_cols.mean(),
            "Standard Deviation": numeric_cols.std()
        })
        return stats.reset_index().rename(columns={"index": "Column"})
    
    def distinct_cat_counts(self):
        cat_cols = self.df.select_dtypes(include=['object', 'category'])
        count = cat_cols.nunique().reset_index()
        count.columns = ["Column", "Distinct Count"]
        return count
    
    def print_df_shape(self):
        obser = self.df.shape
        (row, col) = obser
        print(f"The dataframe has {row} rows and {col} columns.") 
    
    def num_null(self):
        null_df = pd.DataFrame({
            "Columns": self.df.columns, 
            "Null Value Count": self.df.isnull().sum()
        })
        return null_df.reset_index(drop=True)
    
    def numeric_stats(self):
        return self.df.describe().round(2)
    
    def cat_stats(self):
        cat_cols = self.df.select_dtypes(include=["object", "category"])
        stats = []
        for col in cat_cols:
            col_data = self.df[col].dropna()
            if col_data.empty:
                stats.append({
                    "Column": col,
                    "Modes": None,
                    "Mode Frequency": 0
                })
                continue
            modes = col_data.mode()
            modes_str = ", ".join(modes.astype(str)) if not modes.empty else None
            freq_mode = col_data.value_counts().iloc[0] if not col_data.value_counts().empty else 0

            stats.append({
                "Column": col,
                "Modes": modes_str,
                "Mode Frequency": freq_mode
            })

        return pd.DataFrame(stats)

        

test = DataFrameInfo(df_t2)

test.num_null()