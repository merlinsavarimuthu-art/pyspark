from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/datasets/customers.csv")

result = df.filter("purchase_amount > 100")\
            .where("age >= 30")\
            .select("customer_id", "name", "purchase_amount")

result.show()