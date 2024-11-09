import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file into a DataFrame
data = pd.read_csv('emissions.csv')

# Database connection parameters
db_user = 'postgres'
db_password = 'ROOT'
db_host = 'localhost'
db_port = '5432'
db_name = 'emissions_data'

# Create the PostgreSQL engine using SQLAlchemy
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Load data into a new PostgreSQL table called 'emissions'
data.to_sql('emissions', engine, index=False, if_exists='replace')