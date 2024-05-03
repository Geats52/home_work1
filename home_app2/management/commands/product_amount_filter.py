#Фильтрация товара по колличеству на складе
# >>> python manage.py goods_amount_filter  <примерное колличество продукта>, 
#дает список товаров, но исключает те товары, чье колличество указываем
from django.core.management.base import BaseCommand
from home_app2.models import Goods

class Command(BaseCommand):
	help = "Get product with amount <amount>."

	def add_arguments(self, parser):
		parser.add_argument('amount', type=int, help='Goods amount')

	def handle(self, *args, **kwargs):
		amount = kwargs['amount']
		product = Goods.objects.filter(amount__gt=amount)
		self.stdout.write(f'{product}')
