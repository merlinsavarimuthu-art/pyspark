from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark").getOrCreate()

orders_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders_items.csv")
)
products_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/products.csv")
)
df = products_df.join(orders_df.select("product_id").distinct(), "product_id", "left_anti") 

df.show()