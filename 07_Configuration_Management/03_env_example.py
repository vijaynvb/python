import os

os.environ["APP_ENV"] = "Development"

print("Environment:", os.getenv("APP_ENV"))