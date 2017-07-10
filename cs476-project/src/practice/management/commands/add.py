from django.core.management.base import BaseCommand, CommandError
from practice.models import *

class Command(BaseCommand):
    help = 'add data to databases: add model filename'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str)
        parser.add_argument('filename', type=str)
        parser.add_argument('chapter', type=int)

    def handle(self, *args, **options):
        man = Manager()
        return man.add(model=options['model'],filename=options['filename'],chapter=options['chapter'])
        