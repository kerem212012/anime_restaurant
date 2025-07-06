import uuid
from wsgiref.validate import bad_header_value_re

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CASCADE, CharField
from django.utils import timezone
from user.models import CustomUser


class FoodCategory(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    picture = models.ImageField(
        'картинка'
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name


class MerchCategory(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    picture = models.ImageField(
        'картинка'
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name


class FoodIngredient(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    picture = models.ImageField(
        'картинка'
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    picture = models.ImageField()
    user = models.ManyToManyField(
        CustomUser,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        MANAGER = "M", "Передан менеджеру"
        RESTAURANT = "R", "Передан ресторану"
        COURIER = "C", "Передан курьеру"
        PROCESSED = "P", "Обработанный"

    status = models.CharField(max_length=1, choices=StatusChoice.choices, verbose_name="Статус", db_index=True,
                              default=StatusChoice.MANAGER)
    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name="users"
    )
    address = models.TextField(verbose_name="Адрес доставки")
    comment = models.TextField(max_length=200, verbose_name="Комментарий", blank=True)
    registered_at = models.DateTimeField(verbose_name="Зарегистрирован в", default=timezone.now)
    called_at = models.DateTimeField(verbose_name="Позвонили в", db_index=True, blank=True, null=True)
    delivered_at = models.DateTimeField(verbose_name="Доставлен в", db_index=True, blank=True, null=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Food(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        'название',
        max_length=50
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
    )
    category = models.ForeignKey(
        FoodCategory,
        verbose_name='категория',
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
        'картинка'
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )
    food_ingredient = models.ForeignKey(
        FoodIngredient,
        related_name='ingredients',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name


class OrderElement(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Заказ",
        related_name="orders"
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    product = GenericForeignKey(
        'content_type', 'object_id'
    )
    price = models.DecimalField(verbose_name="цена заказа", max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)], default=0)
    quantity = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'


class Event(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )
    picture = models.ImageField(
        'картинка',
        default=None
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
    )
    data = models.DateTimeField()

    def __str__(self):
        return self.name


class Payment(models.Model):
    class PaymentChoice(models.TextChoices):
        CASH = "C", "Наличные"
        NONCASH = "N", "Безналичные"

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )
    method = models.CharField(max_length=1, choices=PaymentChoice.choices, verbose_name="Способ оплаты", db_index=True,
                              default=PaymentChoice.CASH)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField()


class Merch(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        'название',
        max_length=50
    )
    picture = models.ImageField(
        'картинка'
    )
    description = models.TextField(
        'описание',
        blank=True,
        max_length=300,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    merch_category = models.ForeignKey(
        MerchCategory,
        on_delete=models.CASCADE
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=CASCADE,
        related_name="animes"
    )
    size = CharField(max_length=50, )

    def __str__(self):
        return self.name
