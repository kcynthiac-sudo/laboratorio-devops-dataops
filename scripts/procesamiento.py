import pandas as pd
import psycopg2

df = pd.read_csv("input/dataset.csv")

conexion = psycopg2.connect(
    host="localhost",
    dbname="ventasdb",
    user="admin",
    password="admin123"
)