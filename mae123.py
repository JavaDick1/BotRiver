from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync


api_id = 18521068
api_hash = "55642eb28de679c269fbd2b6fb24062b"
client = TelegramClient("test", api_id, api_hash)
client.start()
print("STARTED")
@client.on(events.NewMessage(chats=["moscowach", "moscowtop", 
                            "moscowlenta", "DtRoad", "mosmap", "kim_online_rus"]))
async def normal_handler(event):
        if isinstance(event.chat, types.Channel):
            username = event.chat.username
           # rdy = "@" + str(username)
           # await client.send_message("https://t.me/kek3214", rdy)
            await client.send_message("https://t.me/kek3214", event.message)
        
        
client.run_until_disconnected()

                            #"rosich_rus", "moscowtop", 
                            #$ "voenacher", "Chanel4", "chanel5"


                            #api_id = 18521068
                            #api_hash = "55642eb28de679c269fbd2b6fb24062b"