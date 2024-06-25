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

def collect_table_data(conn):
    sql_query = read_sql_query("./src/analysis/duplicated_list_movies/query.sql")
    execute_sql_query(conn,sql_query)
    query = '''SELECT * FROM deduplicated_list'''
    df = pd.read_sql_query(query, conn)
    print(df)