import os
from dotenv import load_dotenv

load_dotenv()

BETTERSTACK_TOKEN = os.getenv("BETTERSTACK_TOKEN")
BETTERSTACK_HOST = os.getenv("BETTERSTACK_HOST")

