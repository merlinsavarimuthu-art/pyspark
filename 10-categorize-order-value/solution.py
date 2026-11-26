from pyspark.sql import SparkSession
from pyspark.sql.functions import when,col, current_date, datediff, to_date

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

df = df.withColumn("order_value",
                   when(col("amount") < 500, "Low")
                   .when(col("amount") < 1000, "Medium")
                   .otherwise("High"))
df.show()
