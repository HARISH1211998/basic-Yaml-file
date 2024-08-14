def main():
    aws_service = [ "ec2", "sns", "dynamodb", "apigateway", "loadbalancer", "route53" ]
    # Print first value of the list
    print(f"Enter the list first value {aws_service[0]}")
    # print last value of this list
    print(f"Enter the list last value {aws_service[-1]}")
    # replace the second value of the list
    aws_service[3] = "Harishankar"
    print(aws_service)
    # remove 3 value from the list
    aws_service.pop(4)
    print(f"Remove the value of the list {aws_service}")
    # append the value in list
    aws_service.append("cloudfront")
    print(aws_service)
    # slice the value
    print(f"Slice value in list: {aws_service[0:5]}")

if __name__ == '__main__':
    main()
