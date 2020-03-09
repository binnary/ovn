#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os,sys
import django

def main():
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovn.settings')
    django.setup()
    from django.contrib.auth import authenticate
    from django.contrib.auth.models import User, UserManager
    user = authenticate(username='admin123', password='1qaz2wsx')
    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    print(user)
    #try:
    #    from django.core.management import execute_from_command_line
    #except ImportError as exc:
    #    raise ImportError(
    #        "Couldn't import Django. Are you sure it's installed and "
    #        "available on your PYTHONPATH environment variable? Did you "
    #        "forget to activate a virtual environment?"
    #    ) from exc
    #execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
