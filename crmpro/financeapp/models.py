from django.db import models

class Origin(models.Model):  # 1.Manbalar
    name = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        verbose_name = 'Mavjud manbalar'
        verbose_name_plural = "Manbalar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class AccountNumber(models.Model):  # 2.Hisob raqam
    name = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        verbose_name = 'Hisob raqam'
        verbose_name_plural = "Hisob raqamlar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Accruals(models.Model):  # 3.Hisob-kitoblar
    name = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        verbose_name = 'Hisob kitoblar'
        verbose_name_plural = "Hisob kitoblar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Months(models.Model):  # 4.Yil oylari
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Oy'
        verbose_name_plural = "oylar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Counterparty(models.Model):  # 5.Kontragent
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Kontargent'
        verbose_name_plural = "Mavjud kontragentlar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Employees(models.Model):  # 6.Hodimlar
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Hodimlar'
        verbose_name_plural = "Mavjud Hodimlar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class RawMaterial(models.Model):  # 7.Xom - ashyolar
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Xom-ashyolar'
        verbose_name_plural = "Xom-ashyolar"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class ProductName(models.Model):  # 8.Mahsulot nomi
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Mahsulotlar'
        verbose_name_plural = "Mahsulot nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class NameGoods(models.Model):  # 9.Tovarlar nomi
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Tovarlar'
        verbose_name_plural = "Tovar nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Chanells(models.Model):  # 10.Kanallar
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Kanallar'
        verbose_name_plural = "Kanal nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Order(models.Model):  # 11.Zakaslar
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Zakaslar'
        verbose_name_plural = "Zakas nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Planning(models.Model):  # 12. Rejalashtirish
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Rejalashtirish'
        verbose_name_plural = "Rejalashtirish nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Addresses(models.Model):  # 13. Manzillar
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Manzillar'
        verbose_name_plural = "Manzillar nomi"

    def __str__(self):
        return f"{self.id}  - {self.name}"


class TheNext(models.Model):  # 14. Keyingi qadamlar
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Probability(models.Model):  # 15. Extimolligi
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Price(models.Model):  # 16. Narx
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Gender(models.Model):  # 17. Jinsi()
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Position(models.Model):  # 18. Lavozimi
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Referrance(models.Model):  # 19. Ma'lumot
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Sections(models.Model):  # 20. Bo'limlar
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id}  - {self.name}"


class Birdhouse(models.Model):  # 21. Qushxona
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class PaymentType(models.Model):  # 22. To'lov turi
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Branches(models.Model):  # 23. Filiallar
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Construction(models.Model):  # 24. Qurilish
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


# Jadval uchun

class Table(models.Model):
    autodate = models.DateTimeField(auto_now_add=True)  # autovaqt
    date = models.CharField(max_length=255, null=True)  # vaqt
    income = models.FloatField(blank=True, null=True)  # kirim
    expense = models.FloatField(blank=True, null=True)  # chiqim
    accountnumber = models.ForeignKey(AccountNumber, on_delete=models.SET_NULL, blank=True, null=True)  # xisob raqam
    counterparty = models.ForeignKey(Counterparty, on_delete=models.SET_NULL, blank=True, null=True)  # Kontragent
    origin = models.ForeignKey(Origin, on_delete=models.SET_NULL, blank=True, null=True)  # manba
    comment = models.TextField()  # commet
    employes = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, blank=True)  # Hodimlar
    monthone = models.ForeignKey(Months, on_delete=models.SET_NULL, null=True, blank=True)  # oyni tanlaydi
    # monthtwo = models.IntegerField(null=True,blank=True)
    cashmoney = models.FloatField(null=True, blank=True, default=0)  # naqd pul kassasi
    plasticmoney = models.FloatField(null=True, blank=True, default=0)  # plastik pul kassasi
    accountnumbermoney = models.FloatField(null=True, blank=True, default=0)  # xisob raqam pul kassasi
    dollar = models.FloatField(null=True, blank=True, default=0)  # dollar kassasi

    def __str__(self):
        return f"{self.id} - {self.accountnumber}"


class Endvalue(models.Model):
    autodate = models.DateTimeField(auto_now_add=True)
    cashmoneys = models.FloatField(null=True, blank=True, default=0)  # naqd pul kassasi
    plasticmoneys = models.FloatField(null=True, blank=True, default=0)  # plastik pul kassasi
    accountnumbermoneys = models.FloatField(null=True, blank=True, default=0)  # xisob raqam pul kassasi
    dollars = models.FloatField(null=True, blank=True, default=0)  # dollar kassasi

    def __str__(self):
        return int(self.id)














