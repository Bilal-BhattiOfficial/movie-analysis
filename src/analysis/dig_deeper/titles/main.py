import pandas as pd

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


def collect_titles(conn):

    sql_query = read_sql_query("./src/analysis/dig_deeper/titles/longest_title.sql")
    execute_sql_query(conn,sql_query)
    df = pd.read_sql_query(sql_query,conn)
    print(f"The following are the 10 Longest titles: \n {df}")

    sql_query2 = read_sql_query("./src/analysis/dig_deeper/titles/shortest_title.sql")
    execute_sql_query(conn,sql_query2)
    df = pd.read_sql_query(sql_query2,conn)
    print(f"The following are the 10 Shortest titles: \n {df}")

   