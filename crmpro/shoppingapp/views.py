from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from . models import Shopping
from . serializers import ShoppingSerializers

#Xarid uchun
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def shopping_list(request):
    if request.method == 'GET':
        shoppings = Shopping.objects.all()
        serializers = ShoppingSerializers(shoppings,many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializers = ShoppingSerializers(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response({'ok': "qoshildi"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def shopping_detail(request, pk):
    try:
        shopping = Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilazer = ShoppingSerializers(shopping)
        return Response(serilazer.data)
    elif request.method == 'PUT':
        serializer = ShoppingSerializers(shopping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        shopping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
