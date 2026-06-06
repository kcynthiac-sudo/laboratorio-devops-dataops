import pandas as pd
import psycopg2

# Leer CSV
df = pd.read_csv("input/dataset.csv")

# Conexión PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    dbname="ventasdb",
    user="admin",
    password="admin123"
)

cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INTEGER,
    ciudad VARCHAR(50)
)
""")

# Insertar datos
for _, fila in df.iterrows():
    cursor.execute("""
    INSERT INTO clientes(nombre, edad, ciudad)
    VALUES (%s,%s,%s)
    """,
    (fila['nombre'], fila['edad'], fila['ciudad'])
    )

conexion.commit()

print("Datos cargados correctamente")

cursor.close()
conexion.close()