from pyrogram import Client,filters
import socket
import socks
'''Connect To Proxy'''
#socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',2080)
#socket.socket = socks.socksocket

'''Create Bot With Api Hash And Api Id '''
'''Take Api From Telegram WebSite Develooper Tab'''

api_hash = 'Api_hash'
api_id = 'Api_id'

'''This allows me to write the functions in another folder '''

File = dict(root='Functions')
bot = Client('Name', api_id , api_hash,plugins=File)


bot.run()