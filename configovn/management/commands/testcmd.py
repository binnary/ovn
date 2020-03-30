from django.core.management.base import BaseCommand, CommandError
from configovn.models import ConfigsInfo
from optparse import make_option
class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        #BaseCommand.options_
        #option_list = BaseCommand.option_list + (
        #    make_option('--delete',
        #                action='store_true',
        #                dest='delete',
        #                default=False,
        #                help='Delete poll instead of closing it'),
        #)
        for poll_id in args:
            self.stdout.write('Successfully closed poll "%s"' % poll_id)
        raise CommandError('Poll "%s" does not exist' % args)
