#!/usr/bin/env python3
import os, sys
import django
import logging
import time
from optparse import OptionParser
logger = logging.getLogger(__name__)
#default config
def_global_cfg={
'dev':'tun',
'proto':'udp',
'keepalive':'10 40',
'resolv-retry':'infinite',
'persist-key':'',
'persist-tun':'',
'cipher':'AES-256-CBC',
'verb':'3',
'mute':'20',
}
#'ca':'ca.crt',
#'cert':'client.crt',
#'key':'client.key',
def_client_config={
'remote':'127.0.0.1 1194',
'management':'0.0.0.0 1198',
'nobind':'',
}
#'management-query-passwords':'',
#'auth-user-pass':'',
#'remote-cert-tls':'server',
def_server_config={
'port':'1194',
'server':'10.9.0.0 255.255.255.0',
'ifconfig-pool-persist':'ipp.txt',
'push':'"route 10.9.0.0 255.255.255.0 vpn_gateway 500"',
'duplicate-cn':'',
}
def save_config(configs):
    out=""
    for key in configs:
       out+=key+" "+configs[key]+"\n"
    return out

#set default env
def default_env_setup():
    CURPATH=os.path.dirname(os.path.abspath(__name__))
    os.environ['EASY_RSA'] = os.path.join(CURPATH, "easy-rsa")
    os.environ['OPENSSL']= "openssl"
    os.environ['GREP']="grep"
    os.environ['KEY_DIR']= os.path.join(CURPATH,"keys")
    os.environ['KEY_CONFIG']=os.path.join(os.environ['EASY_RSA'], "openssl.cnf")
    os.environ['KEY_SIZE']='2048'
    os.environ['CA_EXPIRE']='3650'
    os.environ['KEY_EXPIRE']='3650'
    os.environ['KEY_COUNTRY']="US"
    os.environ['KEY_PROVINCE']="SX"
    os.environ['KEY_CITY']="XA"
    os.environ['KEY_ORG']="DTT"
    os.environ['KEY_EMAIL']="admin@dtt.com"
    os.environ['KEY_OU']="CICT"
    os.environ['KEY_NAME']="DTT_OVN_EasyRSA"
    os.environ['PKCS11_PIN']="dummy"
    os.environ['PKCS11TOOL']="pkcs11-tool"
    os.environ['PKCS11_MODULE_PATH']="dummy"

def client_env_setup(mail=None, name=None):
    default_env_setup()
    if mail is not None:
         os.environ['KEY_mail']=mail
    if name is not None:
         os.environ['KEY_NAME']=name
def server_env_setup(mail=None, name=None):
    default_env_setup()
    if mail is not None:
         os.environ['KEY_mail']=mail
    if name is not None:
         os.environ['KEY_NAME']=name
def main():
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovn.settings')
    django.setup()

    from status.models import CurrentUsers
    return 0

def GenServerKeys(name='server'):
     if os.path.exists(os.getenv('KEY_DIR')) is False:
         os.system("mkdir -p " + os.getenv('KEY_DIR'))
     try:
         with open(os.getenv('KEY_DIR')+'/index.txt', "w+") as f:
           f.truncate()
     except:
           os.system("touch " + os.getenv('KEY_DIR')+'/index.txt')
     try:
         with open(os.getenv('KEY_DIR')+'/serial', "w+") as f:
           f.truncate()
           f.write('01')
     except:
           os.system("echo 01 > " + os.getenv('KEY_DIR')+'/serial')
     os.system(os.getenv('EASY_RSA')+"/pkitool --initca ")
     os.system("$OPENSSL dhparam -out ${KEY_DIR}/dh${KEY_SIZE}.pem ${KEY_SIZE}")
     os.system(os.getenv('EASY_RSA')+"/pkitool --server "+ name)

def GenClientKeys(name='client_default'):
     os.system(os.getenv('EASY_RSA')+"/pkitool "+ name)

def readkeys(start, end, fname):
    with open(str(os.getenv('KEY_DIR')+'/' + fname), 'r') as f:
       key = start 
       for line in f.readlines():
          key += line
       key+= end
       return key
def GenServerConfig(name='server', mail='null_client@dtt.cn'):
    server=''
    server_env_setup(mail=mail, name=name)
    for key in def_global_cfg:
        server+=key +' ' + def_global_cfg[key] +'\n'
    for key in def_server_config:
        server+= key +' ' + def_server_config[key]+'\n'
    os.system(os.getenv('EASY_RSA')+"/pkitool --initca ")
    GenServerKeys(name)
    server +=readkeys('<ca>\n', '</ca>\n', 'ca.crt')
    server +=readkeys('<cert>\n', '</cert>\n', name+'.crt')
    server +=readkeys('<key>\n', '</key>\n', name+'.key')
    server +=readkeys('<dh>\n', '</dh>\n', 'dh'+os.getenv('KEY_SIZE') + '.pem')
    return server
def GenClientConfig(name='client_default', mail='null_client@dtt.cn'):
    client='client\n'
    for key in def_global_cfg:
        client+=key +' ' + def_global_cfg[key] +'\n'
    for key in def_client_config:
        client+= key +' ' + def_client_config[key]+'\n'
    client_env_setup(mail=mail, name=name)
    GenClientKeys(name)
    client +=readkeys('<ca>\n', '</ca>\n', 'ca.crt')
    client +=readkeys('<cert>\n', '</cert>\n', name+'.crt')
    client +=readkeys('<key>\n', '</key>\n', name+'.key')
    return client


if __name__ == '__main__':
     parser = OptionParser()
     parser.add_option("--host-type", dest="htype", help="client or server")
     parser.add_option("--host-name", dest="hname", help="host name")
     parser.add_option("--mail", dest="mail", help="email addresss")
     parser.add_option("--password", dest="password", help="user")
     #parser.add_option("--interact", dest="interact", help="interact")
     (options, args) = parser.parse_args()
      
     mail='default@dtt.cn'      
     name=str(options.htype)+'01'

     if options.hname is not None:
         name=options.hname
     if options.mail is not None:
         mail=options.mail

     if options.htype == 'server' :
          print(GenServerConfig(name=name, mail=mail))
     elif options.htype == 'client' :
           print(GenClientConfig(name=name, mail=mail))
     else:
          pass
       
     sys.exit()
