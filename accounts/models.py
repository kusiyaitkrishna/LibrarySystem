from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    
    This model adds a user_type field to differentiate between
    librarians and regular members in the library system.
    """
    
    class UserType(models.TextChoices):
        LIBRARIAN = 'librarian', 'Librarian'
        MEMBER = 'member', 'Member'
    
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.MEMBER,
        help_text='Designates the role of this user in the library system.'
    )
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    @property
    def is_librarian(self):
        """Check if user is a librarian."""
        return self.user_type == self.UserType.LIBRARIAN
    
    @property
    def is_member(self):
        """Check if user is a member."""
        return self.user_type == self.UserType.MEMBER