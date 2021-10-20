import os
import json

from dotenv import load_dotenv

from db_processing.sql_provider import SQLProvider

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
CONFIG_DIR = os.getenv('CONFIG_DIR')
DB_CONFIG_FILE_NAME = os.getenv('DB_CONFIG_FILE_NAME')
DB_CONFIG_PATH = f"{os.getcwd()}/{CONFIG_DIR}/{DB_CONFIG_FILE_NAME}"
SQL_REQUESTS_DIR = os.getenv('SQL_REQUESTS_DIR')


print(os.getcwd())
sql_provider = SQLProvider(SQL_REQUESTS_DIR)

with open(DB_CONFIG_PATH) as db_conf_file:
    DB_CONFIG = json.load(db_conf_file)
