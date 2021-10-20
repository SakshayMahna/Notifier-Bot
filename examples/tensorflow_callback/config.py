# Good practice to store Configuration files in other file
from notifierbot.telegram.config import TelegramConfig

BOT_TOKEN = ''
CHAT_ID = ''

# Initialize TelegramConfig object using BOT_TOKEN and CHAT_ID
# BOT_TOKEN obtained from @botfather in Telegram
# CHAT_ID obtained from this url: https://api.telegram.org/bot{BOT_TOKEN}/getUpdates
config = TelegramConfig(BOT_TOKEN, CHAT_ID)