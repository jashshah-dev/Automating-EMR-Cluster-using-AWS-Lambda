from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *

# Initialize a SparkSession, which is the entry point to any Spark functionality
spark = SparkSession \
        .builder \
        .appName("First_Spark_Job") \  # Set an application name for identification
        .getOrCreate()

# Define the main function
def main():
    # Extract S3 bucket and file names from command line arguments
    s3_bucket = sys.argv[1]
    s3_file = sys.argv[2]

    # Form the S3 location URL
    s3_location = "s3a://{}/{}".format(s3_bucket, s3_file)

    # Read a CSV file from the specified S3 location into a DataFrame (iris)
    iris = spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(s3_location)

    # Perform grouping by the "class" column and count the occurrences
    ms = iris.groupBy("class").count()

    # Write the result to a CSV file in a specified S3 destination
    ms.coalesce(1).write.format("csv").option("header", "true").save("s3a://destinationemrbucket/{}".format(s3_file.split('.')[0]))

# Call the main function to execute the Spark job
main()
