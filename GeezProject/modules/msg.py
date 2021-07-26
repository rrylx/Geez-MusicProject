from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def _help(client: Client, message: Message):
    await message.reply_text(
        f"""**Klik Tombol dibawah untuk Melihat daftar perintahnya**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Daftar Perintah 📜", url="https://telegra.ph/Daftar-Perintah-07-24"
                    )
                ]
            ]
        )
    )  
