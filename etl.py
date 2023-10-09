import pandas as pd
import os
import pyodbc
from sqlalchemy import create_engine
from utils import handle_missing_values, normalize_numerical_columns, label_encode_categorical_columns

#get password from environmnet var
PASSWORD = os.environ['PGPASS']
USERNAME = os.environ['PGUID']

#sql db details
DRIVER = 'SQL Server Native Client 11.0'
SERVER = os.environ['MY_SERVER']
DATABASE = "MLDataDB;"

# postgres details 
HOST = 'localhost'
PORT = '5432'
DATABASE_POSTGRES = 'MLDataDB'

# Connection String
connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'    

def extract():
    try:
        src_conn = pyodbc.connect(connectionString)
        # Query and load data into a DataFrame
        query = 'SELECT * FROM StudentData'
        df = pd.read_sql_query(query, src_conn)
        transformed_data = transform(df)
        load(transformed_data)
    
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()

# Applying Transformations

def transform(df):
    
    numerical_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(exclude=['number']).columns
    
    # Apply transformations using utility functions
    df = handle_missing_values(df, strategy='mean')
    df = normalize_numerical_columns(df, numerical_columns)
    df = label_encode_categorical_columns(df, categorical_columns)

    # Return the transformed training data
    return df


#load data to postgres
def load(df):
    try:
        engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_POSTGRES}')
        
        # Specify the target table name as 'transformed_student_data'
        target_table = 'transformed_student_data'
        
        # Save the DataFrame to the specified PostgreSQL table
        df.to_sql(target_table, engine, if_exists='replace', index=False)
        
        print("Data loaded successfully to 'transformed_student_data' table in PostgreSQL.")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))