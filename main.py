from pyrogram import Client,filters
import pyrogram
from pyrogram.types import Message
import socket
import socks
'''Connect To Proxy'''
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',2080)
socket.socket = socks.socksocket

'''Create Bot With Api Hash And Api Id '''
'''Take Api From Telegram WebSite Develooper Tab'''

api_hash = '97d9e48d1a8bc978886b0fde696ffcff'
api_id = 13182989
bot = Client('erfan', api_id , api_hash)

@bot.on_message(filters.chat('testdarimtest'))
def Send_message(m:Message,c:Client):
    print(m.get)



bot.run()