from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce, col, when

spark = (
    SparkSession.builder
    .appName("Fill Missing Customer Cities")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/customers.csv")
)

spark.stop()