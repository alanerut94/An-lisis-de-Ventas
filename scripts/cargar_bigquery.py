
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Configuraciones
CSV_FILE = "ventas_pyme.csv"
JSON_KEY = "clave_bigquery.json"
PROJECT_ID = "proyecto-data-465200"
DATASET_ID = "venta_pyme"
TABLE_ID = "registro_ventas"

# Autenticación con Google Cloud
credentials = service_account.Credentials.from_service_account_file(JSON_KEY)

# Crear cliente de BigQuery
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

# Leer el CSV
df = pd.read_csv(CSV_FILE)

# Definir el esquema si querés especificarlo (opcional)
job_config = bigquery.LoadJobConfig(
    autodetect=True,
    write_disposition="WRITE_TRUNCATE",
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1
)

# Subir los datos a BigQuery
with open(CSV_FILE, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}",
        job_config=job_config
    )

load_job.result()  # Esperar a que termine

print(f"✅ Datos cargados correctamente en {TABLE_ID}")
