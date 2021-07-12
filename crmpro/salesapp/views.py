from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny,IsAuthenticated
from . models import Sales, FuraCondition
from . serializers import SalesSerializers, FuraConditionsSerializers


# sotuv uchun

@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def sales_list(request):
    if request.method == 'GET':
        sales = Sales.objects.all()
        serializers = SalesSerializers(sales, many=True)
        a = serializers.data
        return Response(a)
    elif request.method == 'POST':
        serializers = SalesSerializers(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response({'ok': "qoshildi"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def sales_detail(request, pk):
    try:
        sales = Sales.objects.get(pk=pk)
    except Sales.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = SalesSerializers(sales)
        return Response(serilazer.data)
    elif request.method == 'PUT':
        serializer = SalesSerializers(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# fura holati

@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def fura_list(request):
    if request.method == 'GET':
        fura = FuraCondition.objects.all()
        serializers = FuraConditionsSerializers(fura, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = FuraConditionsSerializers(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response({'ok': "qoshildi"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def fura_detail(request, pk):
    try:
        fura = FuraCondition.objects.get(pk=pk)
    except FuraCondition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = FuraConditionsSerializers(fura)
        return Response(serilazer.data)
    elif request.method == 'PUT':
        serializer = FuraConditionsSerializers(fura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

