# Code Review Training Repository

This repository is designed for teaching technical leadership through code review using Conventional Comments.

## Purpose

This project demonstrates effective code review practices using four types of conventional comments:

- **Praise**: Highlight good practices and positive contributions
- **Question**: Ask for clarification or understanding
- **Suggestion**: Recommend improvements that aren't critical
- **Blocker**: Identify issues that must be fixed before merging

## Project Structure

```
.
├── main.py           # FastAPI application with auth endpoints
├── models.py         # Pydantic models for request/response
├── tests/            # Pytest test suite
│   └── test_auth.py
├── requirements.txt  # Python dependencies
├── pytest.ini        # Pytest configuration
├── review_notes.md   # Code review guide and conventional comments reference
├── .gitignore        # Git ignore patterns
└── README.md         # This file
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Run tests:
   ```bash
   pytest
   ```

## API Endpoints

- `GET /` - Welcome message
- `POST /signup` - Register a new user
- `POST /signin` - Sign in an existing user

## Training Exercise

This repository contains two pull requests designed for code review practice:

1. **Demo PR**: Instructor will demonstrate reviewing code with conventional comments
2. **Practice PR**: Fellows will practice reviewing code on their own

Each PR contains intentional issues for identifying questions, suggestions, blockers, and praiseworthy changes.

## Note

This is a teaching project. The authentication implementation is intentionally simplified and should not be used in production.
