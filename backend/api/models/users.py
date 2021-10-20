from django.db.models import CharField, DateTimeField , EmailField, Model
from django.utils.timezone import now

class Users(Model):
    username = CharField(verbose_name="Username", default="", max_length=100, blank=False)
    passworld = CharField(verbose_name="Passworld", default="", max_length=100, blank=False)
    email = EmailField(verbose_name="Email", default="", max_length=100, blank=False)
    first_name = CharField(verbose_name=, default="", max_length=100)
    create_at = DateTimeField(verbose_name="Registration data", default=now)



    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

