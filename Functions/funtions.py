from pyrogram import Client,filters
from pyrogram.types import Message
from googletrans import Translator
text = ''

@Client.on_message(filters.chat('testdarimtest'),group=0)
def Message_me(_:Client,m:Message):
    global text
    Text = m.text
    translate = Translator()
    Text = translate.translate(Text,dest='fa')
    text = Text.text

@Client.on_message(filters.private,group=1)
def Send_translations(_:Client,m:Message):
    m.reply_to_message(text)