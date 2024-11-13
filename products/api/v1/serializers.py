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



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','item_id','product','user','quantity','total']
        extra_kwargs = {
            'item_id':{'read_only':True},
            'total':{'read_only':True},
        }
    
    
    def create(self,validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        
        total = product.price * quantity
        
        return OrderItem.objects.create(**validated_data,total=total)
        
    
        



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_id','order_items','user','grand_total']
        extra_kwargs = {
            'order_id':{"read_only":True},
            'grand_total':{"read_only":True}
        }
        
        
    def create(self,validated_data):
        order_items = validated_data.pop('order_items')
        grand_total = 0
        for item in order_items:
            grand_total += item.total
        order =  Order.objects.create(**validated_data,grand_total=grand_total)
        
        order.order_items.set(order_items)
        order.save()
        return order