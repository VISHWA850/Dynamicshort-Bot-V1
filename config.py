# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "20337498"))
API_HASH = os.environ.get("API_HASH", "49fe4304b7c240cbfe4dbc8707ea43b3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5882205946:AAGbTr7qXByaCNbUNZ067N0Y-tghDckMqo4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("904093599")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Dynamicshort")
DATABASE_URL = os.getenv("DATABASE_URL", "https://ill-pear-indri-shoe.cyclic.app") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "VISHWA850")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append("Id_Owned_Id")
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
