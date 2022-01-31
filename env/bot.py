import os 

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')

intents = discord.Intents.default()

client = commands.Bot(command_prefix = "m!", intents = intents)

print("Commands:\n")
for filename in os.listdir("./commands"):
    client.load_extensions(f'commands.{filename[:-3]}')
    print("{filename[:3]} has been loaded.")
    
print("Events:\n")
for filename in os.listdir("./events"):
    client.load_extensions(f'events.{filename[:3]}')
    print("{filename[:3]} has been loaded.")

client.run()

