from fastapi import APIRouter
from typing import List
from . import users_controller as controller
from .users_schema import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """Create a new user."""
    return controller.create_user(user)


@router.get("/", response_model=List[UserResponse])
def get_users():
    """Get all users."""
    return controller.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Get user by ID."""
    return controller.get_user(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    """Update user information."""
    return controller.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int):
    """Delete a user."""
    return controller.delete_user(user_id)
