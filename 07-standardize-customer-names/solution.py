from pyspark.sql import SparkSession
from pyspark.sql.functions import col, initcap, lower, trim

spark = (
    SparkSession.builder
    .appName("Standardize Customer Names")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/customers.csv")
)
df = df.withColumn("name",
                   initcap(lower(trim(col("name")))))

df.show();