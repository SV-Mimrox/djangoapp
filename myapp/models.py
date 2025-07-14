from django.db import models
import mongoengine as me

class Product(me.Document):
    name = me.StringField(required=True)
    price = me.FloatField()
    description = me.StringField()
    in_stock = me.BooleanField(default=True)

    # This method is optional, but it helps for easy string representation
    def __str__(self):
        return f"{self.name} - ${self.price}"
