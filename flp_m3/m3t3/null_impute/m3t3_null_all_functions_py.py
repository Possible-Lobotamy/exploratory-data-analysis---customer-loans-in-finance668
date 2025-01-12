class DataFrameTransform:
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

def sum_nulls(df):
    null_counts = df.isnull().sum()
    total_rows = len(df)
    null_percentages = (null_counts / total_rows) * 100

    summary = pd.DataFrame({
        'Column': df.columns,
        'Null Count': null_counts,
        'Null Percentage': null_percentages
    }).reset_index(drop=True)

    return summary

def onlynulls(df):
    columns_with_nulls = df.columns[df.isnull().any()]
    df_with_nulls = df[columns_with_nulls]
    null_counts = df_with_nulls.isnull().sum()
    total_rows = len(df_with_nulls)
    null_percentages = (null_counts / total_rows) * 100

    summary = pd.DataFrame({
        'Column': df_with_nulls.columns,
        'Null Count': null_counts,
        'Null Percentage': null_percentages
    }).reset_index(drop=True)

    return summary
