import json
import boto3

# Initialize the EMR client using AWS credentials
client = boto3.client('emr', region_name='us-west-2', aws_access_key_id='AKIATFYN2XYJEPC4NHXR', aws_secret_access_key='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')

# Lambda function handler
def lambda_handler(event, context):
    # Extract file name and bucket name from S3 event
    file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    # Print information about the file and bucket
    print("File Name:", file_name)
    print("Bucket Name:", bucket_name)

    # Define the Spark application code location on EMR cluster
    backend_code = "s3://emrcodefilecreationbucket/Backend_spark_code.py"

    # Build the spark-submit command
    spark_submit = [
        'spark-submit',
        '--master', 'yarn',
        '--deploy-mode', 'cluster',
        backend_code,
        bucket_name,
        file_name
    ]
    
    # Print the spark-submit command
    print("Spark Submit:", spark_submit)

    # Run the EMR job flow
    cluster_id = client.run_job_flow(
        Name="emr_cluster_transient",
        Instances={
            'InstanceGroups': [
                {
                    'Name': "Master",
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 1,
                },
                {
                    'Name': "Slave",
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'CORE',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 2,
                }
            ],
            'Ec2KeyName': 'emrwest',
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            'Ec2SubnetId':'subnet-006f2c9fde171ce6d',
        },
        LogUri="s3://aws-logs-218535476754-us-west-2/elasticmapreduce",
        ReleaseLabel='emr-7.0.0',
        Steps=[
            {
                "Name": "Emr_Step_Job",
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': spark_submit
                }
            }
        ],
        BootstrapActions=[],
        VisibleToAllUsers=True,
        ServiceRole="emr",
        JobFlowRole="emr_ec2",
        Applications=[{'Name': 'Spark'}, {'Name': 'Hive'}]
    )

# Code Summary:
# This AWS Lambda function is triggered by an S3 event when a new file is uploaded.
# It extracts the file name and bucket name from the event, prints the details,
# and then runs a Spark job on an EMR cluster using the specified configuration.
# The Spark job is submitted using the 'spark-submit' command with the provided Spark application code.
 