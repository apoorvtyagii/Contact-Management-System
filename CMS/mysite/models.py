from django.db import models



class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=10)
    office = models.CharField(max_length=100)
    createdby = models.EmailField(max_length=100)

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = "Contacts"


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = "Users"
