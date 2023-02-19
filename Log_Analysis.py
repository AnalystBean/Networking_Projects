from collections import Counter

log_file = 'access.log'

with open(log_file, 'r') as f:
    logs = f.readlines()

ip_addresses = [line.split()[0] for line in logs]
ip_count = Counter(ip_addresses)

for ip, count in ip_count.items():
    print(f'{ip} - {count}')