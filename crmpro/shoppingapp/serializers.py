from rest_framework import serializers
from financeapp.serializers import CounterpartySerializers, AccountnumberSerializers, ProductNameSerializers
from .models import Shopping


class ShoppingSerializers(serializers.Serializer):
    furaName = serializers.CharField(required=True)  # fura nomi
    sana = serializers.CharField(required=True)  # sana
    countr = CounterpartySerializers(required=True)  # Kontrganet
    telnumber = serializers.CharField(required=True)  # Telefon raqam
    paymentType = AccountnumberSerializers(required=True)  # To'lov turi
    paymentLifeTime = serializers.CharField(required=True)  # To'lov muddat
    commodityType = ProductNameSerializers(required=True)  # Product nomi
    miqdori = serializers.FloatField()  # Mahsulot miqdori
    sotishNarxi = serializers.FloatField()  # sotish narxi
    jami = serializers.FloatField()  # Jami miqdori = Mahsulot miqdori * sotish narxi
    olishNarxi = serializers.FloatField()  # Sotib olinish narxi
    paymentDate = serializers.CharField(required=True)  # to'lov vaqti
    paymentFinish = serializers.FloatField(default=0)  # Pul kelib tushdi yoki tushmadi
    qoldiq = serializers.FloatField()  # qolgan qoldiq
    month = serializers.CharField(required=True)  # Oy
    yalpiFoyda = serializers.FloatField()  # Yalpi foyda
    retroBonusApi = serializers.BooleanField(default=False)
    retroBonus = serializers.FloatField()  # Retro Bonus
    operatFoyda = serializers.FloatField()  # Operativ foyda
    pulYechish = serializers.FloatField()  # Pul yechib olish
    sofFoyda = serializers.FloatField()  # Sof foyda
    oneFoyda = serializers.FloatField()  # 1 kg dan qilingan foyda
    oneOperatFoyda = serializers.FloatField()  # 1 kg dan sof foyda
    ichkiNds = serializers.FloatField()  # ichki indeks
    expense = serializers.FloatField()  # Chiqimlar kiritilishi shart
    foydaSoligi = serializers.FloatField()  # sof foyda solig'i
    finishFoyda = serializers.FloatField()  # oxirgi foyda
    week = serializers.IntegerField()  # hafta
    shoppingTotal = serializers.FloatField()  # Harid summasi
    AmountTotal = serializers.FloatField()  # Xarid miqdori Jami
    TotalPrice = serializers.FloatField()  # Jami harid
    ShoppingTotal = serializers.FloatField()  # Jami harid miqdori

    def create(self, validated_data):
        finish = Shopping.objects.all().order_by('-date')[:1]
        if not finish:
            miqdor1 = validated_data['miqdori']
            jami1 = float(miqdor1) * float(validated_data['sotishNarxi'])
            qoldiq1 = jami1
            yalpiFoyda1 = float(jami1) - (float(validated_data['olishNarxi']) * float(miqdor1))
            if validated_data['retroBonusApi'] == "True":
                retroBonus1 = (float(yalpiFoyda1) * 3) / 100
                operatFoyda1 = float(yalpiFoyda1) - float(retroBonus1)
                if validated_data['paymentType'] == 3:
                    pulYechish1 = (float(yalpiFoyda1) * 5.5) / 100
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = (float(yalpiFoyda1) * 15) / 100
                    foydaSoligi1 = ((float(yalpiFoyda1) - validated_data['expense']) * 15) / 100
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    model = Shopping(
                        furaName=validated_data['furaName'],
                        sana=validated_data['sana'],
                        countr_id=validated_data['countr'],
                        telnumber=validated_data['telnumber'],
                        paymentType_id=validated_data['paymentType'],
                        paymentLifeTime=validated_data['paymentLifeTime'],
                        commodityType_id=validated_data['commodityType'],
                        miqdori=miqdor1,
                        sotishNarxi=validated_data['sotishNarxi'],
                        jami=jami1,
                        olishNarxi=validated_data['olishNarxi'],
                        paymentDate=validated_data['paymentDate'],
                        paymentFinish=validated_data['paymentFinish'],
                        qoldiq=qoldiq1,
                        month=validated_data['month'],
                        yalpiFoyda=yalpiFoyda1,
                        retroBonusApi=True,
                        retroBonus=retroBonus1,
                        operatFoyda=operatFoyda1,
                        pulYechish=pulYechish1,
                        sofFoyda=sofFoyda1,
                        oneFoyda=oneFoyda1,
                        oneOperatFoyda=oneSofFoyda1,
                        ichkiNds=ichkiNds1,
                        expense=validated_data['expense'],
                        foydaSoligi=foydaSoligi1,
                        finishFoyda=finishFoyda1,
                        week=validated_data['week'],
                        shoppingTotal=shoppingTotal1,
                        AmountTotal=miqdor1,
                        TotalPrice=jami1,
                        ShoppingTotal=shoppingTotal1,
                    )
                    model.save()
                else:
                    pulYechish1 = 0
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = 0
                    foydaSoligi1 = 0
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    model = Shopping(
                        furaName=validated_data['furaName'],
                        sana=validated_data['sana'],
                        countr_id=validated_data['countr'],
                        telnumber=validated_data['telnumber'],
                        paymentType_id=validated_data['paymentType'],
                        paymentLifeTime=validated_data['paymentLifeTime'],
                        commodityType_id=validated_data['commodityType'],
                        miqdori=miqdor1,
                        sotishNarxi=validated_data['sotishNarxi'],
                        jami=jami1,
                        olishNarxi=validated_data['olishNarxi'],
                        paymentDate=validated_data['paymentDate'],
                        paymentFinish=validated_data['paymentFinish'],
                        qoldiq=qoldiq1,
                        month=validated_data['month'],
                        yalpiFoyda=yalpiFoyda1,
                        retroBonusApi=True,
                        retroBonus=retroBonus1,
                        operatFoyda=operatFoyda1,
                        pulYechish=pulYechish1,
                        sofFoyda=sofFoyda1,
                        oneFoyda=oneFoyda1,
                        oneOperatFoyda=oneSofFoyda1,
                        ichkiNds=ichkiNds1,
                        expense=validated_data['expense'],
                        foydaSoligi=foydaSoligi1,
                        finishFoyda=finishFoyda1,
                        week=validated_data['week'],
                        shoppingTotal=shoppingTotal1,
                        AmountTotal=miqdor1,
                        TotalPrice=jami1,
                        ShoppingTotal=shoppingTotal1,
                    )
                    model.save()

            if validated_data['retroBonusApi'] == "False":
                retroBonus1 = 0
                operatFoyda1 = float(yalpiFoyda1) - float(retroBonus1)
                if validated_data['paymentType'] == 3:
                    pulYechish1 = (float(yalpiFoyda1) * 5.5) / 100
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = (float(yalpiFoyda1) * 15) / 100
                    foydaSoligi1 = ((float(yalpiFoyda1) - validated_data['expense']) * 15) / 100
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    model = Shopping(
                        furaName=validated_data['furaName'],
                        sana=validated_data['sana'],
                        countr_id=validated_data['countr'],
                        telnumber=validated_data['telnumber'],
                        paymentType_id=validated_data['paymentType'],
                        paymentLifeTime=validated_data['paymentLifeTime'],
                        commodityType_id=validated_data['commodityType'],
                        miqdori=miqdor1,
                        sotishNarxi=validated_data['sotishNarxi'],
                        jami=jami1,
                        olishNarxi=validated_data['olishNarxi'],
                        paymentDate=validated_data['paymentDate'],
                        paymentFinish=validated_data['paymentFinish'],
                        qoldiq=qoldiq1,
                        month=validated_data['month'],
                        yalpiFoyda=yalpiFoyda1,
                        retroBonusApi=True,
                        retroBonus=0,
                        operatFoyda=operatFoyda1,
                        pulYechish=pulYechish1,
                        sofFoyda=sofFoyda1,
                        oneFoyda=oneFoyda1,
                        oneOperatFoyda=oneSofFoyda1,
                        ichkiNds=ichkiNds1,
                        expense=validated_data['expense'],
                        foydaSoligi=foydaSoligi1,
                        finishFoyda=finishFoyda1,
                        week=validated_data['week'],
                        shoppingTotal=shoppingTotal1,
                        AmountTotal=miqdor1,
                        TotalPrice=jami1,
                        ShoppingTotal=shoppingTotal1,
                    )
                    model.save()
                else:
                    pulYechish1 = 0
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = 0
                    foydaSoligi1 = 0
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    model = Shopping(
                        furaName=validated_data['furaName'],
                        sana=validated_data['sana'],
                        countr_id=validated_data['countr'],
                        telnumber=validated_data['telnumber'],
                        paymentType_id=validated_data['paymentType'],
                        paymentLifeTime=validated_data['paymentLifeTime'],
                        commodityType_id=validated_data['commodityType'],
                        miqdori=miqdor1,
                        sotishNarxi=validated_data['sotishNarxi'],
                        jami=jami1,
                        olishNarxi=validated_data['olishNarxi'],
                        paymentDate=validated_data['paymentDate'],
                        paymentFinish=validated_data['paymentFinish'],
                        qoldiq=qoldiq1,
                        month=validated_data['month'],
                        yalpiFoyda=yalpiFoyda1,
                        retroBonusApi=True,
                        retroBonus=retroBonus1,
                        operatFoyda=operatFoyda1,
                        pulYechish=pulYechish1,
                        sofFoyda=sofFoyda1,
                        oneFoyda=oneFoyda1,
                        oneOperatFoyda=oneSofFoyda1,
                        ichkiNds=ichkiNds1,
                        expense=validated_data['expense'],
                        foydaSoligi=foydaSoligi1,
                        finishFoyda=finishFoyda1,
                        week=validated_data['week'],
                        shoppingTotal=shoppingTotal1,
                        AmountTotal=miqdor1,
                        TotalPrice=jami1,
                        ShoppingTotal=shoppingTotal1,
                    )
                    model.save()
        if finish:
            miqdor1 = validated_data['miqdori']
            jami1 = float(miqdor1) * float(validated_data['sotishNarxi'])
            qoldiq1 = jami1
            yalpiFoyda1 = float(jami1) - (float(validated_data['olishNarxi']) * float(miqdor1))
            if validated_data['retroBonusApi'] == "True":
                retroBonus1 = (float(yalpiFoyda1) * 3) / 100
                operatFoyda1 = float(yalpiFoyda1) - float(retroBonus1)
                if validated_data['paymentType'] == 3:
                    pulYechish1 = (float(yalpiFoyda1) * 5.5) / 100
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = (float(yalpiFoyda1) * 15) / 100
                    foydaSoligi1 = ((float(yalpiFoyda1) - validated_data['expense']) * 15) / 100
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    for i in finish:
                        a = float(i.AmountTotal) + float(miqdor1)
                        b = float(i.TotalPrice) + float(jami1)
                        c = float(i.ShoppingTotal) + float(shoppingTotal1)
                        model = Shopping(
                            furaName=validated_data['furaName'],
                            sana=validated_data['sana'],
                            countr_id=validated_data['countr'],
                            telnumber=validated_data['telnumber'],
                            paymentType_id=validated_data['paymentType'],
                            paymentLifeTime=validated_data['paymentLifeTime'],
                            commodityType_id=validated_data['commodityType'],
                            miqdori=miqdor1,
                            sotishNarxi=validated_data['sotishNarxi'],
                            jami=jami1,
                            olishNarxi=validated_data['olishNarxi'],
                            paymentDate=validated_data['paymentDate'],
                            paymentFinish=validated_data['paymentFinish'],
                            qoldiq=qoldiq1,
                            month=validated_data['month'],
                            yalpiFoyda=yalpiFoyda1,
                            retroBonusApi=True,
                            retroBonus=retroBonus1,
                            operatFoyda=operatFoyda1,
                            pulYechish=pulYechish1,
                            sofFoyda=sofFoyda1,
                            oneFoyda=oneFoyda1,
                            oneOperatFoyda=oneSofFoyda1,
                            ichkiNds=ichkiNds1,
                            expense=validated_data['expense'],
                            foydaSoligi=foydaSoligi1,
                            finishFoyda=finishFoyda1,
                            week=validated_data['week'],
                            shoppingTotal=shoppingTotal1,
                            AmountTotal=a,
                            TotalPrice=b,
                            ShoppingTotal=c,
                        )
                        model.save()
                else:
                    pulYechish1 = 0
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = 0
                    foydaSoligi1 = 0
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    for i in finish:
                        a = float(i.AmountTotal) + float(miqdor1)
                        b = float(i.TotalPrice) + float(jami1)
                        c = float(i.ShoppingTotal) + float(shoppingTotal1)
                        model = Shopping(
                            furaName=validated_data['furaName'],
                            sana=validated_data['sana'],
                            countr_id=validated_data['countr'],
                            telnumber=validated_data['telnumber'],
                            paymentType_id=validated_data['paymentType'],
                            paymentLifeTime=validated_data['paymentLifeTime'],
                            commodityType_id=validated_data['commodityType'],
                            miqdori=miqdor1,
                            sotishNarxi=validated_data['sotishNarxi'],
                            jami=jami1,
                            olishNarxi=validated_data['olishNarxi'],
                            paymentDate=validated_data['paymentDate'],
                            paymentFinish=validated_data['paymentFinish'],
                            qoldiq=qoldiq1,
                            month=validated_data['month'],
                            yalpiFoyda=yalpiFoyda1,
                            retroBonusApi=True,
                            retroBonus=retroBonus1,
                            operatFoyda=operatFoyda1,
                            pulYechish=pulYechish1,
                            sofFoyda=sofFoyda1,
                            oneFoyda=oneFoyda1,
                            oneOperatFoyda=oneSofFoyda1,
                            ichkiNds=ichkiNds1,
                            expense=validated_data['expense'],
                            foydaSoligi=foydaSoligi1,
                            finishFoyda=finishFoyda1,
                            week=validated_data['week'],
                            shoppingTotal=shoppingTotal1,
                            AmountTotal=a,
                            TotalPrice=b,
                            ShoppingTotal=c,
                        )
                        model.save()

            if validated_data['retroBonusApi'] == "False":
                retroBonus1 = 0
                operatFoyda1 = float(yalpiFoyda1) - float(retroBonus1)
                if validated_data['paymentType'] == 3:
                    pulYechish1 = (float(yalpiFoyda1) * 5.5) / 100
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = (float(yalpiFoyda1) * 15) / 100
                    foydaSoligi1 = ((float(yalpiFoyda1) - validated_data['expense']) * 15) / 100
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    for i in finish:
                        a = float(i.AmountTotal) + float(miqdor1)
                        b = float(i.TotalPrice) + float(jami1)
                        c = float(i.ShoppingTotal) + float(shoppingTotal1)
                        model = Shopping(
                            furaName=validated_data['furaName'],
                            sana=validated_data['sana'],
                            countr_id=validated_data['countr'],
                            telnumber=validated_data['telnumber'],
                            paymentType_id=validated_data['paymentType'],
                            paymentLifeTime=validated_data['paymentLifeTime'],
                            commodityType_id=validated_data['commodityType'],
                            miqdori=miqdor1,
                            sotishNarxi=validated_data['sotishNarxi'],
                            jami=jami1,
                            olishNarxi=validated_data['olishNarxi'],
                            paymentDate=validated_data['paymentDate'],
                            paymentFinish=validated_data['paymentFinish'],
                            qoldiq=qoldiq1,
                            month=validated_data['month'],
                            yalpiFoyda=yalpiFoyda1,
                            retroBonusApi=True,
                            retroBonus=0,
                            operatFoyda=operatFoyda1,
                            pulYechish=pulYechish1,
                            sofFoyda=sofFoyda1,
                            oneFoyda=oneFoyda1,
                            oneOperatFoyda=oneSofFoyda1,
                            ichkiNds=ichkiNds1,
                            expense=validated_data['expense'],
                            foydaSoligi=foydaSoligi1,
                            finishFoyda=finishFoyda1,
                            week=validated_data['week'],
                            shoppingTotal=shoppingTotal1,
                            AmountTotal=a,
                            TotalPrice=b,
                            ShoppingTotal=c,
                        )
                        model.save()
                else:
                    pulYechish1 = 0
                    sofFoyda1 = float(operatFoyda1) - float(pulYechish1)
                    oneFoyda1 = float(yalpiFoyda1) / float(miqdor1)
                    oneSofFoyda1 = float(sofFoyda1) / float(miqdor1)
                    ichkiNds1 = 0
                    foydaSoligi1 = 0
                    finishFoyda1 = float(oneFoyda1) - float(ichkiNds1) - float(foydaSoligi1)
                    shoppingTotal1 = float(miqdor1) * float(validated_data['olishNarxi'])
                    for i in finish:
                        a = float(i.AmountTotal) + float(miqdor1)
                        b = float(i.TotalPrice) + float(jami1)
                        c = float(i.ShoppingTotal) + float(shoppingTotal1)
                        model = Shopping(
                            furaName=validated_data['furaName'],
                            sana=validated_data['sana'],
                            countr_id=validated_data['countr'],
                            telnumber=validated_data['telnumber'],
                            paymentType_id=validated_data['paymentType'],
                            paymentLifeTime=validated_data['paymentLifeTime'],
                            commodityType_id=validated_data['commodityType'],
                            miqdori=miqdor1,
                            sotishNarxi=validated_data['sotishNarxi'],
                            jami=jami1,
                            olishNarxi=validated_data['olishNarxi'],
                            paymentDate=validated_data['paymentDate'],
                            paymentFinish=validated_data['paymentFinish'],
                            qoldiq=qoldiq1,
                            month=validated_data['month'],
                            yalpiFoyda=yalpiFoyda1,
                            retroBonusApi=True,
                            retroBonus=retroBonus1,
                            operatFoyda=operatFoyda1,
                            pulYechish=pulYechish1,
                            sofFoyda=sofFoyda1,
                            oneFoyda=oneFoyda1,
                            oneOperatFoyda=oneSofFoyda1,
                            ichkiNds=ichkiNds1,
                            expense=validated_data['expense'],
                            foydaSoligi=foydaSoligi1,
                            finishFoyda=finishFoyda1,
                            week=validated_data['week'],
                            shoppingTotal=shoppingTotal1,
                            AmountTotal=a,
                            TotalPrice=b,
                            ShoppingTotal=c,
                        )
                        model.save()
