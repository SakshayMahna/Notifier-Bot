from notifierbot.telegram_bot import TelegramBot
from config import config
import time

# List of Quotes
quotes = [
    'First, solve the problem. Then, write the code. – John Johnson',
    'Experience is the name everyone gives to their mistakes. – Oscar Wilde',
    'Code is like humor. When you have to explain it, it’s bad. – Cory House',
    'Before software can be reusable it first has to be usable. – Ralph Johnson',
    'Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
]

if __name__ == "__main__":
    # Initialize bot
    bot = TelegramBot(config)
    
    # Loop over quotes to send them
    for quote in quotes:
        # Add message to notification
        bot.add_message(quote)

        # Send notification
        bot.notify()

        # Sleep for some time
        time.sleep(10)