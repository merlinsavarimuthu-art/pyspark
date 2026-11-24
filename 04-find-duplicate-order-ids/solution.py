from pyspark.sql import SparkSession

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

df_result = df.groupBy("order_id").count()\
                .alias("occurence_count")\
                .filter("count > 1")

df_result.show()