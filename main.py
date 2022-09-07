import discord
import os
import os.path
import generate, learn
from discord.ext import tasks

client = discord.Client(intents=discord.Intents.all(), )
me = 281442888641150977
me = int(me)
manny = 346251130365542402
manny = int(manny)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

  global me_user, manny_user
  me_user = client.get_user(me)
  manny_user = client.get_user(manny)
#   annoy.start()
    

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.author.id == manny:
    learn.main(msg)

  if message.author.id == me and msg.startswith("$learn"):
    
    guild = client.get_guild(944298608709210203)

    with open("message_list.txt", "w") as file:
      for channel in guild.text_channels:
        async for message in channel.history(limit=None):
          if message.author == manny_user:
            if not message.content == "":
              if not (message.content.endswith((".png", ".txt", ".html", ".css", ".php", ".py", ".js", ".sql")) or message.content.startswith(("http", "www", "```","$","!","-","?","<",">","/","\\"))):
                file.write(message.content+ "-|-")
                # learn.main(message.content)
        
    learn.main()
      

  if msg.startswith("$mankov"):
    await message.channel.send(generate.main())

@tasks.loop(hours = 1)
async def annoy():
    channel = client.get_channel(int("748914556973219899"))
    await channel.send(generate.main())


