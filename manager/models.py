from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name")
    email = models.EmailField(verbose_name="E-mail address")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.email} - {self.name}"
