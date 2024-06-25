import pandas as pd
import matplotlib.pyplot as plt

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

def count_movies(conn):
    sql_query = read_sql_query("./src/analysis/dig_deeper/movies_per_genre/query.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query, conn)
    print("Number of Movies per Genre:")
    print(df)

    df['movie_count'] = df['movie_count'].astype(int)
    # Select top 10 and bottom 10 genres
    top_10 = df.head(10)
    bottom_10 = df.tail(10)
    combined_df = pd.concat([top_10, bottom_10])
    
    # Visualize the result using a horizontal bar chart
    plt.figure(figsize=(12, 9))
    plt.barh(combined_df['genres'], combined_df['movie_count'], color='red')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genres')
    plt.title('Number of Movies per Genre (Top 10 and Bottom 10)')
    #plt.gca().invert_yaxis()  # Invert y-axis to show the highest values on top
    plt.tight_layout()
    plt.show()

