import os

import discord
from dotenv import load_dotenv

from signal_parser import parse_signal

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"🍯 HoneyBot is online as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!hello":
        await message.channel.send("🍯 Hello!")
        return

    signal = parse_signal(message.content)

    if signal:
        await message.channel.send(
            f"🟡 {signal['action']} detected\n"
            f"{signal['raw_message']}"
        )

client.run(DISCORD_BOT_TOKEN)