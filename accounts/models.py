from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your CustomManager here.

class AccountManager(BaseUserManager):
    def _create_user(self, username, email, phone, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given email must be set')
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(
            username = username,
            email=email,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, username, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, phone, password, **extra_fields)


    def create_superuser(self, username, email, phone, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, phone, password, **extra_fields)


# Create your models here.

type_choices = (
    ('R1', 'R1'),
    ('R2', 'R2'), 
    ('R3' ,'R3'),
    )

class Accounts(AbstractUser,PermissionsMixin):
    name     = models.CharField(max_length=50, null = True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(unique=True,max_length=255)
    phone    = models.CharField(max_length=50,unique=True)
    usertype = models.CharField(choices=type_choices, max_length=100, null=True, blank=True)


    #required


    date_joined     =   models.DateTimeField(auto_now_add=True)
    last_login      =   models.DateTimeField(auto_now_add=True)
    is_admin        =   models.BooleanField(default=False)
    is_staff        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=True)
    is_superuser    =   models.BooleanField(default=False)
    

    def __str__(self):
        return self.username
    

    object = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone']
    

    class meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'