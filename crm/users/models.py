# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# phone_validator = RegexValidator(
#     regex=r'^\+?1?\d{9,15}$',
#     message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
# )
#
#
# class UserModel(models.Model):
#     """"Model DB User"""
#     USER_ROLES = [
#         ("AD", "Administrator"),
#         ("OP", "Operator"),
#         ("MR", "Marketer"),
#         ("MG", "Manager"),
#     ]
#     class Meta:
#         ordering = ["pk"]
#         verbose_name = "user"
#         verbose_name_plural = "users"
#
#     user: User = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=2, choices=USER_ROLES, verbose_name="role")
#     phone_number = models.CharField(max_length=16, blank=True, validators=[phone_validator,], verbose_name="phone")
#
#     @receiver(post_save, sender=User)
#     def create_user_model(sender, instance, created, **kwargs):
#         if created:
#             UserModel.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_model(sender, instance, **kwargs):
#         instance.usermodel.save()
#
#     def __str__(self):
#         return self.user.username
