#Обновление товара по цене товара по колличеству на складе
# >>> python manage.py goods_price_update <№ id товара> <новая ценна товара>
from django.core.management.base import BaseCommand
from home_app2.models import Product

class Command(BaseCommand):
	help = "Update product status name by id."

	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='Product ID')
		parser.add_argument('price', type=float, help='Product price')
		
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		price = kwargs.get('price')
		user = Product.objects.filter(pk=pk).first()
		user.price = price
		user.save()
		self.stdout.write(f'{user}')