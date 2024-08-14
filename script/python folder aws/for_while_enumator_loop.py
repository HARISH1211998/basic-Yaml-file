def main():
    aws_service = ["s3", "lambda", "codecommit", "ec2", "ALB"]
    # print the for loop all value 
    print("\nPrint all value in list by using of for loop")
    for service in aws_service:
        print(service)

    # print the while loop all value 
    print("\nPrint all value in list by using of while loop")
    index = len(aws_service) - 1
    while index >= 0:
        print(aws_service[index])
        index -= 1
    
    # print enumator() loop
    print("\nPrint enumator loop in aws")
    for index,service in enumerate(aws_service):
        print(f"Enter the type {index}: {service}")
if __name__ == '__main__' :
    main()