from cogs.cog_main import MyCog
import discord
from discord import app_commands, Interaction
from discord.ext import commands
from keep_alive import keep_alive

# import re
# from dotenv import load_dotenv
import os 



keep_alive()




class ShishiBOT(commands.Bot):
    def __init__(self, *, intents=None):
        if intents is None:
            intents = discord.Intents.default()
            intents.message_content = True 
        super().__init__(
            command_prefix="$",
            intents=intents,
            application_id=os.getenv("BOT_APPLICATION_ID")
        )



    async def load_cog(self):

        # 遍歷 cmds 目錄下的所有 py 檔
        for filename in os.listdir("./cogs"):
            # 判斷是否以 .py 結尾
            if filename.endswith(".py"):
                # 將檔案名稱設定為 extension_name，必須為位置加名稱
                extension_name = f"cogs.{filename[:-3]}"
            try:
                # 嘗試重新加載這個 cog
                await self.reload_extension(extension_name)

            # 如果還沒有加載過這個 cog
            except commands.ExtensionNotLoaded:
                # 就加載這個新的 cog
                await self.load_extension(extension_name)

    async def on_ready(self):
        await self.load_cog()

        if self.guilds:
            for guild in self.guilds:
                slash = await self.tree.sync(guild=guild)
                print(f"{guild.name} ({guild.id}) 載入{len(slash)}個指令 ")
        else:
            print("Bot 尚未加入任何伺服器，無法同步 slash command")

        print(f"{self.user} 上線了!")




# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f"{self.user} 上線了")  # 這裡要用 self.user

#     # 監聽 message
#     async def on_message(self, message):

#         # 不回應自己
#         if message.author == self.user:
#             return

#         # 檢查機器人呼叫指令
#         # if self.user in message.mentions:
#         if message.content.split(" ")[0] == "$汐汐":
#             # 去掉 tag
#             content = message.content.split(" ")[1::].join("")
            
#             if content == '':
#                 reply = "你叫我嗎？"
#             else:
#                 print(message.author.name, content)
#                 reply = ask_gemma(content)

#             # 自動斷行，按句號、驚嘆號、問號或換行切段
#             chunks = re.split(r'(?<=[。！？\n])', reply)
#             buffer = ""

#             for chunk in chunks:
#                 if len(buffer) + len(chunk) > 2000:
#                     await message.channel.send(buffer)
#                     buffer = chunk
#                 else:
#                     buffer += chunk

#             if buffer:
#                 await message.channel.send(buffer)


#     @bot.slash_command(name="first_slash", guild_ids=[...]) 
#     async def first_slash(ctx): 
#             await ctx.respond("You executed the slash command!")

# 讀取 APIKEY
# load_dotenv()
discord_bot_token = os.getenv("DISCORD_BOT_API_KEY")

# 設定 intents
intents = discord.Intents.default()
intents.message_content = True



shishi_bot = ShishiBOT(intents=intents)
@shishi_bot.command()
async def load(ctx: commands.Context):
    await shishi_bot.add_cog(MyCog(shishi_bot))
    await ctx.send("Ping cog loaded", ephemeral=True)

@shishi_bot.command()
async def unload(ctx: commands.Context):
    await shishi_bot.remove_cog("MyCog")
    await ctx.send("Ping cog unloaded", ephemeral=True)

@shishi_bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    await ctx.send(f"發生錯誤了: {error}")




shishi_bot.run(discord_bot_token)