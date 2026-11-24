# Q02 - Remove Duplicate Customers

## Problem Statement

A CRM migration sends duplicate customer records.

The requirement is to ensure that the final dataset contains only **one record for each `customer_id`**.

---

## Dataset

Dataset used:

`datasets/customers.csv`

### Sample Input

| customer_id | name | email | city |
|---|---|---|---|
| C001 | Arun Kumar | arun@gmail.com | Chennai |
| C002 | Priya Sharma | priya.gmail.com | |
| C003 | John Lee | john@example.com | Singapore |
| C001 | Arun Kumar | arun@gmail.com | Bengaluru |

Notice that `C001` appears more than once.

---

## Expected Output

The resulting DataFrame should contain only one row per:

`customer_id`

Example:

| customer_id | name |
|---|---|
| C001 | Arun Kumar |
| C002 | Priya Sharma |
| C003 | John Lee |
| C004 | Meera Das |

---

## PySpark Concepts Used

- `distinct()`
- `dropDuplicates()`
- `show()`

---

## Solution

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Remove Duplicate Customers")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datasets/customers.csv")
)

df_distinct = df.distinct()

df_distinct = df_distinct.dropDuplicates(["customer_id"])

df_distinct.show()

spark.stop()
```

---

## Actual Output

```text
+-----------+-------------+-----------------+---------+----------+---------+
|customer_id|name         |email            |city     |state     |country  |
+-----------+-------------+-----------------+---------+----------+---------+
|C001       |Arun Kumar   |arun@gmail.com   |...      |...       |India    |
|C002       |Priya Sharma |priya.gmail.com  |...      |...       |India    |
|C003       |John Lee     |john@example.com |Singapore|NULL      |Singapore|
|C004       |Meera Das    |meera@example.com|Kochi    |Kerala    |India    |
+-----------+-------------+-----------------+---------+----------+---------+
```

---

## Explanation

`distinct()` removes rows that are completely identical.

```python
df.distinct()
```

`dropDuplicates(["customer_id"])` ensures that only one record is retained for each `customer_id`.

```python
df.dropDuplicates(["customer_id"])
```

---

## Important Consideration

`dropDuplicates(["customer_id"])` does **not guarantee which duplicate row will be preserved** when multiple rows have the same `customer_id` but different values.

For example:

```text
C001 | Arun Kumar | Chennai
C001 | Arun Kumar | Bengaluru
```

If the requirement is to retain the **latest customer record**, a window function with `row_number()` and `updated_at` should be used instead.

That is covered in the next scenario.