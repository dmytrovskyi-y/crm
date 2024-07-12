from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db import models


def avatar_upload_path(instance: "Profile", filename: str) -> str:
    """
    Function that specifies the path to save profile avatars
    :param instance: Model Profile
    :param filename: The name of the avatar that is being uploaded
    :return: Path to save avatar
    """

    return f"users/{instance.pk}/user-details/{filename}"


class Profile(models.Model):
    """"Model Profile"""
    USER_ROLES = [
        ("AD", "Administrator"),
        ("OP", "Operator"),
        ("MR", "Marketer"),
        ("MG", "manager"),
    ]
    class Meta:
        ordering = ["pk"]
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=USER_ROLES, verbose_name="role")
    email = models.EmailField(validators=[validate_email], verbose_name="email")
    address = models.CharField(max_length=200, blank=True, verbose_name="address")
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_upload_path, verbose_name="avatar")

    def __str__(self):
        return self.user.username
