# from apps.trips.models import Deals
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError, models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of username.
    """

    def create_user(self, email, password, phone, name, last_name ,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))

        if not name:
            raise ValueError(_("First and Last name are required!"))
        
        if not last_name:
            raise ValueError(_("First and Last name are required!"))


        if not phone:
            raise ValueError(_("Phone number is required"))


        user = self.model(email=email, name=name,last_name=last_name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name=None, last_name=None, email=None, phone=None, password=None,):
        user = self.model(
            name = name,
            last_name=last_name,
            email = email,
            phone=phone,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user



class CustomUser(AbstractUser):
    """
    Model for Custom User
    """
    username = None
    name = models.CharField(blank=True, max_length=120, verbose_name="Имя")
    last_name= models.CharField(blank=True, max_length=120, verbose_name="Фамилия")
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    date_created= models.DateTimeField(editable=False, auto_now_add=True)
    date_updated= models.DateTimeField(default=timezone.now,)
    REQUIRED_FIELDS = ["phone", "name", "last_name"]
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return "{}  ".format(self.email)


class Reviews(models.Model):
    # deal_id = models.ForeignKey(Deals, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    raiting = models.FloatField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
    def __str__(self):
        return "{}  ".format(self.comment)