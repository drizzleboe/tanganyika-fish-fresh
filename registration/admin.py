from django.contrib import admin
from .models import *

# Register your models here.


class pplt(admin.ModelAdmin):
  prepopulated_fields={'slug':('product_title', )}

class admincust(admin.ModelAdmin):
    list_display=['email','message','phone','date','time']
    list_filter =['date','email','phone']

class order_cust(admin.ModelAdmin):
    list_display=['s_title','phone','email','date','time']
    list_filter =['date','email','phone']

class sub_(admin.ModelAdmin):
    list_display=['email','date','time']
    list_filter =['date','email']
  #  prepopulated_fields={'slug':('fname','lname')}



admin.site.register(contact,admincust)
admin.site.register(order,order_cust)
admin.site.register(gallery_top_image)
admin.site.register(gallery_other_image)
admin.site.register(our_potential)
admin.site.register(about_u)
admin.site.register(comment)
admin.site.register(product,pplt)
admin.site.register(subscribers_email,sub_)
admin.site.register(gallery_bottom)
