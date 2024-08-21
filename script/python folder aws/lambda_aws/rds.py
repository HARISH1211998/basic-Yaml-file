import boto3
from datetime import datetime

# Initialize an RDS client
rds_client = boto3.client('rds')

# Describe the specific DB instance
response = rds_client.describe_db_instances(DBInstanceIdentifier='threetrade-uat-testnet')

# Extract the DB instance details
db_instance = response['DBInstances'][0]

# Create a snapshot name with a timestamp to ensure uniqueness
snapshot_identifier = f"{db_instance['DBInstanceIdentifier']}-snapshot-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Create a snapshot for the DB instance
snapshot_response = rds_client.create_db_snapshot(
    DBInstanceIdentifier=db_instance['DBInstanceIdentifier'],
    DBSnapshotIdentifier=snapshot_identifier
)

# Print the details of the created snapshot
print("Snapshot creation initiated:")
print(f"Snapshot Identifier: {snapshot_response['DBSnapshot']['DBSnapshotIdentifier']}")
print(f"Snapshot Status: {snapshot_response['DBSnapshot']['Status']}")
print(f"Snapshot Creation Time: {snapshot_response['DBSnapshot']['SnapshotCreateTime']}")
