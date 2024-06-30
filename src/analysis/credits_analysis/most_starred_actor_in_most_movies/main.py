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

def actor_most_movies_by_releaseyear(conn):
    sql_query = read_sql_query("./src/analysis/credits_analysis/most_starred_actor_in_most_movies/query.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query, conn)
    print(df)

    # Plotting the data
    plt.figure(figsize=(12, 8))
    bars = plt.bar(df['release_year'], df['movie_count'], color='skyblue')

    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies')
    plt.title('Number of Movies by Most Starring Actor Each Year')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotating the bars with actor names
    for bar, actor in zip(bars, df['actor']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, actor, ha='center', va='bottom', rotation=90, fontsize=8)

    plt.tight_layout()
    plt.show()
    