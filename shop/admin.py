from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)} 

admin.site.register(Category, CategoryAdmin)

@admin.register(Product)  #어노테이션 기법 아래 클래스 부르기 전에 이것을 먼저 실행
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','stock','available_display',
    'available_order','created','updated']
    
    list_filter = ['available_display','created','updated','category']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available_display',
    'available_order']