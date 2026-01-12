"""Tests for authentication endpoints."""

import pytest
from fastapi.testclient import TestClient
from main import app, users_db


@pytest.fixture
def client():
    """Create a test client."""
    users_db.clear()  # Clear the database before each test
    return TestClient(app)


def test_root_endpoint(client):
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Auth Demo API"}


def test_signup_success(client):
    """Test successful user registration."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "secretpass"
    }
    response = client.post("/signup", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["message"] == "User registered successfully"


def test_signup_duplicate_username(client):
    """Test that duplicate usernames are rejected."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "secretpass"
    }
    # First signup should succeed
    response = client.post("/signup", json=user_data)
    assert response.status_code == 201

    # Second signup with same username should fail
    response = client.post("/signup", json=user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"


def test_signin_success(client):
    """Test successful user sign in."""
    # First, sign up a user
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "secretpass"
    }
    client.post("/signup", json=user_data)

    # Now sign in
    signin_data = {
        "username": "testuser",
        "password": "secretpass"
    }
    response = client.post("/signin", json=signin_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["message"] == "Sign in successful"


def test_signin_invalid_username(client):
    """Test sign in with non-existent username."""
    signin_data = {
        "username": "nonexistent",
        "password": "secretpass"
    }
    response = client.post("/signin", json=signin_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_signin_invalid_password(client):
    """Test sign in with incorrect password."""
    # First, sign up a user
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "secretpass"
    }
    client.post("/signup", json=user_data)

    # Try to sign in with wrong password
    signin_data = {
        "username": "testuser",
        "password": "wrongpass"
    }
    response = client.post("/signin", json=signin_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
