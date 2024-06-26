import os
from dotenv import load_dotenv

load_dotenv()

API_ID = 94575
API_HASH = "a3406de8d171bb422bb6ddf3bbd800e2"
BOT_TOKEN = "7027769883:AAE9mMBFJ98fKK11TUSbP-i6lP61SpXBY3g"
SUDOERS = list(map(int, os.getenv("SUDOERS", 0).split()))
MONGO_URL = os.getenv("MONGO_URL", None)
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", None)
MUST_JOIN = os.getenv("MUST_JOIN", "")
DISABLED = os.getenv("DISABLED", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
