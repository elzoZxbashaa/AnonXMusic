from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from AnonXMusic.utils.database import get_assistant
from pyrogram.types import Message
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic.core.call import Anony 

@app.on_message(filters.regex("مين في الكول"))
async def strcall(client, message):
    assistant = await group_assistant(Zoro,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("ErorMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"عمووووو الكول مش مفتوح اصلااا\n❌")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n❌")
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
