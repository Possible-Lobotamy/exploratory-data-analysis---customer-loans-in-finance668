import pandas as pd

class DataTransform:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a Pandas DataFrame.")
        self.df = df

    def change_dtypes(self, dtype_dict):
        try:
            for column, dtype in dtype_dict.items():
                if column in self.df.columns:
                    if dtype == "datetime64":
                        self.df[column] = pd.to_datetime(self.df[column], errors='coerce', format='%b-%Y')
                    elif dtype == "boolean":
                        self.df[column] = self.df[column].map({'y': True, 'n': False})
                    else:
                        self.df[column] = self.df[column].astype(dtype, errors='ignore')
                else:
                    raise KeyError(f"Column '{column}' not found in DataFrame.")
            return self.df
        except Exception as e:
            raise RuntimeError(f"Error whilst changing datatypes: {e}")

if __name__ == "__main__":
    df = pd.read_csv("/Users/max/coding_resources/finance_loan_project/flp_df/loan_payments_og.csv")

    print("Original dytypes of DataFrame:")
    print(df.dtypes)

    transformer = DataTransform(df)

    dtype_dict = {
        "id": "int64",
        "member_id": "int64",
        "loan_amount": "float64",
        "funded_amount": "float64",
        "funded_amount_inv": "float64",
        "term": "category",
        "int_rate": "float64",
        "instalment": "float64",
        "grade": "category",
        "sub_grade": "category",
        "employment_length": "category",
        "home_ownership": "category",
        "annual_inc": "float64",
        "verification_status": "category",
        "issue_date": "datetime64",
        "loan_status": "category",
        "payment_plan": "boolean",
        "purpose": "category",
        "dti": "float64",
        "delinq_2yrs": "int64",
        "earliest_credit_line": "datetime64",
        "inq_last_6mths": "int64",
        "mths_since_last_delinq": "int64",
        "mths_since_last_record": "int64",
        "open_accounts": "int64",
        "total_accounts": "int64",
        "out_prncp": "float64",
        "out_prncp_inv": "float64",
        "total_payment": "float64",
        "total_payment_inv": "float64",
        "total_rec_prncp": "float64",
        "total_rec_int": "float64",
        "total_rec_late_fee": "float64",
        "recoveries": "float64",
        "collection_recovery_fee": "float64",
        "last_payment_date": "datetime64",
        "last_payment_amount": "float64",
        "next_payment_date": "datetime64",
        "last_credit_pull_date": "datetime64",
        "collections_12_mths_ex_med": "category",
        "mths_since_last_major_derog": "int64",
        "policy_code": "int64",
        "application_type": "category"
    }

    transformed_df = transformer.change_dtypes(dtype_dict)

    print("\nTransformed DataFrame dtypes:")
    print(transformed_df.dtypes)

csv_file_path = "/Users/max/coding_resources/finance_loan_project/flp_df/flp_df1_dtype.csv"
transformed_df.to_csv(csv_file_path, index=False)