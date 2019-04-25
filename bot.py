from pyrogram import Client, Filters
import pyrogram
import telepot 
import telethon

app = Client('account')

@app.on_message(Filters.chat('ferrariline1'))
def forawrd(client, message):
    client.forward_messages('icc_cricket', 'ferrariline1', [message.message_id])
app.run() 
