#Команда для выявления конкретного клиента
# >>> python manage.py get_one_client <id клиента>

from django.core.management.base import BaseCommand
from home_app2.models import Client

class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
