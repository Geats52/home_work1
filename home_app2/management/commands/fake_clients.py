#Попытка создания фальшивых клиентов (Внимание работает не корректно!!!)
# >>> python manage.py fake_clients <колличество клиентов>

from django.core.management.base import BaseCommand
from home_app2.models import Client, Product, Order

class Command(BaseCommand):
    help = "Generate fake data."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', number_phone = f'{i}_{i}{i}{i}_{i}{i}{i}_{i}', adress = f'street_{i + 2}')
            user.save()
            for j in range(1, count + 1):
                client_order = Product(name=f'Name{j}', price=f'{i + j}', amount = f'{i * j}')
                client_order.save()
    