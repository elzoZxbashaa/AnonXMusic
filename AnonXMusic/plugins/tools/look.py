import random
from config import *
from AnonXMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


async def Who(m, user_id):
  user = message.chat.get_member(user_id)
  if useimport random
from config import *
from AnonXMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


async def Who(m, user_id):
  user = message.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []

@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
async def of_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions())
  message.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
async def on_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  message.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب", "") & filters.group)
async def of_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  message.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب", "") & filters.group)
async def on_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  message.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه", "") & filters.group)
async def of_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  message.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه", "") & filters.group)
async def on_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  message.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
async def msg(client, message):
  text = message.text
  idchat = message.chat.id

  if message.from_user.id in mute:
    message.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         message.reply(Text,quote=True)

  if message.forward_date:
    if idchat in forward:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         message.reply(Text,quote=True)
r.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []

@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
async def of_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions())
  message.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
async def on_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  message.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب", "") & filters.group)
async def of_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  message.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب", "") & filters.group)
async def on_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  message.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه", "") & filters.group)
async def of_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  message.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه", "") & filters.group)
async def on_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  message.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
async def msg(client, message):
  text = message.text
  idchat = message.chat.id

  if message.from_user.id in mute:
    message.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         message.reply(Text,quote=True)

  if message.forward_date:
    if idchat in forwardimport random
from config import *
from AnonXMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


async def Who(m, user_id):
  user = message.chat.get_member(user_id)
  if useimport random
from config import *
from AnonXMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


async def Who(m, user_id):
  user = message.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []

@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
async def of_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions())
  message.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
async def on_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  message.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب", "") & filters.group)
async def of_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  message.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب", "") & filters.group)
async def on_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  message.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه", "") & filters.group)
async def of_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  message.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه", "") & filters.group)
async def on_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  message.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
async def msg(client, message):
  text = message.text
  idchat = message.chat.id

  if message.from_user.id in mute:
    message.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         message.reply(Text,quote=True)

  if message.forward_date:
    if idchat in forward:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         message.reply(Text,quote=True)
r.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []

@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
async def almortagel(client, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=almortagel)

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
async def of_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions())
  message.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
async def on_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  message.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب", "") & filters.group)
async def of_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  message.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب", "") & filters.group)
async def on_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  message.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه", "") & filters.group)
async def of_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  message.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه", "") & filters.group)
async def on_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER_ID:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  message.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
async def msg(client, message):
  text = message.text
  idchat = message.chat.id

  if message.from_user.id in mute:
    message.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         message.reply(Text,quote=True)

  if message.forward_date:
    if idchat in forward:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         message.reply(Text,quote=True)

      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER_ID:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         message.reply(Text,quote=True)
