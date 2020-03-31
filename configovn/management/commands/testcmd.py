from django.core.management.base import BaseCommand, CommandError
from configovn.models import ConfigsInfo
from optparse import make_option
class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('poll_id', nargs='+', type=int)
        # Named (optional) arguments
        parser.add_argument('--delete',
                            action='store_true',
                            dest='delete',
                            default=False,
                            help='Delete poll instead of closing it')
    def handle(self, *args, **options):
        for poll_id in args:
            self.stdout.write('Successfully closed poll "%s"' % poll_id)
        raise CommandError('Poll "%s" does not exist' % args)
