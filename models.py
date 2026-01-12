"""Data models for user authentication."""

from pydantic import BaseModel, EmailStr


class UserSignUp(BaseModel):
    """Model for user sign up request."""
    username: str
    email: EmailStr
    password: str


class UserSignIn(BaseModel):
    """Model for user sign in request."""
    username: str
    password: str


class UserResponse(BaseModel):
    """Model for user response."""
    username: str
    email: str
    message: str
