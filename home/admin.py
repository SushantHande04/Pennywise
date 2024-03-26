from django.contrib import admin
from .models import addcash
from .models import user_info
# Register your models here.
#admin.site.register(addcash)
@admin.register(addcash)
class AddExpenseAdmin(admin.ModelAdmin):
    list_display = ['user_id' ,'purpose', 'category', 'amount', 'date']

@admin.register(user_info)
class userInfo(admin.ModelAdmin):
    list_display = ['user_id', 'income']