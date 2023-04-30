from django.db import models
from user_role.models import AbstractUser

from core.utils import user_directory_path


class User(AbstractUser):
    photo = models.ImageField(verbose_name="Фото профиля", default="static/default.jpg", upload_to=user_directory_path)

