import os
APP_ENV = os.getenv('APP_ENW', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'admin')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres_test')