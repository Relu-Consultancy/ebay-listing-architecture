from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user manager to handle user creation using email instead of username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model that uses email as the unique identifier.

    Fields:
        - first_name: User's first name.
        - last_name: User's last name.
        - email: Email address (unique).
        - is_active: Designates whether this user account is active.
        - is_staff: Designates whether the user can log into the admin site.
    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Return the user's short name (first name)."""
        return self.first_name


class TimeStampedModel(models.Model):
    """
    Abstract base model to add created and updated timestamps to models.

    Fields:
        - created_at: Timestamp when the record was created.
        - updated_at: Timestamp when the record was last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True, help_text="When this record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="When this record was last updated.")

    class Meta:
        abstract = True


class eBayAccount(TimeStampedModel):
    """
    Represents an eBay account linked to the system.

    Fields:
        - ebay_user_id: Unique eBay user identifier.
        - access_token_encrypted: Encrypted OAuth access token.
        - refresh_token_encrypted: Encrypted OAuth refresh token.
        - access_token_expires_at: Expiry datetime for access token.
        - refresh_token_expires_at: Expiry datetime for refresh token.
        - account_name: Optional display name for the eBay account.
    """
    ebay_user_id = models.CharField(max_length=255, unique=True)
    access_token_encrypted = models.TextField()
    refresh_token_encrypted = models.TextField()
    access_token_expires_at = models.DateTimeField()
    refresh_token_expires_at = models.DateTimeField()
    account_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.account_name or self.ebay_user_id


class eBayAccountUserRole(TimeStampedModel):
    """
    Associates a User with an eBayAccount and assigns a role for access control.

    Fields:
        - user: ForeignKey to User.
        - ebay_account: ForeignKey to eBayAccount.
        - role: User role for this eBay account.

    Roles:
        Defined using Django TextChoices:
            - Super-Admin
            - Admin
            - Reviewer
            - Creator
            - Drafter

    Constraints:
        - Unique constraint on (user, ebay_account) to avoid duplicate role assignments.
    """
    class StaffRole(models.TextChoices):
        SUPER_ADMIN = "Super-Admin", "Super Admin"
        ADMIN = "Admin", "Admin"
        REVIEWER = "Reviewer", "Reviewer"
        CREATOR = "Creator", "Creator"
        DRAFTER = "Drafter", "Drafter"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ebay_roles'
    )
    ebay_account = models.ForeignKey(
        eBayAccount,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )
    role = models.CharField(max_length=20, choices=StaffRole.choices)

    class Meta:
        unique_together = ('user', 'ebay_account')

    def __str__(self):
        return f"{self.user.email} - {self.ebay_account} ({self.get_role_display()})"
