from django.conf import settings
from django.db import models
from django.urls import reverse

from classroom.models import User

# Create your models here.
class Student(models.Model):
    Activate = 1
    Deactivate = 0
    #associations
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='createby',blank=True)

    # Student Stuff
    roll_number = models.IntegerField(unique=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    std_class   = models.CharField(max_length=150)
    email_id    = models.EmailField(max_length=100)
    address     = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    student_status   = (
            (Activate, 'Activate'),
            (Deactivate, 'Deactivate'),
        )

    def __str__(self):
        return self.roll_number

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" #this is for hard code url pattern
        return reverse("detail", kwargs={'pk':self.pk})

    # def get_absolute_url(self): #get_absolute_url
    #     #return f"/restaurants/{self.slug}" #this is for hard code url pattern
    #     return reverse("update", kwargs={'pk':self.pk})
