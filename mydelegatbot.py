import sys
import asyncio
import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open

class ChatDelegate(telepot.aio.helper.ChatHandler):

    async def on_chat_message(self, msg):
	    flavor = telepot.flavor(msg)
	    content_type, chat_type, chat_id = telepot.glance(msg, flavor=flavor)
	    print("content_type: {}, chat_type: {}, chat_id: {}, flavor: {}".format(content_type, chat_type, chat_id, flavor))
	    if content_type == 'text':
	        await self.sender.sendMessage(msg['text'])

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, ChatDelegate, timeout=10),
])

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()