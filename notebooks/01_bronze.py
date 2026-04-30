
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Bronze Ingestion") \
    .getOrCreate()

df = spark.read.csv("/FileStore/data/sample_data.csv", header=True, inferSchema=True)

df.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/bronze_table")