from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from AnonXMusic.utils.database import get_assistant
from pyrogram.types import Message
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic.core.call import Anony 


@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("↞ فتحوا المكالمه اللي وده يسمعنا صوته يصعد 🦦")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("المكالمه تقفلت ↞ أصواتكم كانت تفتح النفس 🍧🙊")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"↯︙قام الشخص ↫ ⦗ {message.from_user.mention} ⦘"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n↯︙بدعوة شخص الى المحادثة المرئية ↫ ⦗ [{user.first_name}](tg://user?id={user.id}) ⦘"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  
