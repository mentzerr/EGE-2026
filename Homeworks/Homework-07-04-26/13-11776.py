from ipaddress import ip_network

cnt = 0
net = ip_network('235.86.56.0/21', False)

for ip in net:
    if f'{int(ip):032b}'[-2:] == '11':
        cnt += 1
print(cnt)