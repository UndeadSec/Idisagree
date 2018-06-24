
import discord
import subprocess

client = discord.Client()

@client.event
async def on_message(message):

    if message.content:
        if str(message.author) == botMaster:
            comando = subprocess.getoutput(str(message.content))
            msg = 'Command granted by {0.author.mention}\n{1}'.format(message, comando)
            await client.send_message(message.channel, msg)	


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(botToken)
