from django.db import models 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , 
                                on_delete=models.CASCADE , )  # agar user o'chsa profile ham o'chadi 
    
    photo = models.ImageField(upload_to='users/' , blank=True , null=True)
    date_of_birth = models.DateField(blank=True  , null=True)

    def get_absolute_url(self):
        return reverse('lawyer_detail', kwargs={'lawyer_slug': self.lawyer_slug})

    def __str__(self):
        return f"{self.user.username} profile "
    
    

