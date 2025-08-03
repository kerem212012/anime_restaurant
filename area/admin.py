from django.contrib import admin

from area.models import FoodCategory, MerchCategory, FoodIngredient, Anime, Order, Food, OrderElement, Event, Payment, \
    Merch, ProductCategory, ProductIngredient, Product

IMAGE_HEIGHT = 200
IMAGE_WIDTH = 200


class OrderElementsInlines(admin.TabularInline):
    model = OrderElement
    extra = 0


@admin.register(FoodCategory)
class AdminFoodCategory(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(MerchCategory)
class AdminMerchCategory(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(FoodIngredient)
class AdminFoodIngredient(admin.ModelAdmin):
    search_fields = ["name", ]

@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    search_fields = ["name", ]

@admin.register(ProductIngredient)
class AdminProductIngredient(admin.ModelAdmin):
    search_fields = ["name", ]

@admin.register(Anime)
class AdminAnime(admin.ModelAdmin):
    search_fields = ["name", ]
    raw_id_fields = ("user",)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    inlines = [
        OrderElementsInlines,
    ]
    search_fields = ["phonenumber", ]
    raw_id_fields = ("user",)


@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    search_fields = ["name", ]
    raw_id_fields = ("anime", "category", "food_ingredient",)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    search_fields = ["name", ]
    raw_id_fields = ("anime", "product_category", "product_ingredient",)


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    search_fields = ["name", ]


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    search_fields = ["method", "is_paid", "order"]
    raw_id_fields = ("order",)


@admin.register(Merch)
class AdminMerch(admin.ModelAdmin):
    search_fields = ["name", ]
    raw_id_fields = ("merch_category", "anime",)
