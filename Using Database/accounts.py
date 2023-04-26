import mysql.connector
import streamlit as st
# from main import *
# Initialize connection.
# Uses st.cache_resource to only run once.

# rows = run_query("SELECT * from mytable;")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

class BankAccount():
    @st.cache_resource
    def __init__(self) -> None:
        # Connect to server
        return mysql.connector.connect(**st.secrets["mysql"])

        conn = init_connection()
        
        @st.cache_data(ttl=600)
        def run_query(query):
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

    def __str__(self) -> str:
        return "connection instablisted to the localhost"

    def create_account():
        pass