from ipaddress import *

for mask in range(16, 25):
    ip = ip_address('187.124.21.237')
    net = ip_network(f'{ip}/{mask}', False)
    if ip not in (net.network_address, net.broadcast_address):
        if all(f'{int(ip):032b}'[:16].count('1') >= f'{int(ip):032b}'[16:].count('1') for ip in net):
            print(net.netmask)
            break