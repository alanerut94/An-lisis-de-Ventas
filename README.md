📊 Análisis de Ventas

Este proyecto demuestra un pipeline completo de análisis de ventas utilizando herramientas del ecosistema de datos moderno. Se trabajó desde el procesamiento de datos en Python, su carga en BigQuery, consultas SQL para obtener insights clave y la visualización final en Power BI.

---

⚙️ Herramientas utilizadas

- **Python** (ETL)
- **Google BigQuery** (almacenamiento y consultas)
- **SQL** (análisis de datos)
- **Power BI** (visualización de insights)

---

🗂 Estructura del proyecto

Analisis-de-Ventas/
├── scripts/ # Scripts de carga y transformación
│ ├── papeline_mejorado.py
│ └── cargar_bigquery.py
│
├── dashboard/ # Visualización
│ └── dashboard_ventas.pbix
│
├── README.md # Este archivo


🔄 Flujo del proyecto

1. Transformación con Python
   El script `papeline_mejorado.py` limpia y prepara los datos para análisis.

2. Carga a BigQuery
   Con `cargar_bigquery.py`, se cargan los datos procesados a un dataset en BigQuery.

3. Consulta SQL en BigQuery
   Se realizó una consulta para identificar el producto más vendido:

   ```sql
   SELECT producto, SUM(total_venta) AS total
   FROM `venta_pyme.registro_ventas`
   GROUP BY producto
   ORDER BY total DESC
   LIMIT 1;

    Resultado: Bolso con ventas por $186.000

Visualización en Power BI
Se construyó un dashboard con:

*Producto más vendido
*Total de ventas
*Ventas por región
