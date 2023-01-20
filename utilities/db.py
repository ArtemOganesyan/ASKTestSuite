import mysql.connector
import config
from utilities.logger import get_logger as log


def query(sql_query):
    try:
        cnx = mysql.connector.connect(
            user=config.get()['Database']['db_user'],
            password=config.get()['Database']['db_pass'],
            host=config.get()['Database']['db_host'],
            database=config.get()['Database']['db_name'],
            port=config.get()['Database']['db_port'],
            ssl_disabled='true'
        )
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(sql_query)
        return cursor.fetchall()
    except:
        log().error('Database connection error')
