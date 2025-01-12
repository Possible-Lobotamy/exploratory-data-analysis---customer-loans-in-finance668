import pandas as pd
import yaml
from sqlalchemy import create_engine
import os

class RDSDatabaseConnector:
    def __init__(self, config_path, query):
        self.config_path = config_path
        self.query = query

    def initialize_engine(self):
        try:
            with open(self.config_path, 'r') as f:
                credentials = yaml.safe_load(f)
            if not credentials:
                raise ValueError("YAML file is empty or improperly formatted.")

            df_user = credentials['RDS_USER']
            df_password = credentials['RDS_PASSWORD']
            df_host = credentials['RDS_HOST']
            df_name = credentials['RDS_DATABASE']
            df_port = credentials.get('RDS_PORT', 5432)

            df_url = f"postgresql://{df_user}:{df_password}@{df_host}:{df_port}/{df_name}"
            engine = create_engine(df_url)
            return engine

        except Exception as e:
            raise RuntimeError(f"An error occurred while initializing the engine: {e}")

    def fetch_data(self, engine):
        try:
            df = pd.read_sql(self.query, engine)
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to fetch data: {e}")
        
    def save_data_to_csv(self, df, file_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True) 
            df.to_csv(file_path, index=False)
            print(f"Data saved successfully to {file_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to save data to CSV: {e}")

if __name__ == "__main__":
    config_path = "/Users/max/coding_resources/finance_loan_project/flp.gitignore/credentials.yaml"
    query = """
        SELECT
            id,
            member_id,
            loan_amount,
            funded_amount,
            funded_amount_inv,
            term,
            int_rate,
            instalment,
            grade,
            sub_grade,
            employment_length,
            home_ownership,
            annual_inc,
            verification_status,
            issue_date,
            loan_status,
            payment_plan,
            purpose,
            dti,
            delinq_2yrs,
            earliest_credit_line,
            inq_last_6mths,
            mths_since_last_delinq,
            mths_since_last_record,
            open_accounts,
            total_accounts,
            out_prncp,
            out_prncp_inv,
            total_payment,
            total_payment_inv,
            total_rec_prncp,
            total_rec_int,
            total_rec_late_fee,
            recoveries,
            collection_recovery_fee,
            last_payment_date,
            last_payment_amount,
            next_payment_date,
            last_credit_pull_date,
            collections_12_mths_ex_med,
            mths_since_last_major_derog,
            policy_code,
            application_type
        FROM
            loan_payments
    """

    connector = RDSDatabaseConnector(config_path, query)

    try:
        engine = connector.initialize_engine()
        print("Database engine initialized successfully.")

        flp_df = connector.fetch_data(engine)
        print("Data fetched successfully:")
        print(flp_df)


        csv_file_path = "/Users/max/coding_resources/finance_loan_project/flp_df/flp_df_og.csv"
        connector.save_data_to_csv(flp_df, csv_file_path)

    except Exception as e:
        print(f"Error: {e}")