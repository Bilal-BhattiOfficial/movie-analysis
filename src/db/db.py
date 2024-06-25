import sqlite3
import csv

def create_and_connect_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Database '{db_name}' created successfully.")
        return conn
    except Exception as e:
        print("DB creation reading error : {e}")

def read_sql_file(file_path):
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
            print(f"SQL file '{file_path}' read successfully.")
            return sql_script
    except Exception as e:
        print("SQL file reading error : {e}")
   

def execute_sql_script(conn, sql_script):
    try:
        with conn:
            conn.executescript(sql_script)
        print("SQL script executed successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def load_csv_data(conn,csv_file,table_name):
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
        print(f"Csv Loading Error: {e}")

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
