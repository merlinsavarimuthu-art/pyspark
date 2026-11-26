from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = (
    SparkSession.builder
    .appName("Parse Business Ideas")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)
df = df.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
df.show()