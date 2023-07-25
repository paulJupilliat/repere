from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Shopper(AbstractUser):
    pass
    # details des précedentes commmandes effectuées par le client
    