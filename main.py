import discord 
from discord.ext import commands
from discord.flags import Intents
import asyncio

intents = discord.Intents.all() # Adiconando comandos que o bot tera que executar
client = commands.Bot(command_prefix='$', intents= intents)  # Adiconamos um prefixo ao nosso Bot e o intents sao os comandos que queremos que o Bot execute.

@client.command(name='ola') # comando que sera executado

async def ola(context):
    await context.message.channel.send('Hello world !') # Canal onde a mensagem foi enviada

@client.event
async def on_ready(): # on_ready geralmente e utilizado para pegar alguma informação
    print("-="*25)
    print(client.guilds)
    print("Bot Iniciado")
    print("-="*25)


client.run('Seu token') # iniciando Bot
