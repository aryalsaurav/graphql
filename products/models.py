import uuid

from django.db import models

from accounts.models import Timestamp,User

# Create your models here.

class Category(Timestamp):
    name = models.CharField(max_length=512)
    parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name



class Product(Timestamp):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=512)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    image = models.ImageField(null=True,blank=True,upload_to='product_images/')
    sku = models.CharField(max_length=256,null=True,blank=True)
    stocks = models.PositiveBigIntegerField(default=0)
    
    
    
    def __str__(self):
        return self.name
    
    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    @property
    def in_stock(self):
        if self.stocks == 0:
            return False
        return True
            



class OrderItem(Timestamp):
    """
    Model definition for OrderItem.
    """
    item_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)



    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return self.item_id
    
    
        
    
    

    
class Order(Timestamp):
    order_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    order_items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    grand_total = models.DecimalField(max_digits=12,decimal_places=2)
    
    def __str__(self):
        return self.order_id
    
    
    