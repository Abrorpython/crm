from django.db import models
from financeapp.models import Counterparty,AccountNumber,ProductName

class Shopping(models.Model):
    furaName = models.CharField(max_length=255) # fura nomi
    sana = models.CharField(max_length=255) # sana
    countr = models.ForeignKey(Counterparty,on_delete=models.SET_NULL,null=True) # Kontrganet
    telnumber = models.CharField(max_length=255,default=None) # Telefon raqam
    paymentType = models.ForeignKey(AccountNumber,on_delete=models.SET_NULL,null=True) # To'lov turi
    paymentLifeTime = models.CharField(max_length=255) # To'lov muddat
    commodityType = models.ForeignKey(ProductName,on_delete=models.SET_NULL,null=True) # Product nomi
    miqdori = models.FloatField() # Mahsulot miqdori
    sotishNarxi = models.FloatField() # sotish narxi
    jami = models.FloatField() # Jami miqdori = Mahsulot miqdori + sotish narxi
    olishNarxi = models.FloatField() # Sotib olinish narxi
    paymentDate = models.CharField(max_length=255) # to'lov vaqti
    paymentFinish = models.FloatField(default=0) # Pul kelib tushdi yoki tushmadi
    qoldiq = models.FloatField() # qolgan qoldiq
    month = models.CharField(max_length=10) # Oy
    yalpiFoyda = models.FloatField() # Yalpi foyda
    retroBonusApi = models.BooleanField(default=False)
    retroBonus = models.FloatField() # Retro Bonus
    operatFoyda = models.FloatField() # Operativ foyda
    pulYechish = models.FloatField() # Pulyechib olish
    sofFoyda = models.FloatField() # Pul yechib olish
    oneFoyda = models.FloatField() # 1 kg dan qilingan foyda
    oneOperatFoyda = models.FloatField() # 1 kg dan sof foyda
    ichkiNds = models.FloatField() # ichki indeks
    expense = models.FloatField() # Chiqimlar kiritilishi shart
    foydaSoligi = models.FloatField() # sof foyda solig'i
    finishFoyda = models.FloatField() # oxirgi foyda
    week = models.IntegerField() # hafta
    shoppingTotal = models.FloatField() # Harid summasi
    AmountTotal = models.FloatField() # Xarid miqdori Jami
    TotalPrice = models.FloatField() # Jami harid
    ShoppingTotal = models.FloatField() # Jami harid miqdori
    date = models.DateTimeField(auto_now_add=True) # avtomatik vaqtni qo'yib ketadi