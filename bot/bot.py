from vkbottle.bot import Bot

from config import api, labeler, state_dispenser, BOT


bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)
setattr(BOT, 'bot', bot)


import handlers
bot.run_forever()