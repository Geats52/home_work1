#Команда для добавления/регистрации нового клиента
# >>> python manage.py add_client

from django.core.management.base import BaseCommand
from home_app2.models import Client

class Command(BaseCommand):
	help = "Create user."
	
	def handle(self, *args, **kwargs):
		
		client = Client(name='Boris', email='bak@mail.ru', number_phone = 7_777_237_1, adress ='homeland_52', data_registration = True)

		...
		client.save()
		self.stdout.write(f'{client}')
		