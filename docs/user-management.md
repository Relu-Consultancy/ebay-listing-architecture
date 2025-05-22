# eBay SKU Management - Django User Management Models

This module defines the core user and eBay account management models
for a SaaS platform managing eBay SKU listings.

---

## Model Overview

### User
- Custom user model that uses **email** as the unique identifier.
- Stores user's first name, last name, and email.
- Includes flags for active status and staff/admin privileges.
- Managed by a custom user manager to handle creation and superuser creation.

### eBayAccount
- Represents an eBay seller account connected via OAuth.
- Stores eBay user ID and encrypted OAuth tokens with expiry times.
- Has a friendly account name for display.
- Inherits timestamps for created/updated tracking.

### eBayAccountUserRole
- Maps a User to an eBayAccount with a specific role.
- Roles include Super-Admin, Admin, Reviewer, Creator, and Drafter.
- Enforces unique user-account-role assignment.
- Supports role-based access control (RBAC) for authorization.

---

## Usage Example

```python
from yourapp.models import User, eBayAccount, eBayAccountUserRole

# Create a user
user = User.objects.create_user(
    email="alice@example.com",
    password="securepassword",
    first_name="Alice",
    last_name="Smith"
)

# Create an eBay account
ebay_account = eBayAccount.objects.create(
    ebay_user_id="ebay_12345",
    access_token_encrypted="encrypted_access_token",
    refresh_token_encrypted="encrypted_refresh_token",
    access_token_expires_at="2025-05-22T12:00:00Z",
    refresh_token_expires_at="2025-11-22T12:00:00Z",
    account_name="Alice's eBay Store"
)

# Assign Admin role to the user for this eBay account
role = eBayAccountUserRole.objects.create(
    user=user,
    ebay_account=ebay_account,
    role=eBayAccountUserRole.StaffRole.ADMIN
)

print(role.get_role_display())  # Output: Admin
print(user.get_full_name())     # Output: Alice Smith
