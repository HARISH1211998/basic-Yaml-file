def main():
    service = "s3"
    get_service = getService(service)
    if get_service == 'none':
        print(f"they is no serice avaliable in aws")
    else:
        print(f"The service describes {get_service}")


def getService(service):
    aws = {
        "s3": "storage",
        "RDS": "Database",
        "DynamoDB": "Nosql",
        "EKS": "Kubernetes",
        "SNS": "Notification"
    }
    try:
        return aws[service]
    except KeyError as e:
        print(f"\n The error from keyerror:{e}")

if __name__ == '__main__':
    main()