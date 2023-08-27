from curses import meta
from dataclasses import field
from rest_framework import serializers
from user_auth.models.product_model import Product, Cart


class ProductSerilaizer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.CharField()
    status = serializers.CharField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        instance = Product.objects.create(**validated_data)
        return instance
       

class CartSerilaizer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)



    # def get_product(self, obj):
    #     products = obj.products.all()
    #     return ProductSerilaizer(products, many=True).data


    class Meta:
        model = Cart
        fields = ("created_at", "modified_at", "products")

    def create(self, validated_data):
        product_list = validated_data.pop('products', [])
        instance = Cart.objects.create(**validated_data)
        print(instance)
        if product_list:
            instance.carts.set(product_list)
        instance.save()

        return instance

