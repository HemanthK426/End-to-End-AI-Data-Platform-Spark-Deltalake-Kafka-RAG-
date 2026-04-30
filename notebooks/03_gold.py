from pyspark.sql.functions import count, desc

df = spark.read.format("delta").load("/delta/silver_table")

agg_df = df.groupBy("category") \
    .agg(count("*").alias("total_count")) \
    .orderBy(desc("total_count"))

agg_df.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/gold_table")