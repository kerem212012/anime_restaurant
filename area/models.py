import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CASCADE, CharField, ForeignKey
from django.utils import timezone
from user.models import CustomUser


class ProductType(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )
    picture = models.ImageField(
        'Picture'
    )
    description = models.TextField(
        'Description',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )
    picture = models.ImageField(
        'Picture'
    )
    description = models.TextField(
        'Description',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name


class ProductIngredient(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )
    picture = models.ImageField(
        'Picture'
    )
    description = models.TextField(
        'Description',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name

class Anime(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name")
    description = models.TextField(max_length=300, blank=True,verbose_name="Description")
    picture = models.ImageField(verbose_name="Picture")
    user = models.ManyToManyField(
        CustomUser,
        verbose_name="User"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        MANAGER = "M", "Transferred to manager"
        RESTAURANT = "R", "Transferred to the restaurant"
        COURIER = "C", "Handed over to the courier"
        PROCESSED = "P", "Processed"

    status = models.CharField(max_length=1, choices=StatusChoice.choices, verbose_name="Статус", db_index=True,
                              default=StatusChoice.MANAGER)
    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name="users",
        verbose_name="User"
    )
    address = models.TextField(verbose_name="Delivery address")
    is_draft = models.BooleanField(default=True,verbose_name="Is Draft")
    order_note = models.TextField(max_length=200, verbose_name="Order Note", blank=True)
    registered_at = models.DateTimeField(verbose_name="Registered at", default=timezone.now)
    called_at = models.DateTimeField(verbose_name="Called at", db_index=True, blank=True, null=True)
    delivered_at = models.DateTimeField(verbose_name="Delivered at", db_index=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} | {self.status}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
class Product(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        'Name',
        max_length=50
    )
    picture = models.ImageField(
        'Picture'
    )
    description = models.TextField(
        'Description',
        blank=True,
        max_length=300,
    )
    price = models.DecimalField(
        'Price',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    product_type = ForeignKey(
        ProductType,
        related_name='types',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Product Type"

    )
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name="Product Category",
        related_name="products_categories"
    )
    product_ingredient = models.ForeignKey(
        ProductIngredient,
        related_name='ingredients',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Product Ingredient"
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
        related_name="animes",
        verbose_name="Anime"
    )
    size = CharField(max_length=50, verbose_name="Size",null=True,blank=True)

    def __str__(self):
        return self.name


class OrderElement(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order",
        related_name="orders"
    )
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Product",
        related_name="products"
    )
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)], default=0)
    quantity = models.IntegerField(verbose_name="Quantity")

    class Meta:
        verbose_name = 'Order Element'
        verbose_name_plural = 'Order Elements'


class Event(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )
    description = models.TextField(
        'Description',
        blank=True,
        max_length=300,
    )
    picture = models.ImageField(
        'Picture',
        default=None
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
        verbose_name="Anime",
    )
    data = models.DateTimeField(verbose_name="Data")

    def __str__(self):
        return self.name
