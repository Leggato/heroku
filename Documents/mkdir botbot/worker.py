import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-------')
	
@client.event
async def on_message(message):
	if message.content == "Hello" :
		awayt client.send_message(message.channel, "World")

client.run(MzYzNzQwODE5Mjg4NzUyMTQy.DLF_TA.ay-GjxcmjiJMNWZut7WO1mzHXVI)	