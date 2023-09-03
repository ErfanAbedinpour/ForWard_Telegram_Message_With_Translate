from pyrogram import Client,filters
from pyrogram.types import Message
from googletrans import Translator
text = str()

@Client.on_message(filters.chat('Chanel_userNme Without @'),group=0)
def Message_me(_:Client,m:Message):
    global text
    Text = m.text
    translate = Translator()
    Text = translate.translate(Text,dest='en')
    text = Text.text

@Client.on_message(filters.chat('Chanel_userNme Without @'),group=1)
def Send_translations(_:Client,m:Message):
    _.send_message('chat_id',text)