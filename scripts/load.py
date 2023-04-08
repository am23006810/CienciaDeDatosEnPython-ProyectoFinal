import boto3
import pandas as pd

def load_to_dl(complete_df, AWS_S3_BUCKET, key, config):

    complete_df.to_csv(
        f"s3://{AWS_S3_BUCKET}/{key}",
        index=False,
        storage_options={
            "key": config.get('IAM', 'ACCESS_KEY'),
            "secret": config.get('IAM', 'SECRET_ACCESS_KEY'),
        }
    )