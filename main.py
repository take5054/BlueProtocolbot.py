import discord,random,antigravity,os,re,time,asyncio
from discord import app_commands,ui,Integration, Intents, Interaction
from discord.ext import tasks,commands
from discord.ui import Select, View
from discord.app_commands import CommandTree
from discord.channel import VoiceChannel
from datetime import datetime,date
import traceback

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
slash = app_commands.CommandTree(client)
f = open('token.txt','r')
TOKEN = f.read()
f.close
CHANNEL_ID = 789831636526432296
ver = '0.5.1α'
voiceChannel: VoiceChannel
vol = 1
path = os.path.dirname(__file__)

@client.event
async def on_ready():
    print(ver)
    await client.change_presence(activity=discord.Game(name='currently testing', type=1))
    await slash.sync()
    loop.start()
    for command in slash.walk_commands():
        print(command.name)

class Feedback(discord.ui.Modal, title='Feedback'):
    name = discord.ui.TextInput(
        label='ネームド',
        placeholder='計測目標ネームドの名前',
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)


@slash.command(name='help',description='ヘルプ')
async def help(ctx):
    embed = discord.Embed(title='**Help**',color=0xeee657)
    embed.add_field(name='開発元',value='discord:たけ#0808')
    embed.add_field(name='',value='Twitter:https://twitter.com/take5054',inline=False)
    embed.add_field(name='コマンド一覧',value='',inline=False)
    for command in slash.walk_commands():
        embed.add_field(name='/'+command.name,value='',inline=False)
    await ctx.response.send_message(embed=embed)

@slash.command(name='named', description='BlueProtocolネームドinfo')
async def namedinfo(ctx, text:str):
    await ctx.response.send_modal(Feedback())

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        return

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    channel = client.get_channel(CHANNEL_ID)

client.run(TOKEN)