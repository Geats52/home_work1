#Команда для добавления/регистрации нового товара
# >>> python manage.py add_goods

from django.core.management.base import BaseCommand
from home_app2.models import Product

class Command(BaseCommand):
	help = "Create product."
	
	def handle(self, *args, **kwargs):
		

		product = Product(name='Беговая дорожка', description = 'Спортивный инвентарь', price = 5500.777, amount = 500, data_add = True)


		...
		product.save()
		self.stdout.write(f'{product}')
		