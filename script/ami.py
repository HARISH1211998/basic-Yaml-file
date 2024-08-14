import boto3
from datetime import datetime, timedelta

def get_recent_amis(days=30):
    ec2 = boto3.client('ec2')
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    print(start_date)
    
    amis = ec2.describe_images(Owners=['self'])
    recent_amis = []

    for ami in amis['Images']:
        creation_date = ami['CreationDate']
        creation_datetime = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        if creation_datetime >= start_date:
            recent_amis.append({
                'ImageId': ami['ImageId'],
                'CreationDate': creation_date,
                'Name': ami['Name']
            })

    return recent_amis

# Print recent AMIs
for ami in get_recent_amis():
    print(f"AMI ID: {ami['ImageId']}, Name: {ami['Name']}, Creation Date: {ami['CreationDate']}")
