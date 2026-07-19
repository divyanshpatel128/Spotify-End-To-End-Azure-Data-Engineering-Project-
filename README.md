# 🎧 Spotify End-to-End Azure Data Engineering Project

An end-to-end Data Engineering pipeline built on Microsoft Azure, covering ingestion, transformation, and dimensional modeling of Spotify-style data.

## 🏗️ Architecture

<img width="1042" height="400" alt="image" src="https://github.com/user-attachments/assets/35b603df-329d-4388-ae15-b865e3f43963" />


Azure SQL DB → Azure Data Factory → Azure Data Lake Storage → Azure Databricks (PySpark + Autoloader) → Delta Live Tables → Star Schema (SCD) → Unity Catalog

## 🛠️ Tech Stack

- Azure Data Factory
- Azure SQL Database
- Azure Data Lake Storage Gen2
- Azure Databricks + PySpark
- Delta Live Tables
- Unity Catalog
- Spark Structured Streaming / Autoloader
- Azure Logic Apps

## 🚀 Key Features

- Incremental ingestion pipelines with backfilling
- Looping, metadata-driven pipelines (PySpark + Jinja2)
- Spark Streaming with Databricks Autoloader
- Star Schema modeling with Slowly Changing Dimensions (SCD)
- Delta Live Tables for automated ETL
- Unity Catalog for governance
- Logic Apps for pipeline alerts

## ⚙️ How It Works

1. Data Factory pulls data from Azure SQL DB into the data lake (incremental + backfill)
2. Databricks + PySpark clean and transform the data
3. Delta Live Tables move data through Bronze → Silver → Gold layers
4. Data is modeled into a Star Schema with SCD tracking
5. Unity Catalog manages access and governance

## 📌 Author

**Divyansh Patel**
Data Engineer | SQL | Databricks | Analytics

🔗 LinkedIn: https://www.linkedin.com/in/divyansh-patel-dataanalyst/
- divyanshpatel751@gmail.com

---

⭐ If you find this project useful, feel free to star the repository!
