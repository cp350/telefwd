from telethon import TelegramClient, events
import base64
import random

apl_id = base64.b64decode("NjA2MzYyOQ==").decode()
api_hash = base64.b64decode(
    'NTRkNjk2NGRjNzk3OWI1ZjcyMWEwNjc5MTIxMGY1NDY=').decode()
api_source = base64.b64decode("LTEwMDEzNjA1NzMwNzk=").decode()
ss = str(random.random())
client = TelegramClient(ss, apl_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    msg = event.raw_text

    print("{}  {}".format(chat_id, msg))  #-592931333

    if (chat_id == -1002223178123):
        await client.send_message(
            -1002231961884,
            msg,
        )


client.start()
client.run_until_disconnected()
