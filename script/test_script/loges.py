import re
from collections import Counter

# Function to extract IP addresses from a log file
def find_repeated_ips(log_file_path):
    # Regular expression pattern for matching IP addresses
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    # Dictionary to keep track of IP address counts
    ip_counts = Counter()

    try:
        # Open the log file and read it line by line
        with open(log_file_path, 'r') as file:
            for line in file:
                # Find all IP addresses in the line
                ips = ip_pattern.findall(line)
                # Update the count for each IP address found
                ip_counts.update(ips)
                
        # Check for and print any repeated IP addresses
        repeated_ips = {ip: count for ip, count in ip_counts.items() if count > 1}
        if repeated_ips:
            for ip, count in repeated_ips.items():
                print(f"IP Address {ip} is repeated {count} times.")
        else:
            print("No IP addresses are repeated.")
    
    except FileNotFoundError:
        print(f"The file {log_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
log_file_path = 'path/to/your/logfile.log'
find_repeated_ips(log_file_path)
