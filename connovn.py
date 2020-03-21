#!/usr/bin/env python3
import os, sys
import django
import logging
import time
from optparse import OptionParser

# ifconfig_pool_local_ip=10.9.3.5 config=server4.ovpn time_unix=1584755922 IV_NCP=2 verb=9 daemon=0 ifconfig_remote=10.9.3.2
# VIRTUAL_ENV=/home/binnary/py3env untrusted_port=45003 IV_LZO=1 IV_LZ4v2=1 IV_LZ4=1 dev=tun1 daemon_pid=7284 tun_mtu=1500
# PWD=/home/binnary/work/ovn/ovn_test local_port_1=1194 IV_PROTO=2 dev_type=tun untrusted_ip=127.0.0.1 daemon_log_redirect=0
# ifconfig_pool_remote_ip=10.9.3.6 remote_port_1=1194 redirect_gateway=0 username=binnary trusted_port=45003
# route_vpn_gateway=10.9.3.2 link_mtu=1622 IV_COMP_STUBv2=1 IV_COMP_STUB=1 script_context=init IV_VER=2.4.4
# route_gateway_1=10.9.3.2 SHLVL=1 route_netmask_1=255.255.255.0 IV_TCPNL=1 proto_1=udp script_type=client-connect
# time_ascii=Sat Mar 21 09:58:42 2020 common_name=binnary ifconfig_local=10.9.3.1 route_network_1=10.9.3.0 IV_PLAT=linux
# route_net_gateway=192.168.31.254 daemon_start_time=1584752362 trusted_ip=127.0.0.1 _=/usr/bin/env
# >CLIENT:ESTABLISHED,2
# >CLIENT:ENV,n_clients=1
# >CLIENT:ENV,time_unix=1584690581
# >CLIENT:ENV,time_ascii=Fri Mar 20 15:49:41 2020
# >CLIENT:ENV,ifconfig_pool_local_ip=10.9.3.5
# >CLIENT:ENV,ifconfig_pool_remote_ip=10.9.3.6
# >CLIENT:ENV,trusted_port=49810
# >CLIENT:ENV,trusted_ip=192.168.31.61
# >CLIENT:ENV,common_name=admin
# >CLIENT:ENV,untrusted_port=49810
# >CLIENT:ENV,untrusted_ip=192.168.31.61
# >CLIENT:ENV,username=admin
# >CLIENT:ENV,script_type=user-pass-verify
# >CLIENT:ENV,remote_port_1=1194
# >CLIENT:ENV,local_port_1=1194
# >CLIENT:ENV,proto_1=udp
# >CLIENT:ENV,daemon_pid=31149
# >CLIENT:ENV,daemon_start_time=1584432788
# >CLIENT:ENV,daemon_log_redirect=0
# >CLIENT:ENV,daemon=1
# >CLIENT:ENV,verb=7
# >CLIENT:ENV,config=server4.ovpn
# >CLIENT:ENV,ifconfig_local=10.9.3.1
# >CLIENT:ENV,ifconfig_remote=10.9.3.2
# >CLIENT:ENV,route_net_gateway=192.168.6.254
# >CLIENT:ENV,route_vpn_gateway=10.9.3.2
# >CLIENT:ENV,route_network_1=10.9.3.0
# >CLIENT:ENV,route_netmask_1=255.255.255.0
# >CLIENT:ENV,route_gateway_1=10.9.3.2
# >CLIENT:ENV,script_context=init
# >CLIENT:ENV,tun_mtu=1500
# >CLIENT:ENV,link_mtu=1557
# >CLIENT:ENV,dev=tun1
# >CLIENT:ENV,dev_type=tun
# >CLIENT:ENV,redirect_gateway=0
# >CLIENT:ENV,END
logger = logging.getLogger(__name__)


def main():
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovn.settings')
    django.setup()

    from status.models import CurrentUsers
    if CurrentUsers.objects.select_for_update().filter(
            common_name=os.environ['common_name'],
            trusted_port=os.environ['trusted_port'],
            trusted_ip=os.environ['trusted_ip']).update(
                 trusted_ip=os.environ['trusted_ip'],
                 local_port=os.environ['local_port_1'],
                 protocol=os.environ['proto_1'],
                 trusted_port=os.environ['trusted_port'],
                 online=u'在线',
                 starting_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                 ifconfig_pool_netmask=os.environ['route_netmask_1']) == 0:
        CurrentUsers.objects.create(
            common_name=os.environ['common_name'],
            trusted_ip=os.environ['trusted_ip'],
            local_port=os.environ['local_port_1'],
            protocol=os.environ['proto_1'],
            trusted_port=os.environ['trusted_port'],
            online=u'在线',
            starting_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            ifconfig_pool_netmask=os.environ['route_netmask_1'],
            ifconfig_pool_remote_ip=os.environ['ifconfig_pool_remote_ip'])
    return 0


if __name__ == '__main__':
    # parser = OptionParser()
    # parser.add_option("--trusted_ip", dest="trusted_ip", help="trusted ip")
    # parser.add_option("--trusted_port", dest="trusted_port", help="trusted port")
    # parser.add_option("--remote_ip", dest="remote_ip", help="ifconfig_pool_remote_ip")
    # parser.add_option("--netmask", dest="netmask", help="ifconfig_pool_netmask")
    # parser.add_option("--common_name", dest="cname", help="common name")
    # parser.add_option("--protocol", dest="proto", help="protocol tcp or udp")
    # parser.add_option("--start-time", dest="stime", help="starting time")
    # parser.add_option("--recvByte", dest="rbytes", help="received bytes")
    # parser.add_option("--sentByte", dest="sbytes", help="sent bytes")
    # (options, args) = parser.parse_args()
    sys.exit(main())
