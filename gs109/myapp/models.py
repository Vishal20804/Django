from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    # user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)

    #want to create page only specific people
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})
    page_name=models.CharField(max_length=100)
    page_cat=models.CharField(max_length=100)
    page_publish_date=models.DateField(max_length=100)

