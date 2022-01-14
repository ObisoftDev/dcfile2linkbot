from Code_X_Mania.bot import StreamBot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command("LIST"))
def _start(client, message):
    client.send_message(chat_id = message.chat.id,
        text = LIST_MSG.format(message.from_user.mention),
        reply_to_message_id = message.message_id,
        parse_mode="markdown"
    )
    
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `START` \n 2. `HELP` \n 3. `LOGIN` \n 4.`FOLLOW` \n 5. `PING` \n 6. `STATUS` \n 7. `DC` this tells your telegram dc \n 8. `MAINTAINERS` "
