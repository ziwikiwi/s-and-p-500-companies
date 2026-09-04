import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_node_s3_source = spark.read.format("parquet").load("s3://amazon-sagemaker-027024089510-us-west-2-635znel7hip47k/shared/query-history/event_date=2026-08-29/")