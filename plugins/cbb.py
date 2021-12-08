#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"Hai, Bot ini adalah bot yang dibuat untuk berbagi file lewat links dan juga bisa menambah sub channel anda.\n<b>Pemilik Bot : </b> <a href='tg://user?id={OWNER_ID}'>Kirim Pesan</a>\n\n<i>Bot ini di Program oleh @ryanx, pengan juga? silakan inbox saya kakak </i>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass