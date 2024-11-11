from rest_framework import serializers


from products.models import Category,Product,Order,OrderItem




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','parent']
        extra_kwargs = {
            'id':{'read_only':True}
        }
    

class ProdcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','category','description','price','sku','stocks','image']
        
        
    def to_representation(self,instance):
        data = super().to_representation(instance)
        data['category'] = instance.category.name if instance.category else None
        return data