#Команда для проверки работоспособности приложения
# >>> python manage.py greeting  
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = "Print 'Hello World!' to output."

	def handle(self, *args, **kwargs):
		self.stdout.write('Hello world!')