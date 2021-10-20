from django.db.models import CharField,  Model
from .users import Users


class Products(Model):
    name = CharField(verbose_name="Name Product", default="", max_length=100, blank=False)
    price = CharField(verbose_name="Price", default="", max_length=100, blank=False)
    description = CharField(verbose_name="description", default="", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Price"
