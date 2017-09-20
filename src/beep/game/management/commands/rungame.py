from django.core.management.base import BaseCommand
import random

# Models
from game.models import *
from time import sleep

class Command(BaseCommand):
    args = 'none'
    help = 'Run the BeeP game'

    def handle(self, *args, **options):
        while True:
            print "Game on...."
            cl = list(Client.objects.filter(points_for_scan=0))

            if cl:
                client = random.choice(cl)
                client.dur_on=0.9
                client.dur_off=0.1
                client.points_for_scan=1
                client.save()
                print "Fired client: %s" % client.client_mac

            sleep(random.randint(1,10))
