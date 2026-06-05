import psycopg

conexion = psycopg.connect(
    "host=localhost dbname=ventasdb user=admin password=admin123"
)

print("Conexion exitosa")

conexion.close()