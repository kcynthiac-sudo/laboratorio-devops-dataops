import psycopg2

conexion = psycopg2.connect(
    "host=localhost dbname=ventasdb user=admin password=admin123"
)

print("Conexion exitosa")

conexion.close()