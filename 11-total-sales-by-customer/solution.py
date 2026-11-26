from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = (
    SparkSession.builder
    .appName("Find Duplicate Order IDs")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)

df =  df.dropDuplicates(["order_id"])\
                .filter(df.status == "COMPLETED")\
                .groupBy("customer_id")\
                .agg(sum("amount").alias("total_sales"))

df.show()