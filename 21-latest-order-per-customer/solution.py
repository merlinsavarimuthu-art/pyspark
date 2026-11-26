from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, row_number

spark = SparkSession.builder.appName("PySpark").getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/workspaces/pyspark/datasets/customers.csv")

windowspec = Window.partitionBy("customer_id").orderBy(col("updated_at").desc())

df = df.withColumn("row_number",row_number().over(windowspec))\
.filter(col("row_number") == 1)\
.drop("row_number")
df.show()