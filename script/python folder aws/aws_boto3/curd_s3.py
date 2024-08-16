import boto3 

s3 = boto3.resource('s3')
bucket_name = "cobraS312g"
all_bucket = [bucket.name for bucket in s3.buckets.all()]

# Create Function 
s3.create_bucket(Bucket=bucket_name)

# Added Function
buckets_name_uploaded = "redirect-cumberlandlabs-co"
file_1 = "./file_1.txt"
file_2 = "./file_2.txt"
s3.Bucket(buckets_name_uploaded).upload_file(Filename=file_1, Key=file_1)

# read the s3 files
obj = s3.Object(buckets_name_uploaded, file_1)
body = obj.get()['Body'].read()
print(body.decode('utf-8'))

# Update Function
s3.Object(buckets_name_uploaded, file_1).put(Body=open(file_2, 'rb'))
body = obj.get()['Body'].read()
print(body.decode('utf-8'))

# Delete Function
s3.Object(buckets_name_uploaded, file_1).delete()


