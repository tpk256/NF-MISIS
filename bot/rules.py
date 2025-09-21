from typing import Union
import json

from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

class CourseRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        data = event.get_payload_json()
        if not data:
            return False

        return data.get("course", None) in (1, 2, 3, 4)