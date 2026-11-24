from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Keep the Latest Customer Version").getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/workspaces/pyspark/datasets/customers.csv")

windowspec = Window.partitionBy("customer_id").orderBy(col("updated_at").desc())

df_latest = df.withColumn("row_number",row_number().over(windowspec))\
              .filter(col("row_number") == 1)\
              .drop("row_number")

df_latest.show();

spark.stop()
