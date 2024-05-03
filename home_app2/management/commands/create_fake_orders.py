from random import *
from django.core.management.base import BaseCommand
from home_app2.models import Order, Product, Client
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Generate random orders, users, and products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of orders to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clients = list(Client.objects.all())
        products = list(Product.objects.all())

        start_date = datetime(2010, 1, 1)
        end_date = datetime(2024, 1, 24)

        for _ in range(count):
            client = choice(clients)
            products_for_order = sample(products, randint(1, len(products)))
            total_amount = sum(product.price for product in products_for_order)

            random_seconds = randint(0, int((end_date - start_date).total_seconds()))
            random_date = start_date + timedelta(seconds=random_seconds)


            order = Order.objects.create(client=client, total_amount=total_amount, order_date=random_date)
            order.products.add(*products_for_order)
            self.stdout.write(f'Order created: {order.id}')