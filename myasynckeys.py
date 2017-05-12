import sys
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(
            text='Press me', callback_data='press')],])

    await bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)


async def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    await bot.answerCallbackQuery(query_id, text='Got it')

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_forever())
print('Listening ...')

loop.run_forever()