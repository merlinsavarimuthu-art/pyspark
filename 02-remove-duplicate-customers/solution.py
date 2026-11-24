from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Remove Duplicate Customers").getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/workspaces/pyspark/datasets/customers.csv")

df_distinct = df.distinct();
df_distinct = df_distinct.dropDuplicates(["customer_id"])
df_distinct.show()