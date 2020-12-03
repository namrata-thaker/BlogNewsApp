from django.db import models


# Create your models here.

class Account(models.Model):
     accountid = models.AutoField(primary_key=True)
     email = models.EmailField(max_length=100, unique=True)
     password = models.CharField(max_length=100)

     def __str__(self):
         return self.email

class Blog(models.Model):
    blogid = models.AutoField(primary_key=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title



