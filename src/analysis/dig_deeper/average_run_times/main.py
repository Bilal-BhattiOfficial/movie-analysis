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

def average_runtimes(conn):
    sql_query = read_sql_query("./src/analysis/dig_deeper/average_run_times/query.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query, conn)
    print("Number of Movies per Genre:")
    print(df)

    #Filtering the data w.r.t MOVIE and SNOW
    movies_df = df[df['type'] == 'MOVIE']
    shows_df = df[df['type'] == 'SHOW']

    #1. Grouping the movies_df DataFrame by the release_year column. 
    #2. Each group corresponds to a unique release year.
    #3. Selecting the 'runtime' column, giving us runtimes of all movies 
    #   grouped by there release year. 
    #4. Calculate the average run time for each release year using the mean function.
    #5. "movies_avg_runtime = movies_df.groupby('release_year')['runtime'].mean()"
    # this gives us a series, now we use the reset_index() to convert it back to a 
    # proper dataframe.
    movies_avg_runtime = movies_df.groupby('release_year')['runtime'].mean().reset_index()
    shows_avg_runtime = shows_df.groupby('release_year')['runtime'].mean().reset_index()
    print(shows_avg_runtime)

    # Plot the results
    plt.figure(figsize=(14, 7))
    
    # Plot movies
    plt.plot(movies_avg_runtime['release_year'], movies_avg_runtime['runtime'], label='Movies', color='blue')
    
    # Plot shows
    plt.plot(shows_avg_runtime['release_year'], shows_avg_runtime['runtime'], label='Shows', color='green')
    
    # Adding labels and title
    plt.xlabel('Release Year')
    plt.ylabel('Average Runtime (minutes)')
    plt.title('Average Runtime per Release Year')
    plt.legend()
    
    # Display the plot
    plt.tight_layout()
    plt.show()



    

