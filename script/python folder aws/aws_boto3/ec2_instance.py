import boto3

# Specify the region when creating the resource
ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
Instance_name = 'test'
instance_exists = False
instance_ids = []  # Initialize as a list

# Check if the instance already exists
ec2_get_all = ec2.instances.all()
for instance in ec2_get_all:
    if instance.tags:  # Ensure tags is not None
        for tags in instance.tags:
            if tags['Key'] == 'Name' and tags['Value'] == Instance_name:
                instance_exists = True
                print(f"Instance already exists: {instance.id}")
                instance_ids.append(instance.id)  # Append to list
                break

print(f"Instance IDs: {instance_ids}")

# Create a new instance if none exists
if not instance_exists:
    ec2_key = ec2.create_instances(
        ImageId='ami-0a72af05d27b49ccb',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[
            {
                'ResourceType': 'instance',  # Corrected the spelling
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Instance_name
                    }
                ]
            }
        ]
    )
    new_instance_id = ec2_key[0].id
    print(f"Created new instance: {new_instance_id}")


if instance_ids:
    instance_id = instance_ids[0]  # Focus on the first instance
    instance = ec2.Instance(instance_id)

    # Terminate the instance
    instance.terminate()
    print(f"Terminating instance {instance_id}")
    instance_ids.remove(instance_id)


# Stop the instances
for instance_id in instance_ids:
    instance = ec2.Instance(instance_id)
    instance.stop()  # Correct method name
    print(f"Stopping instance {instance_id}")