from pyrogram import filters
from typing import List, Union
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant

from AnonXMusic import app 

channel = "vc_xm" 
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")
