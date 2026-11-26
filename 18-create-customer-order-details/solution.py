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

df = orders_df.alias("o").join(customers_df.alias("c"), "customer_id", "left")\
.select("o.order_id", "o.customer_id", "c.name", "c.city", "c.email","o.status")

df.show()