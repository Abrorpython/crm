from rest_framework import serializers
from .models import (Months, Origin,
                     AccountNumber, Counterparty,
                     RawMaterial, Employees, ProductName, Table, Endvalue)


class ProductNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = '__all__'


class OriginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = '__all__'


class AccountnumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountNumber
        fields = '__all__'


class MonthSerializers(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = '__all__'


class CounterpartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'


class EmployesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class RawMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'


class TableSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.CharField(required=True)
    income = serializers.FloatField()      # kirim
    expense = serializers.FloatField()  # chiqim
    accountnumber = AccountnumberSerializers(required=True)  # xisob raqam
    counterparty = CounterpartySerializers(required=True)  # Kontragent
    origin = OriginSerializers(required=True)   # manba
    comment = serializers.CharField(required=True)  # commet
    employes = EmployesSerializers()  # Hodimlar
    monthone = MonthSerializers()  # oyni tanlaydi
    # monthtwo = MonthSerializers()
    cashmoney = serializers.FloatField()  # naqd pul kassasi
    plasticmoney = serializers.FloatField()  # plastik pul kassasi
    accountnumbermoney = serializers.FloatField()  # xisob raqam pul kassasi
    dollar = serializers.FloatField()  # dollar pul kassasi JSON

    def create(self, validated_data):
        a = Table.objects.all().order_by('-autodate')[:1]
        if validated_data['income']:
            if validated_data['accountnumber'] == 1:
                if validated_data['expense'] == 0:
                    if not a:
                        income = validated_data['income']
                        model = Table(
                            date=validated_data['date'],
                            income=validated_data['income'],
                            expense=0,
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            cashmoney=income,
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float(
                                validated_data['income'])+float(i.cashmoney)
                            plastic = i.plasticmoney
                            accounnumberm = i.accountnumbermoney
                            dollar1 = i.dollar
                            model = Table(
                                date=validated_data['date'],
                                income=validated_data['income'],
                                expense=0,
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cash,
                                plasticmoney=plastic,
                                accountnumbermoney=accounnumberm,
                                dollar=dollar1
                            )
                        model.save()
            elif validated_data['accountnumber'] == 2:
                if validated_data['expense'] == 0:
                    if not a:
                        income = validated_data['income']
                        model = Table(
                            date=validated_data['date'],
                            income=validated_data['income'],
                            expense=0,
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            plasticmoney=income
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float(
                                validated_data['income'])+float(i.plasticmoney)
                            cashmoney = i.cashmoney
                            accounnumberm = i.accountnumbermoney
                            dollar2 = i.dollar
                            model = Table(
                                date=validated_data['date'],
                                income=validated_data['income'],
                                expense=0,
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmoney,
                                plasticmoney=cash,
                                accountnumbermoney=accounnumberm,
                                dollar=dollar2
                            )
                            model.save()
            elif validated_data['accountnumber'] == 3:
                if validated_data['expense'] == 0:
                    if not a:
                        income = validated_data['income']
                        model = Table(
                            date=validated_data['date'],
                            income=validated_data['income'],
                            expense=0,
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            accountnumbermoney=income
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float(
                                validated_data['income'])+float(i.accountnumbermoney)
                            plastic = i.plasticmoney
                            cashmon = i.cashmoney
                            dollar3 = i.dollar
                            model = Table(
                                date=validated_data['date'],
                                income=validated_data['income'],
                                expense=0,
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmon,
                                plasticmoney=plastic,
                                accountnumbermoney=cash,
                                dollar=dollar3
                            )
                            model.save()
            elif validated_data['accountnumber'] == 4:
                if validated_data['expense'] == 0:
                    if not a:
                        income = validated_data['income']
                        model = Table(
                            date=validated_data['date'],
                            income=validated_data['income'],
                            expense=0,
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            dollar=income
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float(
                                validated_data['income'])+float(i.dollar)
                            plastic = i.plasticmoney
                            cashmon = i.cashmoney
                            accountnumber = i.accountnumbermoney
                            model = Table(
                                date=validated_data['date'],
                                income=validated_data['income'],
                                expense=0,
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmon,
                                plasticmoney=plastic,
                                accountnumbermoney=accountnumber,
                                dollar=cash
                            )
                            model.save()

        elif validated_data['expense']:
            if validated_data['accountnumber'] == 1:
                if validated_data['income'] == 0:
                    if not a:
                        income = (-float(validated_data['expense']))
                        model = Table(
                            date=validated_data['date'],
                            income=0,
                            expense=validated_data['expense'],
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            cashmoney=income,
                        )
                        model.save()
                    elif a:
                        for i in a:
                            income = float(i.cashmoney) - \
                                float(validated_data['expense'])
                            plastic = i.plasticmoney
                            accountmoney = i.accountnumbermoney
                            model = Table(
                                date=validated_data['date'],
                                income=0,
                                expense=validated_data['expense'],
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=income,
                                plasticmoney=plastic,
                                accountnumbermoney=accountmoney
                            )
                            model.save()
            elif validated_data['accountnumber'] == 2:
                if validated_data['income'] == 0:
                    if not a:
                        income = -(float(validated_data['expense']))
                        model = Table(
                            date=validated_data['date'],
                            income=0,
                            expense=validated_data['expense'],
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            plasticmoney=income
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float((i.plasticmoney)) - \
                                float(validated_data['expense'])
                            cashmoney = i.cashmoney
                            accounnumberm = i.accountnumbermoney
                            model = Table(
                                date=validated_data['date'],
                                income=0,
                                expense=validated_data['expense'],
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmoney,
                                plasticmoney=cash,
                                accountnumbermoney=accounnumberm
                            )
                            model.save()
            elif validated_data['accountnumber'] == 3:
                if validated_data['income'] == 0:
                    if not a:
                        income = -(float(validated_data['expense']))
                        model = Table(
                            date=validated_data['date'],
                            income=0,
                            expense=validated_data['expense'],
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            accountnumbermoney=income
                        )
                        model.save()
                    elif a:
                        for i in a:
                            cash = float(i.accountnumbermoney) - \
                                float(validated_data['expense'])
                            plastic = i.plasticmoney
                            cashmon = i.cashmoney
                            model = Table(
                                date=validated_data['date'],
                                income=0,
                                expense=validated_data['expense'],
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmon,
                                plasticmoney=plastic,
                                accountnumbermoney=cash
                            )
                            model.save()
            elif validated_data['accountnumber'] == 4:
                if validated_data['income'] == 0:
                    if not a:
                        income = -(float(validated_data['expense']))
                        model = Table(
                            date=validated_data['date'],
                            income=0,
                            expense=validated_data['expense'],
                            accountnumber_id=validated_data['accountnumber'],
                            counterparty_id=validated_data['counterparty'],
                            origin_id=validated_data['origin'],
                            comment=validated_data['comment'],
                            employes_id=validated_data['employes'],
                            monthone_id=validated_data['monthone'],
                            dollar=income,
                        )
                        model.save()
                    elif a:
                        for i in a:
                            incom = float(i.dollar) - \
                                float(validated_data['expense'])
                            cashmon = i.cashmoney
                            plastic = i.plasticmoney
                            accountmoney = i.accountnumbermoney
                            model = Table(
                                date=validated_data['date'],
                                income=0,
                                expense=validated_data['expense'],
                                accountnumber_id=validated_data['accountnumber'],
                                counterparty_id=validated_data['counterparty'],
                                origin_id=validated_data['origin'],
                                comment=validated_data['comment'],
                                employes_id=validated_data['employes'],
                                monthone_id=validated_data['monthone'],
                                cashmoney=cashmon,
                                plasticmoney=plastic,
                                accountnumbermoney=accountmoney,
                                dollar=incom
                            )
                            model.save()


class EndValuesSerialziers(serializers.Serializer):
    cashmoneys = serializers.FloatField(default=0)
    plasticmoneys = serializers.FloatField(default=0)
    accountnumbermoneys = serializers.FloatField(default=0)
    dollars = serializers.FloatField(default=0)

    def create(self, validate_data):
        a = Table.objects.all().order_by('-autodate')[:1]
        for i in a:
            deng = float(i.cashmoney)-float(validate_data['cashmoneys'])
            deng2 = float(i.plasticmoney) - float(validate_data['plasticmoneys'])
            deng3 = float(i.accountnumbermoney) - float(validate_data['accountnumbermoneys'])
            deng4 = float(i.dollar)-float(validate_data['dollars'])
            model = Endvalue(
                cashmoneys=deng,
                plasticmoneys=deng2,
                accountnumbermoneys=deng3,
                dollars=deng4
            )
            model.save()
