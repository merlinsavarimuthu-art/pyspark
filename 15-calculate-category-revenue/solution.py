from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
spark = SparkSession.builder.appName("PySpark").getOrCreate()

orders_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/order_items.csv")
)
products_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/products.csv")
)

result = orders_df.join(products_df,"product_id")\
.withColumn("categoryRevenue", orders_df.quantity * orders_df.unit_price)\
.groupBy("category")\
.agg(
   sum("categoryRevenue").alias("total_revenue")
)

result.show()
