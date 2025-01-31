from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("StreamingExample").getOrCreate()

# Define Streaming Data Source (Simulated for Demo)
streaming_data = spark.readStream.format("rate").option("rowsPerSecond", 1).load()

# Display Data Schema
streaming_data.printSchema()
# Apply transformation: Multiply value by 10
transformed_data = streaming_data.withColumn("new_value", col("value") * 10)

# Display output in real time
query = transformed_data.writeStream.outputMode("append").format("console").start()

query.awaitTermination()  # Keeps streaming alive
stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "my_topic") \
    .load()

stream_df.selectExpr("CAST(value AS STRING)").writeStream.format("console").start()
transformed_data.writeStream \
    .outputMode("append") \
    .format("jdbc") \
    .option("url", "jdbc:mysql://your_database_url") \
    .option("dbtable", "real_time_data") \
    .option("user", "your_user") \
    .option("password", "your_password") \
    .start()
transformed_data.writeStream \
    .format("parquet") \
    .option("path", "s3://your-bucket/stream-data/") \
    .option("checkpointLocation", "s3://your-bucket/checkpoints/") \
    .start()

