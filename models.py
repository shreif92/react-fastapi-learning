from pypika_tortoise import NULL
from tortoise.models import Model
from tortoise import fields


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)  # Fixed NULL to null
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    stock = fields.IntField()
    reveneue = fields.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    supplyed_by = fields.ForeignKeyField(
        "models.Supplier", related_name="products", on_delete=fields.CASCADE)

    class Meta:
        table = "products"


class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    phone_number = fields.CharField(max_length=20)
    address = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "suppliers"

    def __str__(self):
        return self.name
