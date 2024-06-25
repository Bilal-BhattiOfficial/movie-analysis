from src.config.config import *
from src.db.db import *
from src.analysis.duplicated_list_movies.main import *
from src.analysis.dig_deeper.longest_shortest_runtime_movies.main import *
from src.analysis.dig_deeper.titles.main import *
from src.analysis.dig_deeper.movies_per_genre.main import *
from src.analysis.dig_deeper.average_run_times.main import *
from src.analysis.dig_deeper.average_imdb_score.main import *


def db_setup():
    #Connecting database
    conn = create_and_connect_database(db_name)

    #Emptying the database
    drop_all_tables(conn)

    #Inserting tables in db
    sql_script = read_sql_file(sql_file_path)
    execute_sql_script(conn, sql_script)

    #Loading data into the tables
    load_csv_data(conn,"./movies/credits.csv","credits")
    load_csv_data(conn,"./movies/titles.csv","titles")
    load_csv_data(conn,"./movies/ratings.csv","ratings")

    #DB connection closed
    conn.close()
    print("Database connection closed.")

def analysis():
    print("Lets start Analysis")
    conn = create_and_connect_database(db_name)

    # Deduplicated List of Movies based on Titles and ratings.
    collect_table_data(conn)

    # Longest and Shortest Runtime for MOVIE
    collect_data(conn)

    #Longest and Shortest titles
    collect_titles(conn)

    #Movies Count per Genre
    #count_movies(conn)

    #Average Runtimes Per Release Year
    #average_runtimes(conn)

    #Average IMDB Scores
    average_imdbscore(conn)
    # print(data)
    conn.close()


def main():
    db_setup()
    analysis()

if __name__ == "__main__":
    print("Launch")
    main()
