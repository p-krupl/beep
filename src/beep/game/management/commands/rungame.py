from django.core.management.base import BaseCommand


# Models
from game.models import *
from time import sleep

class Command(BaseCommand):
    args = 'none'
    help = 'Run the BeeP game'

    def handle(self, *args, **options):
        while True:
            print "Game on...."
            sleep(1)
