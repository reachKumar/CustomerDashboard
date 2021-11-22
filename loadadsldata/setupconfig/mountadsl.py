# Databricks notebook source
# MAGIC %md
# MAGIC # Mount ADSL

# COMMAND ----------

storage_account_name ="rkadls201storage"
client_id="505d5558-5e0f-4ab3-abb1-683467242275"
tenent_id ="2c3fd08b-8d1d-40b6-9895-8affdbe5d7c0"
client_secret="98a7Q~NhftdIZqJwB1BLJdd1bSiBCJCaKYM06"


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": f"{client_id}",
          "fs.azure.account.oauth2.client.secret": f"{client_secret}",
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenent_id}/oauth2/token"}

# COMMAND ----------

# Optionally, you can add <directory-name> to the source URI of your mount point.
container_name="adslingestdim"
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/rkadls201storage/adslingestdim")

# COMMAND ----------

# MAGIC %fs
# MAGIC head dbfs:/mnt/rkadls201storage/adslingestdim/Clients.txt
