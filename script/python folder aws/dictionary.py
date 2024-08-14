def main():
    aws_service = {
        "s3": "simple storage serivce",
        "lambda": "serverless arthitect",
        "EC2": "Service",
        "dynamodb": "No sql"
    }
    print(aws_service)
    # Print any 2 dictorinory
    print(f"Print the second dictornary key {aws_service['lambda']}")
    # Removed last key value
    del aws_service["dynamodb"]
    print(aws_service)
    # print keys(),items() and values()
    print(f"Print all keys {aws_service.keys()}")
    print(f"Print all values {aws_service.values()}")
    print(f"print all items: {aws_service.items()}")

    # Added one more keys values pair in dictionary
    aws_service['RDS'] = "Releation Database"
    print(aws_service)

    # Nested value 
    aws_service["RDS"] = {
        "mysql": 12,
        "psql": 13,
        "describtion": "update all version"
    }
    print(aws_service["RDS"])
    print(aws_service)
    return aws_service

if __name__ == '__main__' :
    main()