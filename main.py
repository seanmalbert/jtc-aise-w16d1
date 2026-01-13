"""FastAPI application for user authentication demo."""

from fastapi import FastAPI, HTTPException, status
from models import UserSignUp, UserSignIn, UserResponse, PasswordReset

app = FastAPI(title="Auth Demo API")

# In-memory storage for demo purposes
users_db = {}


@app.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def sign_up(user: UserSignUp):
    """
    Register a new user.

    Args:
        user: User sign up information

    Returns:
        UserResponse with registration confirmation

    Raises:
        HTTPException: If username already exists
    """
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # Store user (in production, hash the password!)
    users_db[user.username] = {
        "email": user.email,
        "password": user.password
    }

    return UserResponse(
        username=user.username,
        email=user.email,
        message="User registered successfully"
    )


@app.post("/signin", response_model=UserResponse)
async def sign_in(user: UserSignIn):
    """
    Sign in an existing user.

    Args:
        user: User sign in credentials

    Returns:
        UserResponse with sign in confirmation

    Raises:
        HTTPException: If credentials are invalid
    """
    if user.username not in users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    stored_user = users_db[user.username]
    if stored_user["password"] != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return UserResponse(
        username=user.username,
        email=stored_user["email"],
        message="Sign in successful"
    )


@app.post("/reset-password")
def reset_password(reset_data: PasswordReset):
    """Reset user password with email verification."""
    # Validate user exists
    if reset_data.username not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    stored_user = users_db[reset_data.username]

    # Validate email matches (good security practice!)
    if stored_user["email"] != reset_data.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email does not match user account"
        )

    # Update password
    users_db[reset_data.username]["password"] = reset_data.new_password

    return {
        "message": "Password reset successful",
        "username": reset_data.username,
        "new_password": reset_data.new_password
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Auth Demo API"}
