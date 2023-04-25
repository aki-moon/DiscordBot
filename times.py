#coding:UTF-8
import discord
from discord.ext import tasks

TOKEN = "dummy" #自身のトークンをここに入力
CHANNEL_ID = 11111111111 #チャンネルIDをここに入力

client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    # botが起動するまで待つ
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

loop.start()

client.run(TOKEN)