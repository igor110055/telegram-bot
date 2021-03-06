from django.db import models


# Create your models here.

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="User ID",
        unique=True,
    )
    name = models.TextField(
        verbose_name="User name"
    )

    def __str__(self):
        return f"#{self.external_id} {self.name}"

    class Meta:
        verbose_name = "Profile"


class Message(models.Model):
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name="Profile",
        on_delete=models.PROTECT,
    )
    btcPrice = models.TextField(
        verbose_name="BTC Price",
    )
    fiatPrice = models.TextField(
        verbose_name="Fiat Price",
    )
    status = models.TextField(
        verbose_name="Status",
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Receiving time",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Message"


class Type(models.Model):
    typeOfRequisites = models.TextField(
        verbose_name="Requisites Type",
    )
    number = models.TextField(
        verbose_name="Number",
    )
    def __str__(self):
        return f"#{self.typeOfRequisites} {self.number}"
    class Meta:
        verbose_name = "Type of Requisites"


class Requisites(models.Model):
    type = models.ForeignKey(
        to='ugc.Type',
        verbose_name="Requisites Type",
        on_delete=models.PROTECT,
        null=True
    )
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name="Profile",
        on_delete=models.PROTECT,
    )
    btcPrice = models.TextField(
        verbose_name="BTC Price",
    )
    btcPrice = models.TextField(
        verbose_name="BTC Price",
    )
    fiatPrice = models.TextField(
        verbose_name="Fiat Price",
    )
    created_at = models.DateTimeField(
        verbose_name="Receiving time",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Requisites"
