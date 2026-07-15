import os

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

#os.environ["APP_ENV"] = "Development"

print("Environment:", os.getenv("APP_ENV"))