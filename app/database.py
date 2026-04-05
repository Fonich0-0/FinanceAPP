import psycopg2
from psycopg2 import Error
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Находим путь к папке FinanceApp (корень проекта)
BASE_DIR = Path(__file__).resolve().parent 
env_path = BASE_DIR / '.env.local'

load_dotenv(dotenv_path=env_path)

logging.basicConfig(level=logging.INFO, filename='db.log', format='%(asctime)s - %(levelname)s - %(message)s')

class DataBase:
    def __init__(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_pass = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.conn = None
        self.cur = None
    
    def add_operation_to_db(self, operation, date, category, amount, currency, description):
        operation_is = "income" if operation == "income" else "expense"
        query = f"INSERT INTO {operation_is} (date, category, amount, currency, description) VALUES (%s, %s, %s, %s, %s)"
        self.cur.execute(query, (date, category, amount, currency, description))
        self.conn.commit()
        

    def connection_database(self):
        """Упрощённый метод - только подключение"""
        try:
            # Самые базовые параметры
            self.conn = psycopg2.connect(
                user=self.db_user,
                password=self.db_pass,
                host=self.db_host,               
                port=self.db_port,     
                database=self.db_name
            )
            self.cur = self.conn.cursor()
            print("🔥 ПОДКЛЮЧЕНИЕ УСТАНОВЛЕНО!")
            logging.info("Успешное подключение к PostgreSQL")
            self.cur = self.conn.cursor()

            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS income (
                    id SERIAL PRIMARY KEY,
                    date DATE DEFAULT CURRENT_DATE,
                    category VARCHAR(50),
                    amount INTEGER,
                    currency VARCHAR(10),
                    description TEXT
                )
            """)
            print("✅ Таблица 'income' создана")
            
            return True
        except Exception as e:
            print(f"💥 ОШИБКА: {e}")
            return False

    # def connection_database(self):
    #     try:
    #         self.conn = psycopg2.connect(
    #             user=self.db_user,
    #             password=self.db_pass,
    #             host=self.db_host,  
    #             port=self.db_port,     
    #             database=self.db_name
    #         )
    #         logging.info("Успешное подключение к PostgreSQL")
    #         self.cur = self.conn.cursor()

    #         self.cur.execute("""
    #             CREATE TABLE IF NOT EXISTS income (
    #                 id SERIAL PRIMARY KEY,
    #                 date DATE DEFAULT CURRENT_DATE,
    #                 category VARCHAR(50) NOT NULL,
    #                 amount INT NOT NULL,
    #                 currency VARCHAR(10) NOT NULL,
    #                 description VARCHAR(200)
    #             )
    #             """)
            
    #         self.cur.execute("""
    #             CREATE TABLE IF NOT EXISTS expense (
    #                 id SERIAL PRIMARY KEY,
    #                 date DATE DEFAULT CURRENT_DATE,  
    #                 category VARCHAR(50) NOT NULL,
    #                 amount INT NOT NULL,
    #                 currency VARCHAR(10),
    #                 description VARCHAR(200)
    #             )
    #             """)
            
    #         return True
            
            
    #     except (Exception, Error) as error:
    #         logging.error(f"Ошибка при подключении: {error}")
    #         return False

            
    def close_database(self):
        try:
            if self.conn:
                self.conn.commit()
                self.conn.close()
                logging.info("Соединение закрыто")

        except Exception as e:
            logging.error(f"Ошибка при закрытии соединения: {e}")


    