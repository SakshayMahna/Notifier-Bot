import pytest
import requests

from notifierbot.telegram_bot import TelegramBot, TelegramConfig

def test_telegram_bot():
    config = TelegramConfig('', '')
    bot = TelegramBot(config)
    
    bot.add_message("Test Message")
    bot.notify()