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

    def emojiDB(self, dbName: str) -> None:
        conn, cur = DBoperations.DBConnect(self, 'tweets')
        dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
        cur.execute(dbQuery)
        conn.commit()

    def createDB(self) -> None:
        """
        Parameters
        ----------
        dbName :
        dbName:str :
        Returns
        -------
        """
        conn, cur = DBoperations.DBConnect(self)
        conn.commit()
        cur.close()

    def createTables(self, dbName: str) -> None:
        """
        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :
        Returns
        -------
        """
        conn, cur = DBoperations.DBConnect(self, 'tweets')
        sqlFile = 'schema.sql'
        fd = open(sqlFile, 'r')
        readSqlFile = fd.read()
        fd.close()

        sqlCommands = readSqlFile.split(';')

        for command in sqlCommands:
            try:
                res = cur.execute(command)
            except Exception as ex:
                print("Command skipped: ", command)
                print(ex)
        conn.commit()
        cur.close()

        return

    def preprocess_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Parameters
        ----------
        df :
            pd.DataFrame:
        df :
            pd.DataFrame:
        df:pd.DataFrame :
        Returns
        -------
        """
        dropcols = ['Unnamed: 0', 'possibly_sensitive']
        try:
            df = df.drop(columns=dropcols, axis=1)
            df = df.fillna(0)
        except KeyError as e:
            print("Error:", e)

        return 