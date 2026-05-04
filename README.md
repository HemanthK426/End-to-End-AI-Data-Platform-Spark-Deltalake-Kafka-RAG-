<div align="center">

<img src="https://img.shields.io/badge/Status-Production--Grade-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" />
<img src="https://img.shields.io/badge/Delta%20Lake-003366?style=for-the-badge" />
<img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" />
<img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" />

# ⚡ End-to-End AI Data Platform

### Spark · Delta Lake · Kafka · RAG · Snowflake · FastAPI

**A production-grade, medallion-architecture data platform that ingests batch and real-time data at scale, transforms it through a multi-layer lakehouse, and surfaces intelligent answers through a Retrieval-Augmented Generation (RAG) AI pipeline — all served via a REST API.**

[📖 Architecture](#-architecture) · [🛠 Tech Stack](#-tech-stack) · [🚀 Quick Start](#-quick-start) · [📂 Project Structure](#-project-structure) · [🔄 Pipeline Walkthrough](#-pipeline-walkthrough) · [🤖 RAG System](#-rag-ai-system) · [📡 API Reference](#-api-reference) · [🗺 Roadmap](#-roadmap)

</div>

---

## 🧭 Overview

This project demonstrates a **full-stack data engineering and AI platform** built to enterprise standards. It handles:

- **Batch ingestion** from CSV, JSON, and APIs
- **Real-time streaming** via Apache Kafka + Spark Structured Streaming
- **Lakehouse storage** using Delta Lake's medallion architecture (Bronze → Silver → Gold)
- **Data warehousing** via Snowflake with dbt transformations
- **AI-powered querying** using a Retrieval-Augmented Generation (RAG) pipeline
- **REST API serving** via FastAPI for downstream clients and BI tools

The platform is designed to be modular, observable, and extensible — each layer can be developed and tested independently.

---

## 🏛 Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          DATA SOURCES                               │
│  ┌────────────┐   ┌────────────┐   ┌───────────────────────────┐   │
│  │  CSV / JSON│   │    APIs    │   │  Kafka Streaming Events   │   │
│  └─────┬──────┘   └─────┬──────┘   └──────────────┬────────────┘   │
└────────┼────────────────┼─────────────────────────┼────────────────┘
         │                │                         │
         └────────────────┴────────────┬────────────┘
                                       ▼
                          ┌────────────────────────┐
                          │    INGESTION LAYER      │
                          │  PySpark (Batch +       │
                          │  Structured Streaming)  │
                          └────────────┬───────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              ▼                        ▼                        ▼
   ┌──────────────────┐    ┌───────────────────┐    ┌──────────────────┐
   │   BRONZE LAYER   │    │   SILVER LAYER    │    │   GOLD LAYER     │
   │  Delta Lake (S3) │───▶│  Delta Lake (S3)  │───▶│  Delta Lake (S3) │
   │  Raw / Immutable │    │  Cleaned + Typed  │    │  Aggregated /    │
   │  Append Only     │    │  Deduplicated     │    │  Business-Ready  │
   └──────────────────┘    └───────────────────┘    └────────┬─────────┘
                                                             │
                      ┌──────────────────────────────────────┤
                      │                                      │
                      ▼                                      ▼
          ┌─────────────────────┐               ┌───────────────────────┐
          │  SNOWFLAKE + dbt    │               │     AI PIPELINE       │
          │  Data Warehouse     │               │  ┌─────────────────┐  │
          │  Star Schema Models │               │  │ Text Chunking   │  │
          │  Analytics / BI     │               │  │ Embeddings      │  │
          └─────────────────────┘               │  │ (Transformers)  │  │
                                                │  │ FAISS Vector DB │  │
                                                │  └────────┬────────┘  │
                                                └───────────┼───────────┘
                                                            │
                                                            ▼
                                                ┌───────────────────────┐
                                                │     RAG PIPELINE      │
                                                │  Query → Retrieve     │
                                                │  → Context Build      │
                                                │  → LLM Generation     │
                                                └───────────┬───────────┘
                                                            │
                                                            ▼
                                                ┌───────────────────────┐
                                                │   FastAPI REST API    │
                                                │   GET /query?q=...    │
                                                └───────────┬───────────┘
                                                            │
                                                            ▼
                                                     👤 User / Client
```

---

## 🛠 Tech Stack

| Category | Technologies |
|---|---|
| **Batch Processing** | PySpark, Delta Lake |
| **Real-Time Streaming** | Apache Kafka, Spark Structured Streaming |
| **Storage** | AWS S3, Delta Lake (ACID, Time Travel, MERGE) |
| **Compute** | Apache Spark (local / Databricks) |
| **Data Warehouse** | Snowflake |
| **Transformation** | dbt (Data Build Tool) |
| **AI / Embeddings** | SentenceTransformers, LangChain, LlamaIndex |
| **Vector Store** | FAISS |
| **LLM Layer** | OpenAI / local LLM via LangChain |
| **API** | FastAPI, Uvicorn |
| **Orchestration** | Apache Airflow |
| **Language** | Python 3.10+ |

---

## 📂 Project Structure

```
End-to-End-AI-Data-Platform/
│
├── notebooks/                      # Medallion pipeline scripts
│   ├── 01_bronze.py                # Raw ingestion → Bronze Delta table
│   ├── 02_silver.py                # Cleaning + schema → Silver Delta table
│   └── 03_gold.py                  # Aggregations → Gold Delta table
│
├── streaming/                      # Real-time Kafka pipeline
│   ├── producer.py                 # Kafka event producer
│   └── consumer.py                 # Spark Structured Streaming consumer
│
├── warehouse/                      # Snowflake integration
│   ├── load_to_snowflake.py        # Gold → Snowflake loader
│   └── dbt_models/                 # dbt transformation models
│       ├── staging/
│       ├── intermediate/
│       └── mart/
│
├── ai_pipeline/                    # RAG system
│   ├── chunker.py                  # Document chunking logic
│   ├── embeddings.py               # SentenceTransformer embedding generation
│   ├── vector_store.py             # FAISS index build + retrieval
│   └── rag_pipeline.py             # End-to-end RAG chain (retrieve → LLM)
│
├── api/                            # FastAPI application
│   └── app.py                      # /query endpoint definition
│
├── airflow/                        # DAGs for orchestration
│   └── dags/
│       ├── batch_pipeline_dag.py
│       └── streaming_monitor_dag.py
│
├── data/                           # Sample datasets
│   └── sample_transactions.csv
│
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Walkthrough

### 1️⃣ Bronze Layer — Raw Ingestion

The Bronze layer is the **landing zone**. Data arrives as-is — no transformation, no schema enforcement. This preserves raw fidelity for reprocessing.

- Sources: CSV files, REST APIs, Kafka topics
- Engine: PySpark `spark.read` (batch) + `spark.readStream` (streaming)
- Storage: Delta Lake table on S3 (append-only)
- Schema: inferred at write time

```python
# notebooks/01_bronze.py
df = spark.read.option("header", True).csv("data/sample_transactions.csv")
df.write.format("delta").mode("append").save("s3://your-bucket/bronze/transactions")
```

---

### 2️⃣ Silver Layer — Cleaned & Structured

The Silver layer applies **data quality rules**. This is where raw noise becomes analytical signal.

- Null filtering and type casting
- Deduplication on primary keys
- Schema enforcement with Delta constraints
- SCD Type 1 MERGE (upsert) patterns

```python
# notebooks/02_silver.py
from delta.tables import DeltaTable

silver = DeltaTable.forPath(spark, "s3://your-bucket/silver/transactions")
silver.alias("target").merge(
    cleaned_df.alias("source"),
    "target.transaction_id = source.transaction_id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
```

---

### 3️⃣ Gold Layer — Aggregated Business Data

The Gold layer serves **business consumers** — BI tools, dashboards, the AI pipeline, and Snowflake.

- KPI aggregations (revenue by category, anomaly counts, etc.)
- Pre-joined, optimized datasets
- Written as partitioned Delta tables for fast reads

```python
# notebooks/03_gold.py
gold_df = silver_df.groupBy("category", "date") \
    .agg(
        F.sum("amount").alias("total_amount"),
        F.count("*").alias("transaction_count"),
        F.avg("amount").alias("avg_amount")
    )
gold_df.write.format("delta").mode("overwrite").save("s3://your-bucket/gold/summary")
```

---

## 📡 Real-Time Streaming

Kafka + Spark Structured Streaming enables **sub-minute latency** for event-driven data.

### Producer

```python
# streaming/producer.py
from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode())

while True:
    event = {"user_id": random.randint(1, 1000),
             "amount": round(random.uniform(1, 5000), 2),
             "category": random.choice(["retail", "food", "travel"])}
    producer.send("transactions", event)
    time.sleep(0.5)
```

### Consumer (Spark Structured Streaming)

```python
# streaming/consumer.py
stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

# Parse JSON, write to Bronze Delta in real-time
stream_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start("s3://your-bucket/bronze/streaming_transactions")
```

---

## 🏔 Data Warehouse (Snowflake + dbt)

Gold layer data is loaded into **Snowflake** for scalable warehousing. dbt models handle transformations, testing, and documentation.

### Load to Snowflake

```python
# warehouse/load_to_snowflake.py
conn_options = {
    "sfURL": "<account>.snowflakecomputing.com",
    "sfUser": "<user>",
    "sfPassword": "<password>",
    "sfDatabase": "PLATFORM_DB",
    "sfSchema": "GOLD",
    "sfWarehouse": "COMPUTE_WH"
}

gold_df.write \
    .format("snowflake") \
    .options(**conn_options) \
    .option("dbtable", "TRANSACTION_SUMMARY") \
    .mode("overwrite") \
    .save()
```

### dbt Layer

dbt models transform raw Snowflake tables into analytics-ready marts:

```
dbt_models/
├── staging/       stg_transactions.sql        -- type cast + rename
├── intermediate/  int_category_rollup.sql     -- category aggregation
└── mart/          fct_daily_summary.sql       -- final fact table for BI
```

Run with: `dbt run && dbt test`

---

## 🤖 RAG AI System

The AI pipeline turns the Gold layer into a **queryable knowledge base** using Retrieval-Augmented Generation.

### How It Works

```
Gold Layer Data
      │
      ▼
  Chunking               Split records into overlapping text chunks
      │
      ▼
  Embedding              SentenceTransformer encodes chunks → vectors
      │
      ▼
  FAISS Index            Vectors stored in a searchable FAISS index
      │
      ▼
  Query Input            User submits a natural language question
      │
      ▼
  Semantic Retrieval     Top-k most relevant chunks retrieved
      │
      ▼
  Context Assembly       Retrieved chunks passed as LLM context
      │
      ▼
  LLM Generation         LLM generates a grounded, cited answer
```

### Code Sample

```python
# ai_pipeline/rag_pipeline.py
from sentence_transformers import SentenceTransformer
import faiss, numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(texts):
    embeddings = model.encode(texts, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, texts

def retrieve(query, index, texts, k=5):
    q_vec = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(q_vec, k)
    return [texts[i] for i in indices[0]]
```

---

## 📡 API Reference

The FastAPI layer exposes the RAG system as a simple REST endpoint.

**Start the server:**
```bash
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
```

**Interactive docs:** `http://localhost:8000/docs`

---

### `GET /query`

Query the RAG pipeline with a natural language question.

**Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `q` | `string` | ✅ | The natural language query |

**Example Request:**
```http
GET /query?q=What are the most common transaction anomalies?
```

**Example Response:**
```json
{
  "query": "What are the most common transaction anomalies?",
  "response": "High-value transactions above $4,500 and rapid consecutive purchases within 60 seconds account for 78% of flagged anomalies. The 'travel' category shows the highest concentration of suspicious activity.",
  "sources_retrieved": 5,
  "latency_ms": 312
}
```

**More sample queries:**
```
GET /query?q=Which product category has the highest revenue?
GET /query?q=Summarize transaction trends for last week
GET /query?q=What patterns indicate fraudulent behavior?
GET /query?q=Compare retail vs food category performance
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Java 11+ (for Spark)
- Docker (optional, for Kafka)
- AWS credentials configured (for S3)

### 1. Clone & Install

```bash
git clone https://github.com/HemanthK426/End-to-End-AI-Data-Platform-Spark-Deltalake-Kafka-RAG-.git
cd End-to-End-AI-Data-Platform-Spark-Deltalake-Kafka-RAG-

pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Fill in: AWS credentials, Snowflake details, OpenAI API key (if using GPT)
```

### 3. Run Batch Pipeline

```bash
# Bronze → Silver → Gold
python notebooks/01_bronze.py
python notebooks/02_silver.py
python notebooks/03_gold.py
```

### 4. Start Kafka (Docker)

```bash
docker-compose up -d zookeeper kafka
python streaming/producer.py    # Terminal 1
python streaming/consumer.py    # Terminal 2
```

### 5. Load to Snowflake & Run dbt

```bash
python warehouse/load_to_snowflake.py
cd warehouse/dbt_models && dbt run && dbt test
```

### 6. Build the RAG Index

```bash
python ai_pipeline/embeddings.py     # Generate embeddings from Gold layer
python ai_pipeline/vector_store.py   # Build and persist FAISS index
```

### 7. Start the API

```bash
uvicorn api.app:app --reload
```

Visit: [http://localhost:8000/query?q=fraud+patterns](http://localhost:8000/query?q=fraud+patterns)
Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✨ Key Features

| Feature | Details |
|---|---|
| 🥉🥈🥇 **Medallion Architecture** | Bronze / Silver / Gold separation of concerns |
| ⚛️ **Delta Lake** | ACID transactions, time travel, schema evolution, MERGE/UPSERT |
| ⚡ **Spark Structured Streaming** | Sub-minute Kafka-to-Delta latency |
| 🧠 **RAG Pipeline** | Semantic retrieval + LLM generation on your own data |
| 🔍 **FAISS Vector Search** | Efficient similarity search at scale |
| 🏔 **Snowflake + dbt** | Enterprise-grade warehouse with tested transformation models |
| 🌐 **FastAPI** | High-performance async REST API with Swagger docs |
| 🔁 **Airflow Orchestration** | DAG-driven scheduling and monitoring |
| 🔒 **Data Quality** | Schema enforcement, deduplication, constraint checks at Silver layer |

---

## ⚙️ Delta Lake Capabilities Used

```python
# Time Travel — query historical state
df_yesterday = spark.read.format("delta") \
    .option("versionAsOf", 5) \
    .load("s3://your-bucket/silver/transactions")

# MERGE (Upsert)
delta_table.alias("t").merge(
    updates.alias("s"), "t.id = s.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

# Optimize + Z-Order for fast queries
delta_table.optimize().executeZOrderBy("category", "date")
```

---

## 🗺 Roadmap

- [ ] **Cloud Deployment** — Terraform IaC for AWS (S3 + EMR + API Gateway + Lambda)
- [ ] **Pinecone Integration** — Replace FAISS with a managed, scalable vector DB
- [ ] **Monitoring Stack** — Prometheus + Grafana dashboards for pipeline health
- [ ] **API Authentication** — OAuth2 / API key middleware for FastAPI
- [ ] **Databricks Migration** — Unified Spark + Delta environment on Databricks
- [ ] **Great Expectations** — Automated data quality checks at each medallion layer
- [ ] **Multi-LLM Support** — Plug-and-play support for GPT-4, Claude, Mistral, Llama 3
- [ ] **CI/CD Pipeline** — GitHub Actions for automated testing and deployment

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a PR.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

⭐ Star this repo if it helped you build something awesome!

</div>
