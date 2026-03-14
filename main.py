# import discord
# from reply import ask_gemma

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f"{client.user} 上線了")

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         # 檢查機器人是否被 tag
#         if client.user in message.mentions:
#             # 去掉 tag
#             content = message.content.replace(f'<@{client.user.id}>', '').strip()
#             if content == '':
#                 reply = "你叫我嗎？"
#             else:
#                 reply = ask_gemma(content)
#             await message.channel.send(reply)

# token = open('token.txt', 'r').read()
# intents = discord.Intents.default()
# intents.message_content = True
# client = MyClient(intents=intents)
# client.run(token)


import discord
import re
from reply import ask_gemma

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"{self.user} 上線了")  # 這裡要用 self.user

    async def on_message(self, message):
        # 不回應自己
        if message.author == self.user:
            return

        # 檢查機器人是否被 tag
        if self.user in message.mentions:
            # 去掉 tag
            content = message.content.replace(f'<@{self.user.id}>', '').strip()
            
            if content == '':
                reply = "你叫我嗎？"
            else:
                reply = ask_gemma(content)

            # 自動斷行，按句號、驚嘆號、問號或換行切段
            chunks = re.split(r'(?<=[。！？\n])', reply)
            buffer = ""

            for chunk in chunks:
                if len(buffer) + len(chunk) > 2000:
                    await message.channel.send(buffer)
                    buffer = chunk
                else:
                    buffer += chunk

            if buffer:
                await message.channel.send(buffer)

# 讀取 token
token = open('token.txt', 'r').read().strip()

# 設定 intents
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)