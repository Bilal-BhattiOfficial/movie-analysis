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

def average_imdbscore(conn):
    sql_query = read_sql_query("./src/analysis/dig_deeper/average_imdb_score/query.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query, conn)
    print(df)

    x = np.arange(len(df['vote_range']))
    width = 0.20

    fig, ax1 = plt.subplots()

    # Plot number of movies
    ax1.bar(x - width/2, df['num_movies'], width, label='Number of Movies', alpha=0.7)
    ax1.set_xlabel('IMDb Votes Range')
    ax1.set_ylabel('Number of Movies')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['vote_range'])
    ax1.legend(loc='upper left')

    # Create a twin Axes sharing the same x-axis
    ax2 = ax1.twinx()
    ax2.bar(x + width/2, df['avg_imdb_score'], width, label='Average IMDb Score', color='orange', alpha=0.7)
    ax2.set_ylabel('Average IMDb Score')
    ax2.legend(loc='upper right')

    plt.title('Number of Movies and Average IMDb Score by IMDb Votes Range')
    plt.tight_layout()
    plt.show()

   