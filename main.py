import asyncio

from bot.utils.env import load_env
from bot.utils.logs import start_logging
from bot.bot import bot

def main():
    load_env()

    start_logging()

    try:
        asyncio.run(bot())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
