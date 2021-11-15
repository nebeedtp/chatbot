from django.db import models
from django.contrib.auth.models import User

class BotPost(models.Model):
    
    user_id = models.ForeignKey(User,  null=True, db_column='user_id', related_name="user_id", on_delete=models.CASCADE)
    date_added = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)

