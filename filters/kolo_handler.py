import re

from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config


class KoloFilter(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        if message.content_type != 'text':
            return False
        return re.search(config.pattern, message.text, re.IGNORECASE) is not None
