from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TOKEN', 'define me!')
    AI_TOKEN: Final = environ.get('AI_TOKEN', 'define me!')
