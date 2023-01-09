from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerailizer



@api_view(['GET','POST'])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many= True, context= {'request':request})
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data = request.data)


        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product
    
    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance
    

        # if serializer.is_valid():
        #     # serializer.validated_data
        #     return Response("Okay this is done")
        
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        if product.orderitem_set.count()>0:
            return Response({'error': "Product is associated with order item, so cannot delete"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerailizer(queryset, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CollectionSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection.objects.annotate(products_count = Count("products")),pk=pk)

    if request.method == "GET":
        serializer = CollectionSerailizer(collection)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CollectionSerailizer(collection, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        if collection.products.count()>0:
            return Response({"error" : "Collection cannot be deleted cause it has some products in it."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)