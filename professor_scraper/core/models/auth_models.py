import re
import base64 
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission,
)
from cryptography.fernet import Fernet
from django.conf import settings


from core.choice import UserRole, UserStatus, Gender

import logging
logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        if not role:
            raise ValueError("Users must have a role.")
        if password:
            validation_result, message = User.validate_password(password)
            if not validation_result:
                raise ValueError(message)

        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)

        # Encrypt password using custom algorithm
        user.set_encrypted_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", UserRole.ADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        Group, verbose_name="groups", blank=True, related_name="professor_scraper_user_groups"
    )
    user_permissions = models.ManyToManyField(
        Permission, verbose_name="user permissions", blank=True, related_name="professor_scraper_user_permissions"
    )
    
    email = models.EmailField(unique=True, verbose_name="user email address", max_length=255)
    role = models.CharField(max_length=30, choices=UserRole.choices, default=UserRole.VISITOR)
    user_status = models.CharField(max_length=20, choices=UserStatus.choices, db_index=True, default=UserStatus.ACTIVE)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.OTHERS)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["role", "first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # Custom password encryption and decryption using Fernet
    @staticmethod
    def get_fernet_key():
        # Use Fernet symmetric encryption key from settings or generate one securely.
        return settings.SECRET_KEY[:32].encode()  # Ensure key length is correct for Fernet

    def set_encrypted_password(self, raw_password):
        """Encrypt the password before saving."""
        fernet = Fernet(base64.urlsafe_b64encode(self.get_fernet_key()))
        encrypted_password = fernet.encrypt(raw_password.encode())
        self.password = encrypted_password.decode()  # Store as a string

    def check_password(self, raw_password):
        """Decrypt and compare the password during authentication."""
        fernet = Fernet(base64.urlsafe_b64encode(self.get_fernet_key()))
        try:
            decrypted_password = fernet.decrypt(self.password.encode()).decode()
            return decrypted_password == raw_password
        except Exception:
            return False

    @staticmethod
    def validate_password(password):
        """
        Validate password based on length, uppercase, lowercase, numeric, and special character requirements.
        Returns a tuple (is_valid, message) where is_valid is True if password is valid, otherwise False.
        """
        if len(password) < 6:
            return False, "Password must be at least 6 characters long."
        if len(password) > 12:
            return False, "Password must not exceed 12 characters."
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter."
        if not re.search(r"\d", password):
            return False, "Password must contain at least one digit."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character."

        return True, "Password is valid."

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)