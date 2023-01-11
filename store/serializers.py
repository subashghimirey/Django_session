
from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection, Review


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'inventory', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    
    
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.2)



class CollectionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title','products_count']

    products_count = serializers.IntegerField(read_only = True)

     

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        Review.objects.create(product_id = product_id, **validated_data)











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


