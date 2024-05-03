from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField(default=None)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Клиент: {self.name}, эл.адресс: {self.email}, тел.: +{self.phone_number}, адресс проживания: {self.address},')

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=None)
    added_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return (f'Товар: {self.name}, описание: {self.description}, ценна={self.price} "RUB", количество: {self.quantity} "шт.", дата добавления: {self.added_date}')

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        product_names = ', '.join([product.name for product in self.products.all()])
        return (f'Детали заказа: Имя клиента - {self.client.name}, телефон клиента + {self.client.phone_number}, товары в заказе - {product_names}, общая ценна = {self.total_amount}')