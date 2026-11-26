from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, datediff, to_date

spark = (
    SparkSession.builder
    .appName("Parse Business Ideas")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/customers.csv")
)

currentdate = current_date()
# syntax - datediff(end_date, start_date)
df = df.withColumn("tenure_days",
                   datediff(currentdate,col("signup_date"))
                   )
df.show()