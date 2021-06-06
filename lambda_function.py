import json
import boto3

rds_client = boto3.client("rds-data")


database_name = "demoserverless"
database_cluster_arn = "" # Aurora DB Cluster ARN here
database_credentials_secret_store_arn = "" # Secret Key here

def lambda_handler(event, context):
    response = execute_statement("SELECT * FROM demoserverless.Customer");
    return response;

def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=database_credentials_secret_store_arn,
        database=database_name,
        resourceArn=database_cluster_arn,
        sql=sql
    )
    return response;