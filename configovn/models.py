from django.db import models

configs="""local
remote
remote-random
remote-random-hostname
mode
proto
proto-force
connect-retry
connect-retry-max
http-proxy
http-proxy
http-proxy-option
socks-proxy
socks-proxy-retry
resolv-retry
float
ipchange
port
lport
rport
bind
nobind
dev
dev-type
dev-node
lladdr
topology
iproute
ifconfig
ifconfig-ipv6
ifconfig-noexec
ifconfig-nowarn
route
route-ipv6
route-gateway
route-metric
route-delay
route-up
route-pre-down
route-noexec
route-nopull
allow-pull-fqdn
redirect-gateway
redirect-private
client-nat
push-peer-info
setenv
setenv
ignore-unkown-option
script-security
shaper
keepalive
inactive
ping-exit
ping-restart
ping-timer-rem:
ping
multihome
fast-io
remap-usr1
persist-tun
persist-remote-ip
persist-local-ip
persist-key
passtos
tun-mtu
tun-mtu-extra
link-mtu
mtu-disc
mtu-test
fragment
mssfix
sndbuf
rcvbuf
mark
txqueuelen
memstats
mlock
up
up-delay
down
down-pre
up-restart
user
group
chroot
cd
daemon
syslog
inetd
log
log-append
suppress-timestamps
machine-readable-output
writepid
nice
echo
verb
mute
status
status-version
disable-occ
gremlin
compress
comp-lzo
comp-noadapt
management
management-client
management-query-passwords
management-query-proxy
management-query-remote
management-hold
management-signal
management-forget-disconnect
management-up-down
management-log-cache
management-client-user
management-client-group
management-client-auth
management-client-pf
plugin
server
server-ipv6
server-bridge
push
push-reset
ifconfig-pool
ifconfig-pool-linear
ifconfig-pool-persist
ifconfig-ipv6-pool
ifconfig-push
ifconfig-ipv6-push
iroute
iroute-ipv6
disable
client-cert-not-required
verify-client-cert
username-as-common-name
auth-user-pass-verify
opt-verify
auth-user-pass-optional
no-name-remapping
client-to-client
duplicate-cn
client-connect
client-disconnect
client-config-dir
ccd-exclusive
tmp-dir
hash-size
bcast-buffers
tcp-queue-limit
tcp-nodelay
learn-address
connect-freq
max-clients
max-routes-per-client
stale-routes-check
explicit-exit-notify
port-share
client
auth-user-pass
pull
pull-filter
auth-retry
static-challenge
connect-timeout
allow-recursive-routing
explicit-exit-notify
secret
auth
cipher
ncp-ciphers
ncp-disable
prng
keysize
engine
no-replay
mute-replay-warnings
replay-window
no-iv
replay-persist
test-crypto
tls-server
tls-client
key-method
ca
capath
dh
cert
extra-certs
key
tls-version-min
tls-version-max
pkcs12
x509-username-field
verify-hash
tls-cipher
tls-timeout
reneg-bytes
reneg-pkts
reneg-sec
hand-window
tran-window
single-session:
tls-exit
tls-auth
tls-crypt
askpass
auth-nocache
crl-verify
tls-verify
tls-export-cert
verify-x509-name
ns-cert-type
x509-track
keying-material-exporter
remote-cert-ku
remote-cert-eku
remote-cert-tls
pkcs11-providers
pkcs11-protected-authentication
pkcs11-private-mode
pkcs11-cert-private
pkcs11-pin-cache
pkcs11-id-management
pkcs11-id
show-ciphers
show-digests
show-engines
show-tls
genkey
secret
mktun
rmtun
dev
dev-type
user
group
show-pkcs11-ids
show-gateway"""
# Create your models here.

import psutil
from django import forms
#forms.TextInput

def get_netcard():
    netcard_info = [("0.0.0.0", 'Any:0.0.0.0')]
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2:
                netcard_info.append((item[1], k+":"+item[1]))
    return netcard_info


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class ConfigsInfo(models.Model):
    objects = models.Manager()
    #    (time.strftime('%Y.%m.%d %H-%m-%S-%s',time.localtime(time.time())))
    id = models.AutoField(primary_key=True)
    local = models.CharField(max_length=254, blank=True, verbose_name="监听网络地址",
                             choices=get_netcard(), default='0.0.0.0',
                             help_text="""选择绑定本机网络地址,默认监听所有网络地址""")
    from enum import Enum
    class ProtoChoice(Enum):
        TCP = "TCP"
        UDP = "UDP"
        # BOTH = "TCP和UDP"

    proto = models.CharField(max_length=254, blank=False, verbose_name="协议选择",default='UDP',
                             choices=[(tag.value, tag.name) for tag in ProtoChoice],
                             help_text="""选择服务端支持的协议类型""")
    from django.contrib.auth.models import User
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    from django.core.validators import MaxValueValidator, MinValueValidator

    port = models.IntegerField(blank=False, default='1195', verbose_name="监听网络端口",unique=True,
                               validators=[MaxValueValidator(65534), MinValueValidator(1024)],
                               help_text="""选择绑定本机网络端口,默认监听1195""")
    duplicate_cn = models.BooleanField(blank=True, default=True, verbose_name="是否允许多用户共享认证文件",
                               help_text="""仅针对服务器端配置,决定是允许多用户共享一份认证文件""")

    def __str__(self):
        return u'ConfigsInfo'

    def save(self, *args, **kwargs):
        # do_something()
        print("ssssssssssssssssssssssss")
        print(kwargs)
        print(args)
        super(ConfigsInfo, self).save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        db_table = "ConfigsInfo"
        ordering = ('id',)
        verbose_name = verbose_name_plural = u'基础配置'


class ConfigsAdvanced(models.Model):
    objects = models.Manager()
    #    (time.strftime('%Y.%m.%d %H-%m-%S-%s',time.localtime(time.time())))
    id = models.AutoField(primary_key=True)
    fileds = locals()
    for i in configs.split():
        fileds[i] = models.CharField(max_length=254, blank=True, verbose_name=i)

    def __str__(self):
        return u'ConfigAdvanced'

    class Meta:
        db_table = "ConfigsAdvanced"
        ordering = ('id',)
        verbose_name = verbose_name_plural = u'高级配置'
