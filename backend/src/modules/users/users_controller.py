
from fastapi import HTTPException

from . import users_service as service
from .users_schema import UserCreate, UserResponse, UserUpdate


def create_user(user_data: UserCreate) -> UserResponse:
    """Create a new user."""
    user = service.create_user(name=user_data.name, email=user_data.email)
    return UserResponse.model_validate(user)


def get_all_users() -> list[UserResponse]:
    """Get all users."""
    users = service.get_all_users()
    return [UserResponse.model_validate(user) for user in users]


def get_user(user_id: int) -> UserResponse:
    """Get user by ID."""
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


def update_user(user_id: int, user_data: UserUpdate) -> UserResponse:
    """Update user information."""
    user = service.update_user(
        user_id=user_id,
        name=user_data.name,
        email=user_data.email
    )
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


def delete_user(user_id: int) -> dict:
    """Delete a user."""
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
