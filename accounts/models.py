from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="user.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY) 
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return str(self.product.name)


# Command Prompt Shell

'''
from accounts.models import *
customers = customer.objects.all()
print(customers)
Mudassir ,Shahbaz
print(customers.first())
Mudassir
print(customer1.email)
zeyamudassir@gmail.com
print(customer1.id)
1
customer2 = Customer.objects.get(id=2)
print(customer2)
Shahbaz
orders = customer2.order_set.all()
print(orders)
Order object (3)
order = Order.objects.first()
print(order,customer.name)
Mudassir
print(order.customer.phone)
7506164227
products = Product.objects.filter()
print(products)
BBQ Grill, Dishes, Ball
products = Product.objects.filter(category="Outdoor")
print(products)
BBQ Grill, Ball
products = Product.objects.all().order_by('id')
print(products)
BBQ Grill, Dishes, Ball
products = Product.objects.all().order_by('-id')
print(products)
Ball, Dishes, BBQ Grill

'''
