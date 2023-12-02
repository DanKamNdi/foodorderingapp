from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image/", max_length=250, null=True, default=None)
    url = models.URLField(null=True)


class Product(models.Model):
    p_title = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_image = models.FileField(upload_to="myapp/static/images/products", max_length=200, null=True)


# models.py
class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem')

    @property
    def total_cost(self):
        return sum(item.total for item in self.cartitem_set.all())

    def __str__(self):
        return f"Cart {self.id}"


# models.py
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def total(self):
        return self.quantity * self.product.p_price

    def __str__(self):
        return f"{self.quantity} x {self.product.p_price} in {self.cart}"


class Features(models.Model):
    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=100)
    fea_img = models.ImageField(upload_to="Features/", max_length=100, null=True)


class Categories(models.Model):
    title = models.CharField(max_length=40)
    discount = models.IntegerField()
    img = models.ImageField()


# # Create your models here.
# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)


class Userregistration(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key=True)
    passw = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="profile/", max_length=100, null=True)


class Bannerdesc(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


class Addreview(models.Model):
    ureview = models.CharField(max_length=100)
