import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_register_and_login():
    # Register a new user
    response = client.post("/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpass",
        "full_name": "Test User",
        "grade": "10"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"

    # Try to register with the same username
    response = client.post("/register", json={
        "username": "testuser",
        "email": "another@example.com",
        "password": "testpass"
    })
    assert response.status_code == 400

    # Try to register with the same email
    response = client.post("/register", json={
        "username": "anotheruser",
        "email": "testuser@example.com",
        "password": "testpass"
    })
    assert response.status_code == 400

    # Login with correct credentials
    response = client.post("/token", data={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token == "testuser"

    # Login with wrong password
    response = client.post("/token", data={
        "username": "testuser",
        "password": "wrongpass"
    })
    assert response.status_code == 401

def test_profile():
    # Register and login
    client.post("/register", json={
        "username": "profileuser",
        "email": "profile@example.com",
        "password": "profilepass",
        "full_name": "Profile User",
        "grade": "11"
    })
    response = client.post("/token", data={
        "username": "profileuser",
        "password": "profilepass"
    })
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get profile
    response = client.get("/profile", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "profileuser"
    assert data["email"] == "profile@example.com"
    assert data["full_name"] == "Profile User"
    assert data["grade"] == "11"

    # Update profile
    response = client.put("/profile", headers=headers, json={
        "username": "profileuser",
        "email": "profile@example.com",
        "full_name": "Updated Name",
        "grade": "12"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Updated Name"
    assert data["grade"] == "12"

