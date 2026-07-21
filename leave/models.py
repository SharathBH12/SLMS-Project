from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    
    
    def __str__(self):
        return self.user.username 
