import pandas as pd
from google.cloud import bigquery
import os

# Archivos y configuración
csv_entrada = "ventas_pyme.csv"
csv_transformado = "ventas_pyme_transformado.csv"
json_key = "clave_bigquery.json"
project_id = "proyecto-data-465200"
dataset_id = "venta_pyme"
table_id = "registro_ventas"

# Cargar datos originales
df = pd.read_csv(csv_entrada)

# Validación: eliminar filas con datos faltantes en columnas clave
columnas_clave = ["producto", "cantidad", "precio_unitario"]
df_limpio = df.dropna(subset=columnas_clave)

# Transformación: agregar columna total_venta
df_limpio["total_venta"] = df_limpio["cantidad"] * df_limpio["precio_unitario"]

# Guardar CSV transformado
df_limpio.to_csv(csv_transformado, index=False)

# Autenticación para BigQuery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key
client = bigquery.Client(project=project_id)

# Definir esquema con nueva columna total_venta
schema = [
    bigquery.SchemaField("fecha", "DATE"),
    bigquery.SchemaField("producto", "STRING"),
    bigquery.SchemaField("cliente", "STRING"),
    bigquery.SchemaField("cantidad", "INTEGER"),
    bigquery.SchemaField("precio_unitario", "FLOAT"),
    bigquery.SchemaField("region", "STRING"),
    bigquery.SchemaField("canal", "STRING"),
    bigquery.SchemaField("total_venta", "FLOAT"),
]

# Configurar carga a BigQuery
job_config = bigquery.LoadJobConfig(
    schema=schema,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=False,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

# Cargar archivo transformado
with open(csv_transformado, "rb") as source_file:
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    load_job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

load_job.result()

print("✅ Pipeline ejecutado: datos validados, transformados y cargados en BigQuery.")
