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

The process of setting up the database and importing data involves several key steps:
1. **Configuration**: Settings are stored in the `config.py` file, defining the database name and the path to the SQL initialization script.
2. **Database Setup**: The database is configured and initialized using the settings from the `config.py` file.
3. **Database Functions**: Scripts are used to manage database operations, including data loading and processing.

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

---

For more detailed information, please refer to the [Project Report](Metycle_Project___Movie_Data_Analysis_Report.pdf).
