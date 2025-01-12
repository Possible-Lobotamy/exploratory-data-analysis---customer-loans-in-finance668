import numpy as np 
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

class DataFrameTransform: 
    def __init__(self, df):
        self.df = df

    @staticmethod
    def impute_mean(df, column_name):
        if column_name in df.columns and df[column_name].dtype in [np.float64, np.int64]:
            mean_value = df[column_name].mean()
            df = df.copy()
            df.loc[df[column_name].isna(), column_name] = mean_value
            print(f"Imputed mean value {mean_value:.2f} into null values of '{column_name}'")
        return df

    @staticmethod
    def impute_median(df, column_name):
        if column_name in df.columns and df[column_name].dtype in [np.float64, np.int64]:
            median_value = df[column_name].median()
            df = df.copy()
            df.loc[df[column_name].isna(), column_name] = median_value
            print(f"Imputed median value {median_value:.2f} into null values of '{column_name}'")
        return df

    @staticmethod
    def impute_mode(df, column_name):
        if column_name in df.columns:
            mode_value = df[column_name].mode()
            if not mode_value.empty:
                df = df.copy()
                df.loc[df[column_name].isna(), column_name] = mode_value[0]
                print(f"Imputed mode value '{mode_value[0]}' into null values of '{column_name}'")
        return df

    def log_tf(self, column_name):
        if column_name in self.df.columns and (self.df[column_name] >= 0).all():
            self.df[column_name] = self.df[column_name].map(lambda i: np.log(i + 1))
            print(f"Applied log transformation to '{column_name}'.")
            sns.histplot(self.df[column_name], kde=True)
            plt.title(f"Log Transform of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"Cannot apply log transformation to '{column_name}'. Ensure there are no negative values.")

    def sqrt_tf(self, column_name):
        if column_name in self.df.columns and (self.df[column_name] >= 0).all():
            self.df[column_name] = self.df[column_name].map(lambda i: np.sqrt(i))
            print(f"Applied square root transformation to '{column_name}'.")
            sns.histplot(self.df[column_name], kde=True)
            plt.title(f"Square Root Transform of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"Cannot apply square root transformation to '{column_name}'. Ensure all values are non-negative.")

    def bxcx_tf(self, column_name):
        if column_name in self.df.columns and (self.df[column_name] > 0).all():
            transformed, _ = stats.boxcox(self.df[column_name])
            self.df[column_name] = transformed
            print(f"Applied Box-Cox transformation to '{column_name}'.")
            sns.histplot(self.df[column_name], kde=True)
            plt.title(f"Box-Cox Transform of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"Cannot apply Box-Cox transformation to '{column_name}'. Ensure all values are positive.")

    def yeoj_tf(self, column_name):
        if column_name in self.df.columns:
            transformed, _ = stats.yeojohnson(self.df[column_name])
            self.df[column_name] = transformed
            print(f"Applied Yeo-Johnson transformation to '{column_name}'.")
            sns.histplot(self.df[column_name], kde=True)
            plt.title(f"Yeo-Johnson Transform of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"Cannot apply Yeo-Johnson transformation to '{column_name}'.")

    def rem_num_out(self):
        numeric_mask = pd.Series(True, index=self.df.index)
        for col in self.df.select_dtypes(include=[np.number]).columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            numeric_mask &= (self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)
        self.df = self.df[numeric_mask]
        print("Removed numeric outliers.")

    def rem_dtme_out(self):
        datetime_mask = pd.Series(True, index=self.df.index)
        for col in self.df.select_dtypes(include=["datetime64[ns]"]).columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - pd.Timedelta(days=30 * 1.5 * (IQR / pd.Timedelta(days=30)))
            upper_bound = Q3 + pd.Timedelta(days=30 * 1.5 * (IQR / pd.Timedelta(days=30)))
            datetime_mask &= (self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)
        self.df = self.df[datetime_mask]
        print("Removed datetime outliers using ~months (30 days) as the unit.")


    def get_dataframe(self):
        return self.df
