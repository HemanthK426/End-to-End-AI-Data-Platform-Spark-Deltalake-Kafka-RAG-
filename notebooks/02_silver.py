from pyspark.sql.functions import col

df = spark.read.format("delta").load("/delta/bronze_table")

clean_df = df.dropDuplicates() \
    .dropna() \
    .withColumnRenamed("old_column", "new_column")

clean_df.write.format("delta") \
    .mode("overwrite") \
    .save("/delta/silver_table")