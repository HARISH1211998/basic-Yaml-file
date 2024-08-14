import re
from collections import Counter

def file_logs_test(log_file):
    ips_patern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ips_counts = Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                ips = ips_patern.findall(line)
                ips_counts.update(ips)
            repeated_ips = {ips: count for ips, count in ips_counts.items() if count > 1}
            print(repeated_ips)
    except Exception as e:
        print(f"print all the error {e}")

log_file="./logs.json"
file_logs_test(log_file)