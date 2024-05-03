#Удаление клиента
# >>> python manage.py delete_client <id клиента>

from django.core.management.base import BaseCommand
from home_app2.models import Client

class Command(BaseCommand):
	help = "Delete user by id."

	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='Client ID')

	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')

		client = Client.objects.filter(pk=pk).first()
		if client is not None:
			client.delete()
		self.stdout.write(f'{client}')