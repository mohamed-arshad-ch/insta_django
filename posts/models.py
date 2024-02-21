from django.db import models
# Create your models here.
class SearchedUser(models.Model):  
    
    userName = models.CharField(max_length=100)  
    
    class Meta:  
        db_table = "searched_users"  


class InstaData(models.Model):  
    
   related_model = models.ForeignKey(SearchedUser, on_delete=models.CASCADE)
   json_data = models.JSONField()
   file_name = models.CharField(max_length=200)
   files_array = models.JSONField()
   flag = models.BooleanField(default=True  )

   class Meta:  
        db_table = "insta_data" 