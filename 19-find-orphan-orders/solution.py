from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark").getOrCreate()

orders_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)
customers_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/customers.csv")
)

df = orders_df.join(customers_df.select("customer_id").distinct(), "customer_id", "left_anti")

df.show()