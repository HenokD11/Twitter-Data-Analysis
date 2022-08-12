import numpy as np
import pandas as pd
import psycopg2
import streamlit as st
from decouple import config
from sqlalchemy import exc


class DBoperations:

    def __init__(self, host, database, user, password, port) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def DBConnect(self, dbName=None):
        try:
            conn = psycopg2.connect(
                database=self.database, user=self.user, password=self.password, host=self.host, port=self.port
            )
            cursor = conn.cursor()
            cursor.execute("select version()")
            data = cursor.fetchone()
            print("Connection established to: ", data)
            return conn, cursor
        except exc.SQLAlchemyError as e:
            print("Error", e)
        # conn = mysql.connector.connect(host='localhost', port="3306", user='root', password="",
            #    database=dbName)