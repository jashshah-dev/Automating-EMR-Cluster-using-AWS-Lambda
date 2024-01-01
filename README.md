# Automating-EMR-Cluster-using-AWS-Lambda
 Automate Amazon EMR clusters using Lambda for streamlined and scalable data processing workflows. Unlock the full potential of your data pipeline with LambdaEMR Automator.

 # LambdaEMR Spark Job Automator

## Overview
This AWS Lambda function automates Spark job execution on an Amazon EMR cluster triggered by S3 events. When a new file is uploaded to an S3 bucket, the Lambda function extracts file and bucket details, prints them, and initiates a Spark job on an EMR cluster using specified configurations.

## Lambda Function Workflow
1. **Event Trigger:** The Lambda function is triggered by an S3 event upon file upload.
2. **Details Extraction:** Extracts file name and bucket name from the S3 event.
3. **Print Information:** Displays information about the uploaded file and bucket.
4. **Spark Application Code:** Specifies the location of the Spark application code on the EMR cluster.
5. **Spark Submit Command:** Constructs the 'spark-submit' command for running the Spark job with relevant parameters.
6. **EMR Cluster Configuration:** Defines the EMR cluster configuration, including instance types, roles, and subnet details.
7. **Job Flow Execution:** Initiates the EMR job flow with the specified configuration and runs the Spark job using the 'spark-submit' command.

## Lambda Configuration
- **Region:** us-west-2
- **Access Credentials:** AWS Access Key and Secret Access Key are provided in the Lambda function.

## EMR Cluster Configuration
- **Cluster Name:** emr_cluster_transient
- **Instance Types:**
  - Master: m5.xlarge (1 instance)
  - Slave: m5.xlarge (2 instances)
- **Instance Market:** ON_DEMAND
- **EC2 Key Name:** emrwest
- **Subnet ID:** subnet-006f2c9fde171ce6d
- **Termination Protection:** Disabled
- **Log URI:** s3://aws-logs-218535476754-us-west-2/elasticmapreduce
- **EMR Release Label:** emr-7.0.0
- **Applications:** Spark, Hive

## Spark Job Execution
- **Name:** Emr_Step_Job
- **Action On Failure:** CONTINUE
- **Jar:** command-runner.jar
- **Args:** Arguments for 'spark-submit' command for executing the Spark job.

**Note:** Ensure AWS credentials are securely managed, and proper IAM roles and policies are configured for Lambda and EMR interactions.

Feel free to modify configurations as needed for your specific use case.

