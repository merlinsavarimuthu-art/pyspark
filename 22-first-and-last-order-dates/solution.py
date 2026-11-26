from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max
spark = SparkSession.builder.appName("PySpark").getOrCreate()
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/workspaces/pyspark/datasets/orders.csv")

df = df.groupby("customer_id").agg(
                                    min("order_date").alias("first_order_date"),
                                    max("order_date").alias("last_order_date")
                                ) 
df.show()