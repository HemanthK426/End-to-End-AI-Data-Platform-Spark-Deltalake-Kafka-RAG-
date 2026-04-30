# Time Travel
df_v1 = spark.read.format("delta") \
    .option("versionAsOf", 0) \
    .load("/delta/silver_table")

# Upsert (MERGE)
from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "/delta/silver_table")

updates_df = spark.read.csv("/FileStore/data/updates.csv", header=True)

delta_table.alias("target").merge(
    updates_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdateAll() \
 .whenNotMatchedInsertAll() \
 .execute()

# Optimize
spark.sql("OPTIMIZE delta.`/delta/silver_table`")