# backend/tests/config_test.py

import os

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # SQLite in-memory database for testing
    SECRET_KEY = 'skrky'  # Replace with a secret key for testing
