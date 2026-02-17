
from database.db import Session
from database.models import User


#example of create function, currently used in the implementation but can be expanded with error handling and validation in the future
def create_user(name: str, email: str) -> User:
    """Create a new user and add to database."""
    session = Session()
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    finally:
        session.close()

#example of get all users function, currently used in the implementation but can be expanded with pagination or filtering in the future
def get_all_users() -> list[User]:
    """Retrieve all users from database."""
    session = Session()
    try:
        users = session.query(User).all()
        return users
    finally:
        session.close()

#example of get by id function, not used in current implementation but can be useful for future features
def get_user_by_id(user_id: int) -> User | None:
    """Retrieve a user by their ID."""
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    finally:
        session.close()

#example of get by email function, not used in current implementation but can be useful for future features
def get_user_by_email(email: str) -> User | None:
    """Retrieve a user by their email."""
    session = Session()
    try:
        user = session.query(User).filter(User.email == email).first()
        return user
    finally:
        session.close()

#example of update function, not used in current implementation but can be useful for future features
def update_user(user_id: int, name: str | None = None, email: str | None = None) -> User | None:
    """Update a user's information."""
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            session.commit()
            session.refresh(user)
        return user
    finally:
        session.close()

#example of delete function, not used in current implementation but can be useful for future features
def delete_user(user_id: int) -> bool:
    """Delete a user by their ID. Returns True if deleted, False if not found."""
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    finally:
        session.close()
