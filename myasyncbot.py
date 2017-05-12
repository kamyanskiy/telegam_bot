import sys
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop


async def handle(msg):
    flavor = telepot.flavor(msg)
    content_type, chat_type, chat_id = telepot.glance(msg, flavor=flavor)
    print("content_type: {}, chat_type: {}, chat_id: {}, flavor {}".format(content_type, chat_type, chat_id, flavor))
    if content_type == 'text':
        await bot.sendMessage(chat_id, msg['text'])


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

loop.run_forever()