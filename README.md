# Movie Data Analysis Project

## Project Overview

This repository contains the Movie Data Analysis Project, which demonstrates the process of connecting to a database, importing and modifying data using SQL, and creating insightful visualizations. The project involves multiple analytical tasks to uncover patterns and insights within a comprehensive movie dataset.

## Table of Contents
1. [Introduction](#introduction)
2. [Methodology](#methodology)
   - [Dataset Description](#dataset-description)
   - [Data Import and Setup](#data-import-and-setup)
3. [Tasks and Analysis](#tasks-and-analysis)
   - [Deduplicated List of Movies and Shows](#task-1-deduplicated-list-of-movies-and-shows)
   - [Longest and Shortest Runtimes](#task-2-longest-and-shortest-runtimes)
   - [Average Runtime per Release Year](#task-3-average-runtime-per-release-year)
   - [Title Lengths Analysis](#task-4-title-lengths-analysis)
   - [IMDb Scores by Number of Votes](#task-5-imdb-scores-by-number-of-votes)
   - [Number of Movies per Genre](#task-6-number-of-movies-per-genre)
   - [Actor with Most Movie Appearances](#task-7-actor-with-most-movie-appearances)
   - [Number of Movies per Year](#task-8-number-of-movies-per-year)
4. [Conclusion](#conclusion)

## Introduction

This project presents a detailed analysis of a movie dataset as part of a coding challenge for the role of Product Analyst. The primary objective is to demonstrate the ability to connect to a database, import and manipulate data using SQL, and generate insightful visualizations. The dataset consists of three main tables—titles, ratings, and credits—which provide comprehensive information about movies, including release years, IMDb ratings, and the actors involved.

## Methodology

### Dataset Description

The dataset is divided into three main tables:
- **Titles**: Contains details about movies and TV shows, such as title, type, description, release year, age certification, runtime, genres, production countries, seasons (for TV shows), IMDb ID, and IMDb score.
- **Ratings**: Includes IMDb ratings and votes, linked to the titles table via the ID.
- **Credits**: Lists actors and directors associated with the movies and TV shows, linking to the titles and ratings tables.


### Data Import and Setup

The process of setting up the database and importing data involves several key steps. This section describes the configuration, database setup, database loading, and the scripts used to manage these operations.

### Configuration

The configuration settings are stored in the `config.py` file, which defines the database name and the path to the SQL initialization script. The contents of the `config.py` file are as follows:
```python
db_name = './database/movie-analysis.db'
sql_file_path = './src/db/init.sql'
```

```cmd
python ./main.py
```

### Database Setup

The main database setup and data import operations are handled in the `main.py` file. The `db_setup` function orchestrates the entire process:

```python
def db_setup():
    # Connecting database
    conn = create_and_connect_database(db_name)
    # Emptying the database
    drop_all_tables(conn)
    # Inserting tables in db
    sql_script = read_sql_file(sql_file_path)
    execute_sql_script(conn, sql_script)
    # Loading data into the tables
    load_csv_data(conn, "./movies/credits.csv", "credits")
    load_csv_data(conn, "./movies/titles.csv", "titles")
    load_csv_data(conn, "./movies/ratings.csv", "ratings")
    # DB connection closed
    conn.close()
    print("Database connection closed.")

```

### Database Functions

The `db.py` file contains all the functions required for creating the database, reading SQL scripts, executing SQL commands, loading CSV data into the database, and dropping existing tables. These functions are as follows:

```python
import sqlite3
import csv

def create_and_connect_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Database '{db_name}' created successfully.")
        return conn
    except Exception as e:
        print(f"DB creation error: {e}")

def read_sql_file(file_path):
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
            print(f"SQL file '{file_path}' read successfully.")
            return sql_script
    except Exception as e:
        print(f"SQL file reading error: {e}")

def execute_sql_script(conn, sql_script):
    try:
        with conn:
            conn.executescript(sql_script)
            print("SQL script executed successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def load_csv_data(conn, csv_file, table_name):
    try:
        cursor = conn.cursor()
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            columns = ', '.join(reader.fieldnames)
            placeholders = ', '.join('?' * len(reader.fieldnames))
            sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
            for row in reader:
                cursor.execute(sql, list(row.values()))
            conn.commit()
    except Exception as e:
        print(f"CSV loading error: {e}")

def drop_all_tables(conn):
    try:
        cursor = conn.cursor()
        # Get list of tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        # Drop each table
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            print(f"Table '{table_name}' dropped successfully.")
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
```

## Process Overview

1. **Connecting to the Database**: The create and connect database function establishes a connection to the SQLite database specified in the configuration file. If the database does not exist, it is created.

2. **Emptying the Database**: The drop all tables function removes all existing tables from the database to ensure a clean slate for data import.

3. **Executing SQL Script**: The read sql file function reads the SQL initialization script from the specified file path. The execute sql script function then executes this script to create the necessary tables in the database.

4. **Loading CSV Data**: The load csv data function imports data from CSV files into the corresponding tables in the database. This function reads the CSV files for the credits, titles, and ratings tables and inserts the data into the database.

5. **Closing the Connection**: Finally, the database connection is closed, ensuring all operations are properly completed and resources are released.

By following this process, the database is set up and populated with the necessary data, ready for further analysis and querying.


## Tasks and Analysis

### Task 1: Deduplicated List of Movies and Shows
- **Objective**: Remove duplicate records from the dataset.
- **SQL Code**: Provided in the report.
- **Results**: A clean, deduplicated list of movies and shows.

### Task 2: Longest and Shortest Runtimes
- **Objective**: Identify the movies with the longest and shortest runtimes.
- **SQL Code**: Provided in the report.
- **Results**: Lists of movies with the longest and shortest runtimes.

### Task 3: Average Runtime per Release Year
- **Objective**: Analyze the average runtime of movies by release year.
- **SQL Code and Python Processing**: Provided in the report.
- **Results**: Average runtimes visualized by year.

### Task 4: Title Lengths Analysis
- **Objective**: Examine the lengths of movie and show titles.
- **SQL Code**: Provided in the report.
- **Results**: Analysis of title lengths.

### Task 5: IMDb Scores by Number of Votes
- **Objective**: Analyze IMDb scores in relation to the number of votes.
- **SQL Code**: Provided in the report.
- **Results**: Insights into IMDb scores and vote counts.

### Task 6: Number of Movies per Genre
- **Objective**: Determine the number of movies in each genre.
- **SQL Code**: Provided in the report.
- **Results**: Genre distribution of movies.

### Task 7: Actor with Most Movie Appearances
- **Objective**: Identify the actor with the most movie appearances each year.
- **SQL Code**: Provided in the report.
- **Results**: List of actors with the most appearances by year.

### Task 8: Number of Movies per Year
- **Objective**: Analyze the number of movies released each year.
- **SQL Code**: Provided in the report.
- **Results**: Visualization of movie releases by year.

## Conclusion

This project effectively demonstrated the process of establishing a database connection, importing and modifying data using SQL, and creating informative visuals. Various analytical tasks revealed important patterns and insights within a vast movie dataset. The SQL queries and visualizations showcased proficiency in database management and data analysis techniques, providing a clear and efficient approach to exploring the data. This report exemplifies the valuable insights that can be derived from well-organized datasets, emphasizing the importance of data-driven decision-making in product analysis.

For more detailed information, please refer to the [Project Report](.\src\reports\Metycle_Project___Movie_Data_Analysis_Report.pdf).


