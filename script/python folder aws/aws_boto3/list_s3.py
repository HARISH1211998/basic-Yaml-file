import boto3

def main():
    s3 = boto3.resource('s3')
    for buckets in s3.buckets.all():
        if buckets.name not in "digitali.xyz":
            print(f"they is no bucket avaliable you can create the new bucket {buckets.name}")
        else:
            print(f"bucket is already exists {buckets.name}")

if __name__ == '__main__':
    main()