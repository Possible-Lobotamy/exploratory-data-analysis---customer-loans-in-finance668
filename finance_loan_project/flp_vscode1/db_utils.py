import pandas as pd
import yaml
from sqlalchemy import create_engine

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

            db_user = credentials['RDS_USER']
            db_password = credentials['RDS_PASSWORD']
            db_host = credentials['RDS_HOST']
            db_name = credentials['RDS_DATABASE']
            db_port = credentials.get('RDS_PORT', 5432)

            db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            engine = create_engine(db_url)
            return engine

        except Exception as e:
            raise RuntimeError(f"An error occurred while initializing the engine: {e}")

    def fetch_data(self, engine):
        try:
            df = pd.read_sql(self.query, engine)
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to fetch data: {e}")


if __name__ == "__main__":
    config_path = "/Users/max/coding_resources/finance_loan_project/flp.gitignore/credentials.yaml"

    query = "SELECT * FROM loan_payments"

    connector = RDSDatabaseConnector(config_path, query)

    try:
       
        engine = connector.initialize_engine()
        print("Database engine initialized successfully.")

        data_df = connector.fetch_data(engine)
        print("Data fetched successfully:")
        print(data_df)

        csv_file_path = "/Users/max/coding_resources/finance_loan_project/flp_db/loan_payments.csv"
        connector.save_data_to_csv(data_df, csv_file_path)

    except Exception as e:
        print(f"Error: {e}")