import json
from datetime import datetime
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    ec2 = boto3.client('ec2')
    current_date = datetime.now().strftime("%Y%M%D")
    try:
       response = ec2.create_snapshot(
           VolumeId='',
           Description='',
           TagSpecifications=[
               {
                   'ResourceType': 'snapshot',
                   'Tags' : [
                       {
                           'key': 'Name',
                           'Value': f"my snapshot {current_date}"
                       }
                   ]
               }
           ] 
       )
       logger.info(f"print the reponse of volume: {json.dumps(response, default=str)}")
    except Exception as e:
         logger.info(f"print the logger: {json.dumps(e)}")

if __name__ == "__main__":
    main()