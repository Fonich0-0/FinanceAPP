import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv


load_dotenv('.env.local')

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_encd = os.getenv("DB_ENCODING")


def connection_database():
    try:
        connection = psycopg2.connect(
            user=db_user,
            password=db_pass,
            host=db_host,  
            port=db_port,     
            database=db_name,
            encoding=db_encd
        )
        print("Успешное подключение к PostgreSQL")
        cur = connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                date DATE('now'),
                category VARCHAR(50) NOT NULL,
                amount INT NOT NULL,
                description VARCHAR(200),
                account TEXT
            )
            """)
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                date DATE('now'),
                category VARCHAR(50) NOT NULL,
                amount INT NOT NULL,
                description VARCHAR(200),
                account TEXT
            )
            """)
        working_with_db(cur, connection)
        
    except (Exception, Error) as error:
        print(f"Ошибка при подключении: {error}")

        
def close_database(connection):
    try:
        if connection:
            connection.commit()
            connection.close()
            print("Соединение закрыто")

    except Exception as e:
        print(f"Ошибка при закрытии соединения: {e}")


def working_with_db(cur, conn):
    pass

    close_database(conn)


connection_database()