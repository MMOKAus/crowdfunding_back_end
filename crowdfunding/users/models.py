from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

# Create your models here.
class Meta:
        permissions = [
            ("can_approve_project", "Can approve project"),
            ("can_reject_project", "Can reject project"),
        ]
