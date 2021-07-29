from rest_framework import serializers
from financeapp.serializers import CounterpartySerializers, ProductNameSerializers, AccountnumberSerializers
from . models import Sales, FuraCondition


class FuraConditionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = FuraCondition
        fields = '__all__'


class SalesSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    salesNumber = serializers.CharField(required=True)  # xarid nomer1
    data = serializers.CharField()  # olingan sana2
    country = CounterpartySerializers()  # kontragent3
    productname = ProductNameSerializers()  # Produkt name
    slaughteredCattle = serializers.FloatField()  # so'yilgan mol
    amount = serializers.FloatField()  # miqdori
    loss = serializers.FloatField()  # go'sht yo'qolishi
    price = serializers.FloatField(required=True)  # mahsulot narxi
    purchase = serializers.FloatField()  # soltib olinish
    nds = serializers.FloatField(default=0.0)  # NDS to'lovlari
    veterinar = serializers.FloatField(default=0.0)  # veterinar to'lovlari
    goStandart = serializers.FloatField(default=0.0)  # gostandart to'lovlari
    gigiena = serializers.FloatField(default=0.0)  # gigiena to'lovlari
    customer = serializers.FloatField(default=0.0)  # Bojxona to'lovlari
    deklarent = serializers.FloatField(default=0.0)  # deklarent to'lovlari
    # Yetkazib berishga to'lov, Dostavka
    delivery = serializers.FloatField(default=0.0)
    swift = serializers.FloatField(default=0.0)  # Swiftga to'lov
    ministryFinance = serializers.FloatField(default=0.0)  # Moliyaga yo'l
    certificate = serializers.FloatField(default=0.0)  # Sertifikat
    sPOT = serializers.FloatField(default=0.0)  # SPOT to'lov
    sES = serializers.FloatField(default=0.0)  # Sesga to'lov
    thatsall = serializers.FloatField()  # jami summasi
    accountnumber = AccountnumberSerializers()  # hisob raqam
    furaCondition = FuraConditionsSerializers()  # Fura holati
    finisheddate = serializers.CharField()  # tugagan sana
    willBePaid = serializers.FloatField(default=0.0)  # to'landi
    residue = serializers.FloatField()  # qoldiq
    buymonth = serializers.IntegerField()  # sotib olingan oy
    finishedmonth = serializers.IntegerField()  # tugagan oy
    comment = serializers.CharField(required=True)  # commentariya
    tanPrice = serializers.FloatField()  # tannarx thatsall/amount
    amounttotal = serializers.FloatField()
    amountpurchase = serializers.FloatField()
    totalthatsall = serializers.FloatField()
    def create(self, validated_data):
        finish = Sales.objects.all().order_by('-date')[:1]
        if not finish:
            pur = float(validated_data['amount']) * float(validated_data['price'])
            thatsal = float(pur)+float(validated_data['nds'])+float(validated_data['veterinar'])+float(validated_data['goStandart'])+float(validated_data['gigiena'])+float(
                validated_data['customer'])+float(validated_data['deklarent'])+float(validated_data['delivery'])+float(validated_data['swift'])
            residues = float(thatsal) - float(validated_data['willBePaid'])
            tanPrice1 = (float(thatsal)/float(validated_data['amount']))
            model = Sales(
                salesNumber=validated_data['salesNumber'],
                data=validated_data['data'],
                country_id=validated_data['country'],
                productname_id=validated_data['productname'],
                slaughteredCattle=validated_data['slaughteredCattle'],
                amount=validated_data['amount'],
                loss=validated_data['loss'],
                price=validated_data['price'],
                purchase=pur,
                nds=validated_data['nds'],
                veterinar=validated_data['veterinar'],
                goStandart=validated_data['goStandart'],
                gigiena=validated_data['gigiena'],
                customer=validated_data['customer'],
                deklarent=validated_data['deklarent'],
                delivery=validated_data['delivery'],
                swift=validated_data['swift'],
                ministryFinance=validated_data['ministryFinance'],
                thatsall=thatsal,
                accountnumber_id=validated_data['accountnumber'],
                furaCondition_id = validated_data['furaCondition'],
                finisheddate=validated_data['finisheddate'],
                willBePaid=validated_data['willBePaid'],
                residue=residues,
                buymonth=validated_data['buymonth'],
                finishedmonth=validated_data['finishedmonth'],
                comment=validated_data['comment'],
                tanPrice =tanPrice1,
                amounttotal = validated_data['amount'],
                amountpurchase = pur,
                totalthatsall = thatsal,
                )
            model.save()
        if finish:
            for i in finish:
                pur = float(validated_data['amount']) * float(validated_data['price'])
                thatsal = float(pur) + float(validated_data['nds']) + float(validated_data['veterinar']) + float(
                    validated_data['goStandart']) + float(validated_data['gigiena']) + float(
                    validated_data['customer']) + float(validated_data['deklarent']) + float(
                    validated_data['delivery']) + float(validated_data['swift'])
                residues = float(thatsal) - float(validated_data['willBePaid'])
                tanPrice1 = (float(thatsal) / float(validated_data['amount']))
                a = float(i.amounttotal) + float(validated_data['amount'])
                b = float(i.amountpurchase) + float(pur)
                c = float(i.totalthatsall) + float(thatsal)
                model = Sales(
                    salesNumber=validated_data['salesNumber'],
                    data=validated_data['data'],
                    country_id=validated_data['country'],
                    productname_id=validated_data['productname'],
                    slaughteredCattle=validated_data['slaughteredCattle'],
                    amount=validated_data['amount'],
                    loss=validated_data['loss'],
                    price=validated_data['price'],
                    purchase=pur,
                    nds=validated_data['nds'],
                    veterinar=validated_data['veterinar'],
                    goStandart=validated_data['goStandart'],
                    gigiena=validated_data['gigiena'],
                    customer=validated_data['customer'],
                    deklarent=validated_data['deklarent'],
                    delivery=validated_data['delivery'],
                    swift=validated_data['swift'],
                    ministryFinance=validated_data['ministryFinance'],
                    thatsall=thatsal,
                    accountnumber_id=validated_data['accountnumber'],
                    furaCondition_id = validated_data['furaCondition'],
                    finisheddate=validated_data['finisheddate'],
                    willBePaid=validated_data['willBePaid'],
                    residue=residues,
                    buymonth=validated_data['buymonth'],
                    finishedmonth=validated_data['finishedmonth'],
                    comment=validated_data['comment'],
                    tanPrice=tanPrice1,
                    amountpurchase=b,
                    amounttotal=a,
                    totalthatsall=c,
                )
                model.save()
