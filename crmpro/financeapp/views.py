from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import (Employees, Origin, AccountNumber,
                     Months, Counterparty, RawMaterial, ProductName, Table)

from .serializers import (EmployesSerializers, EndValuesSerialziers,
                          OriginSerializers, AccountnumberSerializers,
                          MonthSerializers, CounterpartySerializers,
                          RawMaterialSerializers, ProductNameSerializers,
                          TableSerializers, Endvalue)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def endvalue(request):
    if request.method == 'GET':
        endvalues = Endvalue.objects.all().order_by('-autodate')[:1]
        serializers = EndValuesSerialziers(endvalues, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = EndValuesSerialziers(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def table_list(request):
    if request.method == 'GET':
        table = Table.objects.all()
        serializers = TableSerializers(table, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = TableSerializers(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response({'ok': "qoshildi"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def table_detail(request, pk):
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = TableSerializers(table)
        return Response(serilazer.data)
    # elif request.method == 'PUT':
    #     serializer = TableSerializers(table,data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # class TableView(APIView):


#     def get(self,request):
#         table = Table.objects.all()
#         serializers = TableSerializers(table,many=True)
#         return Response(serializers.data)

#     def post(self,request,*args, **kwargs):
#         serializer = TableSerializers(data=request.data)
#         serializer.is_valid(raise_exception=False)
#         serializer.create(serializer.data)
#         return Response({'ok':"qoshildi"},status=status.HTTP_201_CREATED)


# Mahsulot nomi uchun(ProductName)
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def productname_list(request):
    if request.method == 'GET':
        productname = ProductName.objects.all()
        serializers = ProductNameSerializers(productname, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ProductNameSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def productname_detail(request, pk):
    try:
        productname = ProductName.objects.get(pk=pk)
    except ProductName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = ProductNameSerializers(productname)
        return Response(serilazer.data)
    elif request.method == 'PUT':
        serializer = ProductNameSerializers(productname, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        productname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Manba uchun (Origin)
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def origin_list(request):
    if request.method == 'GET':
        origin = Origin.objects.all()
        serializers = OriginSerializers(origin, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = OriginSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def origin_detail(request, pk):
    try:
        origin = Origin.objects.get(pk=pk)
    except Origin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = OriginSerializers(origin)
        return Response(serilazer.data)
    elif request.method == 'PUT':
        serializer = OriginSerializers(origin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        origin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Hisob raqam uchun (Accountnumber)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def accountnumber_list(request):
    if request.method == 'GET':
        accountnumber = AccountNumber.objects.all()
        serializers = AccountnumberSerializers(accountnumber, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = AccountnumberSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def accountnumber_detail(request, pk):
    try:
        accountnumber = AccountNumber.objects.get(pk=pk)
    except AccountNumber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountnumberSerializers(accountnumber)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AccountnumberSerializers(accountnumber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        accountnumber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Yil oylari Month


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def month_list(request):
    if request.method == 'GET':
        month = Months.objects.all()
        serializers = MonthSerializers(month, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = MonthSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def month_detail(request, pk):
    try:
        month = Months.objects.get(pk=pk)
    except Months.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MonthSerializers(month)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MonthSerializers(month, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        month.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CounterPart - Kontragent
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def counterpart_list(request):
    if request.method == 'GET':
        counter = Counterparty.objects.all()
        serializers = CounterpartySerializers(counter, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = CounterpartySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def counterparty_detail(request, pk):
    try:
        counter = Counterparty.objects.get(pk=pk)
    except Counterparty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CounterpartySerializers(counter)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CounterpartySerializers(counter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        counter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Employess - Hodimlar
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def employes_list(request):
    if request.method == 'GET':
        employes = Employees.objects.all()
        serializers = EmployesSerializers(employes, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = EmployesSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def employes_detail(request, pk):
    try:
        employes = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmployesSerializers(employes)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployesSerializers(employes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        employes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # RawMaterial - Hom ashyolar


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def rawmaterial_list(request):
    if request.method == 'GET':
        rawmaterial = RawMaterial.objects.all()
        serializers = RawMaterialSerializers(rawmaterial, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = RawMaterialSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def rawmaterial_detail(request, pk):
    try:
        rawmaterial = RawMaterial.objects.get(pk=pk)
    except RawMaterial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RawMaterialSerializers(rawmaterial)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RawMaterialSerializers(rawmaterial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        rawmaterial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

