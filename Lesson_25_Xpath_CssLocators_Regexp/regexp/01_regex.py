# https://docs.python.org/3/library/re.html
# https://regex101.com/


import re

text = "ball call ball call"

regexp = re.match(pattern='ball call', string=text)
regexp2 = re.search('[bB]al{2,3}', text, flags=re.DEBUG)
regexp3 = re.findall('[tT]all', text)

text_wifi_iface = """3: wlp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether f0:d5:bf:3c:e0:83 brd ff:ff:ff:ff:ff:ff
    inet 192.168.150.116/24 brd 192.168.150.255 scope global dynamic noprefixroute wlp1s0
       valid_lft 2627sec preferred_lft 2627sec
    inet6 fe80::d04c:f4ab:20:17d3/64 scope link noprefixroute
       valid_lft forever preferred_lft forever"""

ip_addresses = re.findall('\d{3}\.\d{3}\.\d{3}\.\d{3}', text_wifi_iface)
print(type(ip_addresses))
print(ip_addresses)
ip_interface = re.findall(':\s.+:\s<', text_wifi_iface)
print(ip_interface)
