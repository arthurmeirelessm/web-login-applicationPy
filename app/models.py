from django.db import models

# Create your models here.

class Admin(models.Model):
      nome = models.CharField(max_length=100)
      email = models.EmailField(max_length=50)
      contato = models.CharField(max_length=50)
      password = models.CharField(max_length=100)

      class Meta: 
        db_table="admin"