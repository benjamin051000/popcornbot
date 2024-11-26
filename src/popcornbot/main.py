import discord
from discord.ext import commands
from dotenv import dotenv_values

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


def main():
    # The env var might exist, but it might not have a value, I guess?
    token = dotenv_values()["DISCORD_APPLICATION_TOKEN"]
    if not token:
        raise ValueError(
            "Error loading token. Did you create one and paste it in `.env`?"
        )

    bot.run(token)


if __name__ == "__main__":
    main()
