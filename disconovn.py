#!/usr/bin/env python3
import os, sys
import django
import logging
import time
from optparse import OptionParser

# os.environ['common_name']
# os.environ['trusted_ip']
# os.environ['ifconfig_pool_remote_ip']
# os.environ['ifconfig_pool_netmask']
# os.environ['local_port']
# os.environ['trusted_port']
# os.environ['bytes_sent']
# os.environ['bytes_received']

logger = logging.getLogger(__name__)


# end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
# print time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
def main():
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovn.settings')
    django.setup()
    from status.models import CurrentUsers
    if CurrentUsers.objects.select_for_update().filter(
            common_name=os.environ['common_name'],
            trusted_port=os.environ['trusted_port'],
            trusted_ip=os.environ['trusted_ip']).update(
                local_port=os.environ['local_port_1'],
                bytes_sent=os.environ['bytes_sent'],
                bytes_received=os.environ['bytes_received'],
                ifconfig_pool_netmask=os.environ['route_netmask_1'],
                end_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                online=u'离线') == 0:
        CurrentUsers.objects.create(
            common_name=os.environ['common_name'],
            trusted_ip=os.environ['trusted_ip'],
            local_port=os.environ['local_port_1'],
            bytes_sent=os.environ['bytes_sent'],
            bytes_received=os.environ['bytes_received'],
            end_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            ifconfig_pool_netmask=os.environ['route_netmask_1'],
            ifconfig_pool_remote_ip=os.environ['ifconfig_pool_remote_ip'],
            online=u'离线')
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
