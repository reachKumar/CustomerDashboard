# Databricks notebook source
# MAGIC %md
# MAGIC # Hello World

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/databricks-datasets/")

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs
# MAGIC head dbfs:/databricks-datasets/SPARK_README.md

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.widgets.help()
