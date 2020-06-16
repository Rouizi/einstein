from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """A custom user for extension"""