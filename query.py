#!/usr/bin/env python3
import os, sys
import django
import logging
from optparse import OptionParser

logger = logging.getLogger(__name__)
def main(u, p):
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovn.settings')
    django.setup()
    from django.contrib.auth import authenticate
    from django.contrib.auth.models import User, UserManager
    user = authenticate(username=u, password=p)
    if user is None:
        return 1
    return 0


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user", help="user name")
    parser.add_option("-p", "--password", dest="pwd", help="user password")

    (options, args) = parser.parse_args()
    if options.user == None:
        sys.exit(2)
    if options.pwd == None:
        sys.exit(2)
    sys.exit(main(options.user, options.pwd))
