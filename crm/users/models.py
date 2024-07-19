from django.contrib.auth.models import User
from django.core.validators import validate_email, RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
)


class UserModel(models.Model):
    """"Model User"""
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
    phone_number = models.CharField(max_length=16, blank=True, validators=[phone_validator,], verbose_name="phone")
    email = models.EmailField(validators=[validate_email], unique=True, verbose_name="email")

    def __str__(self):
        return self.user.username
