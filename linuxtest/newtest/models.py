from django.db import models

# Create your models here.


class UserModel (models.Model):
    password = models.CharField(max_length=12)
    account = models.CharField(max_length=12)

    def __str__(self):
        return self.account


class UserTokenModel(models.Model):
    token = models.CharField(max_length=32)
    user = models.OneToOneField(to='UserModel', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.token

