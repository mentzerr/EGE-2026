from ipaddress import *

cnt = 0

for A in range(256):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/27', False)
    if ip not in (net.network_address, net.broadcast_address):
        if all(f'{int(ip):032b}'[16:24].count('0') > f'{int(ip):032b}'[24:].count('0') for ip in net.hosts()):
            cnt += 1
print(cnt)

