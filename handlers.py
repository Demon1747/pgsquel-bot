import os, random, re
import config

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

router = Router()

words = [
    "sq.*",
    ".*ql",
    "postgre.*",
    "mong.*",
    "sequel.*",
    "select",
    "where",
    "from",
    "update",
    "delete",
    "drop",
    "join",
    "create?",
    "insert",
    ".*db",
    "databas.*",
    "data bas.*",
    "э?ску[эе]?л.*",
    "сик.?в?[эе]л.*",
    "эс к.?ю эл.*",
    "постгр.*",
    "монг.*",
    "баз.* данных",
    ".*бд",
    "бд.*",
    "гриб.*",
]

regex = re.compile("|".join(["^(?:\S*\s)*" + x + "(:?\s\S*)*$" for x in words]))

@router.message()
async def message_handler(msg: Message):
    if regex.match(msg.text.lower()):
        picture = FSInputFile(config.pics_root + random.choice(os.listdir(config.pics_root)))
        await msg.answer_photo(photo=picture)
