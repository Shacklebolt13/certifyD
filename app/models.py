from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    emailPass = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" or self.email or self.username


class Placeholder(models.Model):
    kind = models.CharField(
        choices=(("text", "text"), ("image", "image")), max_length=10
    )
    name = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    template = models.ForeignKey("CertificateTemplate", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.template} @({self.x},{self.y})"


class CertificateTemplate(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} by {self.user}"


class CertificateSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(CertificateTemplate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    recievers = models.ManyToManyField(User, related_name="recievers")

    def __str__(self):
        return f"{self.template} for {self.recievers.count()}"


class reciever(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    extra = models.TextField()

    class Meta:
        unique_together = (("name", "email"),)

    def __str__(self):
        return f"{self.name} ({self.email})"


class recieved_certificate(models.Model):
    id = models.UUIDField(primary_key=True)
    reciever = models.ForeignKey(reciever, on_delete=models.CASCADE)
    template = models.ForeignKey(CertificateTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reciever} recieved {self.template}"
