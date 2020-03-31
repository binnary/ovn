from django.core.management.base import BaseCommand, CommandError
from configovn.models import ConfigsInfo
from optparse import make_option
class Command(BaseCommand):
#    args = '<server|client>'
    help = 'auto gen ovnconfig'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('type', nargs='+', type=str)
        # Named (optional) arguments
        parser.add_argument('--user',  dest='user', help='user name')
        parser.add_argument('--password',  dest='pass',  help='password')
        parser.add_argument('--server',  dest='server', help='config type(server or client)')

    def handle(self, *args, **options):
        print(args, options)

        self.stdout.write(options['user'])
        self.stdout.write(options['pass'])
        self.stdout.write(options['server'])
        return 0
        #for poll_id in args:
        #    self.stdout.write('Successfully closed poll "%s"' % poll_id)
        #raise CommandError('Poll "%s" does not exist' % args)
