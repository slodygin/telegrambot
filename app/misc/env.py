from os import getenv
from typing import Final

from dotenv import load_dotenv

load_dotenv()


TG_BOT_TOKEN: Final = getenv("TG_BOT_TOKEN")
AI_TOKEN: Final = getenv("AI_TOKEN")
