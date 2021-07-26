from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def _help(client: Client, message: Message):
    await message.reply_text(
        f"""**Klik Tombol dibawah untuk Melihat Panduan Bot music**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❄️ Panduan ❄️", url="https://telegra.ph/Panduan-Bot-Music-07-26"
                    )
                ]
            ]
        )
    )  
