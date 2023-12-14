import discord,random,antigravity,os,re,time,asyncio
from discord import app_commands,ui,Integration, Intents, Interaction
from discord.ext import tasks,commands
from discord.ui import Select, View
from discord.app_commands import CommandTree
from datetime import datetime,date
import traceback
import named
import openpyxl as px

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
slash = app_commands.CommandTree(client)
f = open('token.txt','r')
TOKEN = f.read()
f.close
ver = '0.5.1α'
path = os.path.dirname(__file__)
named = ''

@client.event
async def on_ready():
    print(ver)
    await client.change_presence(activity=discord.Game(name='currently testing', type=1))
    await slash.sync()
    loop.start()
    for command in slash.walk_commands():
        print(command.name)

class namedpop(discord.ui.Modal, title="計測目標ネームド"):
    name = discord.ui.TextInput(
        label='ネームド',
        placeholder='計測目標ネームドの名前',
    )

    async def on_submit(self, interaction: discord.Interaction):
        '''named = self.name.value
        embed = discord.Embed(title=f'**{named.named()}**',color=0xeee657)
        embed.add_field(name='',value='')'''
        data = openpyxl.load_workbook(path+ '/nameddata.xlsx')
        datas = data["Sheet1"]
        active_sheet = data.active
        for row in active_sheet.rows:
            excel = []
            for cell in row:
                excel.apped(cell.value)
        await interaction.response.send_message(f"{temp}")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('ERROR', ephemeral=True)
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
async def namedinfo(ctx):
    await ctx.response.send_modal(namedpop())

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

client.run(TOKEN)