# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Holaa {message.from_user.first_name} saya adalah {PROJECT_NAME}\n
Saya Adalah Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Anda Dengan Mudah!
➥ Ketik » /help « untuk Mengetahui daftar perintahnya

➥ Assistant : {OWNER}
</b>""",

# Edit Yang Seharusnya Lu Edit Aja:D
# Tapi Jangan di Hapus Special Thanks To nya Yaaa :'D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❄️ Owner", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "❄️ Channel", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "🎁 Donate", url=f"https://t.me/rrylx")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

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


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **✅ RLX Music player is online**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "❄️ Channel Support", url="https://t.me/RLX_OFC"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara Menggunakan BOT 📜", url="https://t.me/Vckyouuu/32"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel Support", url=f"https://t.me/RLX_OFC"
                    ),
                    InlineKeyboardButton(
                        "Created By", url=f"https://t.me/rrlyx"
                    )
                ]
            ]
        )
   )

