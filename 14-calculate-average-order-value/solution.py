from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count,sum,to_date,countDistinct


spark = SparkSession.builder.appName("PySpark").getOrCreate()
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)
df = df.dropDuplicates(["order_id"]).filter(df.status == "COMPLETED")\
        .groupBy("customer_id")\
        .agg(
            sum("amount").alias("total_sales"),
            count("order_id").alias("total_orders")
        )\
        .withColumn("AOV",col("total_sales")/col("total_orders"))
