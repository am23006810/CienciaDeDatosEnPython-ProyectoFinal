import boto3
import psycopg2
import numpy as np
import pandas as pd


def extractRDS(config):

    aws_conn = boto3.client('rds', aws_access_key_id=config.get('IAM', 'ACCESS_KEY'),
                        aws_secret_access_key=config.get('IAM', 'SECRET_ACCESS_KEY'),
                        region_name='us-east-1')
                        
    try:
        instances = aws_conn.describe_db_instances(DBInstanceIdentifier='proyectofinal')
        RDS_HOST = instances.get('DBInstances')[0].get('Endpoint').get('Address')
        print(RDS_HOST)
    except Exception as ex:
        print("La instancia de base de datos no existe o aun no se ha terminado de crear.")
        print(ex)


    postgres_driver = f"""postgresql://{config.get('RDS', 'DB_USER')}:{config.get('RDS', 'DB_PASSWORD')}@{RDS_HOST}:{config.get('RDS', 'DB_PORT')}/{config.get('RDS', 'DB_NAME')}"""

    sql_query = 'SELECT * FROM rose_wine;'
    rose_data = pd.read_sql(sql_query, postgres_driver)
    return rose_data


def extractS3(config):

    s3client = boto3.client(
        's3',
        aws_access_key_id=config.get('IAM', 'ACCESS_KEY'),
        aws_secret_access_key=config.get('IAM', 'SECRET_ACCESS_KEY'),
    )

    response = s3client.get_object(
        Bucket='proyectofinal-us-east-1-665777243823',
        Key='sources/Red.csv'
    )

    red_data = pd.read_csv(response.get("Body"))
    red_data = red_data.rename(columns={"Name": "name", "Country": "country", "Region": "region", "Winery": "winery", "Rating": "rating", "NumberOfRatings": "numberofratings", "Price": "price", "Year": "year"}, errors="raise")


    response = s3client.get_object(
        Bucket='proyectofinal-us-east-1-665777243823',
        Key='sources/White.csv'
    )

    white_data = pd.read_csv(response.get("Body"))
    white_data = white_data.rename(columns={"Name": "name", "Country": "country", "Region": "region", "Winery": "winery", "Rating": "rating", "NumberOfRatings": "numberofratings", "Price": "price", "Year": "year"}, errors="raise")


    return red_data, white_data