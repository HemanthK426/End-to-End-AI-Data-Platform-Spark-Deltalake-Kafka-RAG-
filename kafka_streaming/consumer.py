df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING)")

parsed_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/delta/checkpoints") \
    .start("/delta/bronze_stream")