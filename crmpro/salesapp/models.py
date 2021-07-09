from django.db import models
from financeapp.models import Counterparty, ProductName, AccountNumber


class FuraCondition(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = 'Fura holati'
        verbose_name_plural = "Fura holati"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # vaqt Avtomatik qo'yiladi
    salesNumber = models.CharField(max_length=50, blank=True)  # xarid nomer
    data = models.CharField(max_length=100)  # olingan sana
    country = models.ForeignKey(Counterparty, on_delete=models.SET_NULL, null=True)  # kontragent
    productname = models.ForeignKey(ProductName, on_delete=models.SET_NULL, null=True)  # Produkt name
    slaughteredCattle = models.FloatField(null=True, blank=True)  # so'yilgan mol
    amount = models.FloatField(null=True, blank=True)  # miqdori
    loss = models.FloatField(null=True, blank=True)  # go'sht yo'qolishi
    price = models.FloatField(null=False, blank=False)  # mahsulot narxi
    purchase = models.FloatField()  # soltib olinish
    nds = models.PositiveBigIntegerField(null=False, blank=False, default=0.0)  # NDS to'lovlari
    veterinar = models.FloatField(null=False, blank=False, default=0.0)  # veterinar to'lovlari
    goStandart = models.FloatField(null=False, blank=False, default=0.0)  # gostandart to'lovlari
    gigiena = models.FloatField(null=False, blank=False, default=0.0)  # gigiena to'lovlari
    customer = models.FloatField(null=False, blank=False, default=0.0)  # Bojxona to'lovlari
    deklarent = models.FloatField(null=False, blank=False, default=0.0)  # deklarent to'lovlari
    delivery = models.FloatField(null=False, blank=False, default=0.0)  # Yetkazib berishga to'lov, Dostavka
    swift = models.FloatField(null=False, blank=False, default=0.0)  # Swiftga to'lov
    ministryFinance = models.FloatField(null=False, blank=False, default=0.0)  # Moliyaga yo'l
    certificate = models.FloatField(null=False, blank=False, default=0.0)
    sPOT = models.FloatField(null=False, blank=False, default=0.0)  # SPOT to'lov
    sES = models.FloatField(null=False, blank=False, default=0.0)  # Sesga to'lov
    thatsall = models.FloatField()  # jami summasi
    accountnumber = models.ForeignKey(AccountNumber, on_delete=models.SET_NULL, null=True)  # hisob raqam
    furaCondition = models.ForeignKey(FuraCondition, on_delete=models.SET_NULL, null=True)  # fura holati
    finisheddate = models.CharField(max_length=100)  # tugagan sana
    willBePaid = models.FloatField(null=False, blank=False, default=0.0)  # to'landi
    residue = models.FloatField()  # qoldiq
    buymonth = models.IntegerField()  # sotib olingan oy
    finishedmonth = models.IntegerField()  # tugagan oy
    comment = models.CharField(max_length=1028, null=False, blank=False)  # commentariya

    class Meta:
        verbose_name = "Sotuvlar"
        verbose_name_plural = "Sotuvlar jadvali"
