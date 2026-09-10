import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession


sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()


# Script generated for node S3DataSource
S3DataSource_n_source = spark.read.format("text").load("s3://amazon-sagemaker-027024089510-us-west-2-635znel7hip47k/shared/workflows/my-workflows-3.yaml")

# Script generated for node S3DataSink
S3DataSource_n_source.write.format("csv") \
    .option("header", True) \
    .mode("append") \
    .save("s3://sagemaker-glue-output-027024089510/my-workflows-3-output/")