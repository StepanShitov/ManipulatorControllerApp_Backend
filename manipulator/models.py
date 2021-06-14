from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    userPassword = models.CharField(max_length=200)

    def __str__(self):
        return "Login: " + self.username + "; Password: " + self.userPassword + ";"


class Logs(models.Model):
    actionDate = models.CharField(max_length=100)
    userName = models.CharField(max_length=200)
    actionContains = models.CharField(max_length=200)
    
    def __str__(self):
        return self.userName