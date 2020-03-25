#!/usr/bin/env python

import psutil
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 :
                netcard_info.append((k,item[1]))
    return netcard_info
if __name__ == '__main__':
    print(get_netcard())
