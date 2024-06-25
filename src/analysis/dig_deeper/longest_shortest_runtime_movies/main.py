import pandas as pd

def read_sql_query(file_path):
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
            print(f"SQL file '{file_path}' read successfully.")
            return sql_script
    except Exception as e:
        print("SQL file reading error : {e}")

def execute_sql_query(conn,file_path):
     try:
         with conn:
            # sql_script = read_sql_query(file_path)
            # cursor = conn.executescript(sql_script)
            # return cursor.fetchall()

            query = '''SELECT MAX(runtime) AS Longest_runtime
                    FROM deduplicated_list
                    Where "type" = 'MOVIE';'''
            df = pd.read_sql_query(query, conn)
            return df
            # return cursor.fetchone()[0]
     except Exception as e:
         print(f"An error occurred: {e}")


def collect_data(conn):
    file_path = "./src/analysis/dig_deeper/longest_shortest_runtime_movies/longest_query.sql"
    longest = execute_sql_query(conn,file_path)
    print(longest)
    # file_path2 = "./src/analysis/dig_deeper/longest_shortest_runtime_movies/shortest_query.sql"
    # sql_script2 = read_sql_query(file_path2)
    #shortest = pd.read_sql_query(conn,sql_script2)
    # return longest

   