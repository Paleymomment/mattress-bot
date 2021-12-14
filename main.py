import webbrowser
import discord

url = "https://www.youtube.com/watch?v=4IwTXhCfGYk&t=33s"
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#thats what the
    if "mattress" in message.content:
        webbrowser.open(url)
#MATTRESS
    if "MATTRESS" in message.content:
        webbrowser.open(url)
#thats what the point
    if "Mattress" in message.content:
        webbrowser.open(url)
#of the
    if "matress" in message.content:
        webbrowser.open(url)
#matres.
    if "matres" in message.content:
        webbrowser.open(url)

    if "mattres" in message.content:
        webbrowser.open(url)

client.run('put your token here')
