from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True,
    unique=True, allow_unicode=True) #pk 대신 사용되는 값

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name   

    def get_absoloute_url(self):  
        return reverse('shop:product_in_category', args=[self.slug]) #모델을 바로 출력만 해도 해당 모델의 주소가 자동으로 디스플레이



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True) 
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True) 
    image = models.ImageField(upload_to='products/&Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #8자리 금액과 소수점 두자리
    stock = models.PositiveIntegerField()
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,
        self.slug])

