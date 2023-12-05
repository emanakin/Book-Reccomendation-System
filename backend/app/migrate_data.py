import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Function to preprocess and validate data types
def preprocess_data(df, table_name, engine):
    # Preprocessing for the 'users' table
    if table_name == 'users':
        # Ensure all ages are integers or NaN
        df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Convert to NaN if not an int

    # Preprocessing for the 'ratings' table
    if table_name == 'ratings':
        # Ensure all user_ids and book_ratings are integers or NaN
        df['user_id'] = pd.to_numeric(df['user_id'], errors='coerce')
        df['book_rating'] = pd.to_numeric(df['book_rating'], errors='coerce')

        # Ensure user_ids and book_ids exist in the respective tables
        existing_user_ids = pd.read_sql_table('users', engine)['id'].astype(int).tolist()
        existing_book_isbns = pd.read_sql_table('books', engine)['isbn'].astype(str).tolist()
        print(f"Total user IDs in the database: {len(existing_user_ids)}")
        print(f"Total book ISBNs in the database: {len(existing_book_isbns)}")

        # Make sure there are no NaN values that could mess up the filtering
        df = df.dropna(subset=['user_id', 'book_isbn'])
        # Filter out ratings with non-existent user IDs or ISBNs
        initial_count = len(df)
        df = df[df['user_id'].isin(existing_user_ids) & df['book_isbn'].isin(existing_book_isbns)]
        filtered_count = len(df)
        df = df.drop_duplicates(subset=['user_id', 'book_isbn'])
        print(f"Filtered {initial_count - filtered_count} invalid ratings out of {initial_count}")
        print(f"Remaining ratings after filter: {filtered_count}")

    # Drop rows with NaN values that were created due to coercion
    df = df.dropna()

    # Reset index after dropping rows
    df = df.reset_index(drop=True)

    return df

# Function to import a CSV file into a database table
def import_csv(csv_file, table_name, engine):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Preprocess and validate data
    df = preprocess_data(df, table_name, engine)

    # Import data into the database, if_exists='append' will add data to the table
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Data from {csv_file} has been imported into the {table_name} table.")

import_csv('C:/Users/eakinlosotu/Documents/School/CP421 - Data Mining/project/backend/data/Books.csv', 'books', engine)
import_csv('C:/Users/eakinlosotu/Documents/School/CP421 - Data Mining/project/backend/data/Users.csv', 'users', engine)
import_csv('C:/Users/eakinlosotu/Documents/School/CP421 - Data Mining/project/backend/data/Ratings.csv', 'ratings', engine)

