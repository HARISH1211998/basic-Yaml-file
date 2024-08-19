import boto3
import time

rds = boto3.client('rds')

username = "harishankar"
password = '2xcvdfg'
db_subnet_group = ''
db_cluster_id = 'test-1234-rds'

try:
    db_checker = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print("DB already exists")
except rds.exceptions.DBClusterNotFoundFault:
    response = rds.create_db_cluster(
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.08.3',
        DBClusterIdentifier=db_cluster_id
    )
    print(f"The DB cluster name '{db_cluster_id}' has been created")

    while True:
        response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters'][0]['Status']
        print(f"The status of the cluster is '{status}'")
        if status == 'available':
            break
        print("Waiting for the DB cluster to become available...")
        time.sleep(30)  # Adding a sleep to avoid making too many requests
