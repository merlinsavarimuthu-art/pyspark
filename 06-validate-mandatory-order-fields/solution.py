from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce, col, when

spark = (
    SparkSession.builder
    .appName("Fill Missing Customer Cities")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/workspaces/pyspark/datasets/orders.csv")
)
# 1. remove the null or empty customer_id values
missing_customers = (df.customer_id.isNull() | ((col("customer_id")) == ""))


rejected_records = df.withColumn("rejection_reason",
                 when(missing_customers,"Rejected due to missing customer_id")
                .when(~missing_customers, "Valid record"))
rejected_records.show()
spark.stop()