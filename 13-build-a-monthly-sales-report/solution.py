from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count,sum,to_date,countDistinct
spark = SparkSession.builder.appName("PySpark").getOrCreate()

 
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)


result = df.dropDuplicates(["order_id"])\
                .filter(df.status == "COMPLETED")\
                .withColumn("sales_month", to_date("order_date", "yyyy-MM"))\
                .groupBy("sales_month")\
                .agg(
                        countDistinct("order_id").alias("total_orders"),
                        sum("amount").alias("total_sales")
                    )
result.show()