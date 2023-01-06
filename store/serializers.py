
from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    
    
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.2)



class CollectionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']















# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length= 200)


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 100)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source = "unit_price")
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
#     # collection = serializers.StringRelatedField()   #stringkeyrelatedfield

#     # collection = CollectionSerializer()  //nested objects

#     collection = serializers.HyperlinkedRelatedField(
#         queryset = Collection.objects.all(),
#         view_name="Collection-detail"
#     )




#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.2)


