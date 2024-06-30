import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_sql_query(file_path):
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
            print(f"SQL file '{file_path}' read successfully.")
            return sql_script
    except Exception as e:
        print("SQL file reading error : {e}")
   

def execute_sql_query(conn,sql_script):
    try:
        with conn:
            conn.executescript(sql_script)
        print("SQL script executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def movies_peryear(conn):
    sql_query = read_sql_query("./src/analysis/self_insights/movies_per_each_year/query.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query, conn)
    print(df)

    # Plotting the data
    plt.figure(figsize=(12, 6))
    plt.bar(df['release_year'], df['num_movies'], color='skyblue')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies Released')
    plt.title('Number of Movies Released Each Year')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Highlight the year with the most movies released
    max_movies_year = df.loc[df['num_movies'].idxmax(), 'release_year']
    plt.axvline(x=max_movies_year, color='red', linestyle='--', label=f'Most Movies ({max_movies_year})')
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
        