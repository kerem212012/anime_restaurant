import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CASCADE, CharField
from django.utils import timezone
from user.models import CustomUser


class FoodCategory(models.Model):
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


class MerchCategory(models.Model):
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


class FoodIngredient(models.Model):
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


class Food(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Uuid"
    )
    name = models.CharField(
        'Name',
        max_length=50
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
        verbose_name="Anime"
    )
    category = models.ForeignKey(
        FoodCategory,
        verbose_name='Category',
        related_name='foods',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    picture = models.ImageField(
        verbose_name='Picture'
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        max_length=300,
    )
    food_ingredient = models.ForeignKey(
        FoodIngredient,
        related_name='ingredients',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Food Ingredient"
    )

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return self.name


class OrderElement(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order",
        related_name="orders"
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,verbose_name="Content Type")
    object_id = models.PositiveIntegerField()

    product = GenericForeignKey(
        'content_type', 'object_id',
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


class Payment(models.Model):
    class PaymentChoice(models.TextChoices):
        CASH = "C", "Cash"
        NONCASH = "N", "Noncash"

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order"
    )
    method = models.CharField(max_length=1, choices=PaymentChoice.choices, verbose_name="Payment Method", db_index=True,
                              default=PaymentChoice.CASH)
    is_paid = models.BooleanField(default=False,verbose_name="Is Paid")
    paid_at = models.DateTimeField(verbose_name="Paid at")


class Merch(models.Model):
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
    merch_category = models.ForeignKey(
        MerchCategory,
        on_delete=models.CASCADE,
        verbose_name="Merch Category"
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
        related_name="animes",
        verbose_name="Anime"
    )
    size = CharField(max_length=50, verbose_name="Size")

    def __str__(self):
        return self.name
