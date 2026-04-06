from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'183.192.{A}.0/22', False)
    if all(f'{int(ip):032b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break