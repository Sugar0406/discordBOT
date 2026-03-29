import discord
from discord.ext import commands
from discord import app_commands
from reply import ask_gemma
import re
# import time
# import asyncio

class MyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def 你好汐汐(self, ctx):
        await ctx.send('正如歲主所說，你我會在此相遇')

    @commands.command()
    async def 汐汐(self, ctx, *, content):
        print(f"收到訊息: {content}")
        content += "NOTE:用繁體中文回復，不需要回復NOTE，只需要回復前方問題"
        if content == '':
            reply = "你叫我嗎？"
        else:
            reply = ask_gemma(content)

        # 自動斷行，按句號、驚嘆號、問號或換行切段
        chunks = re.split(r'(?<=[。！？\n])', reply)
        buffer = ""

        for chunk in chunks:
            if len(buffer) + len(chunk) > 2000:
                await ctx.send(buffer)
                buffer = chunk
            else:
                buffer += chunk

        if buffer:
            await ctx.send(buffer)

    # @app_commands.command(name = "hello", description = "Hello, world!")
    # async def hello(self, interaction: discord.Interaction):
    #     # 回覆使用者的訊息
    #     await interaction.response.send_message("Hello, world!")

    @app_commands.command(name="你好汐汐", description="和汐汐說你好")
    async def 你好汐寶(self, interaction: discord.Interaction):
        await interaction.response.send_message("正如歲主所說，你我會在此相遇")

    # @app_commands.command(name="問問汐汐", description="汐汐什麼都知道")
    # async def 問問汐汐(self, interaction: discord.Interaction, 問題:str):
    #     print(問題)
    #     # 記錄開始時間
    #     start_time = time.time()
    #     # 嘗試在短時間內生成（比如 2 秒）
    #     try:
    #         reply = await asyncio.wait_for(ask_gemma_async(問題), timeout=2)
    #         short_generation = True
    #     except asyncio.TimeoutError:
    #         short_generation = False

    #     # 如果生成超過 2 秒，先回覆「正在生成」
    #     if not short_generation:
    #         await interaction.response.send_message("正在生成回答，請稍等...", ephemeral=True)
    #         reply = await ask_gemma_async(問題)  # 繼續生成完整內容

    #     # 分段回覆長文
    #     max_len = 2000
    #     chunks = re.split(r'(?<=[。！？\n])', reply)
    #     buffer = ""
    #     for chunk in chunks:
    #         if len(buffer) + len(chunk) > max_len:
    #             await interaction.followup.send(buffer)
    #             buffer = chunk
    #         else:
    #             buffer += chunk
    #     if buffer:
    #         await interaction.followup.send(buffer)


async def setup(bot):
    cog = MyCog(bot)
    await bot.add_cog(cog)

    for attr_name in dir(cog):
        attr = getattr(cog, attr_name)
        if isinstance(attr, app_commands.Command):
            for guild in bot.guilds:
                bot.tree.add_command(attr, guild=guild)
