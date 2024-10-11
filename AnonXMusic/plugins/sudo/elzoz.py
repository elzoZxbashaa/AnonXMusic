import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
                
@app.on_message(
    command(["زوز","الزوز","عم الكون","zoz","ZOZ","elzoz","ELZOZ","المطور الزوز"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("DaRrKNneSs_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["زوز","الزوز","elzoz","zoz","elzoz","ELZOZ"])
    & filters.group
)
@app.on_message(
    command(["‹ الزوز ›"])
    & filters.private 
)
async def yas(client, message):
    usr = await client.get_chat("V_K_Z")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
@app.on_message(
    command(["بوت"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("K6O_BoT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"Hi My Name iS Elzoz n\nA Strong Telegram Bot To Play Music & Video iN The Voice Chat.\n\nJust Add Me To Your Group And Send /help . ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/ElZoZ?startgroup=true")
                ],
            ]
        ),
    )

@app.on_message(
    command(["الزوز","باشا","غشيم ","الـ غشيم"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("gs_y1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["رعد","الراعي","العباس"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("QIIIlIP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
