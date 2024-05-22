import settings

import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

# For cog
from cogs.greetings import Greetings
from cogs.messages import Messages


def run():
    # Enable all type of intents. *Only for developing*.
    intents = discord.Intents.all()
    # Choose intent types to enable
    # intents = discord.Intents.default()
    # intents.message_content = True # Enable message intents

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    # When bot is online.
    async def on_ready():
        # Show message with the format I set.
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")


        # from cmds directory, get every files which name finish with .py
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            # ignore init file.
            if cmd_file.name != "__init__.py":
                # last 3 characters are ".py"
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

        
        # Loading cog
        # With load_extension, don't need bog.add_cog(Greetings())
        # await bot.load_extension("cogs.greetings")
        # await bot.add_cog(Greetings(bot))

        # Load cogs with directory
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                # load cog files, without ".py"
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

        # Command for reloading bot commands loaded with cog.
        @bot.command()
        async def reload(ctx, cog: str):
            await bot.reload_extension(f"cogs.{cog.lower()}")

    @bot.event
    # Global error handler.
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globally")



    bot.run(settings.TOKEN, root_logger=True)

if __name__ == "__main__":
    run()