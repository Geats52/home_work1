#Команда для выявления списка всех клиентов
# >>> python manage.py get_all_clients

from django.core.management.base import BaseCommand
from home_app2.models import Client

class Command(BaseCommand):
	help = "Get all clients."
	
	def handle(self, *args, **kwargs):
		users = Client.objects.all()
		self.stdout.write(f'{users}')