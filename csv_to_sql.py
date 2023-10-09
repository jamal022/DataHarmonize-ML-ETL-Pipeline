import pandas as pd
import pyodbc
import sqlalchemy

# SQL Server details
DRIVER = 'SQL Server Native Client 11.0'
SERVER = os.environ['MY_SERVER']'
DATABASE = 'MLDataDB'

# Connection String for Windows Authentication
sql_connection_string = f'DRIVER={{{DRIVER}}};SERVER={{{SERVER}}};DATABASE={{{DATABASE}}};Trusted_Connection=yes'

# Create an SQLAlchemy engine
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={sql_connection_string}')

def extract_and_load():
    try:
        # CSV file path
        csv_file_path = "combined_student_data.csv"
        df = pd.read_csv(csv_file_path)

        # Table name
        table_name = "StudentData"

        # Insert data into SQL Server
        df.to_sql(table_name, engine, if_exists="replace", index=False)

    except Exception as e:
        print("Data extract and load error: " + str(e))

if __name__ == "__main__":
    extract_and_load()

