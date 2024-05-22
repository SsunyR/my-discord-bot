import settings

#[D] = Discord
import discord
from discord.ext import commands

#[L] = Logger
logger = settings.logging.getLogger("bot")

# For cog
from cogs.greetings import Greetings

#[F] = Feature
import random                                   # For the command "!choices".     


def run():
    intents = discord.Intents.all()                     # Enable all type of intents. Only for developing.

    # Choose intent types to enable
    # intents = discord.Intents.default()
    # intents.message_content = True # Enable message intents

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():                                           # When bot is online.
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")        # Show message with the format I set.

        # Loading cog
        # With load_extension, don't need bog.add_cog(Greetings())
        await bot.load_extension("cogs.greetings")
        # await bot.add_cog(Greetings(bot))

        # from cmds directory, get every files which name finish with .py
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            # ignore init file.
            if cmd_file.name != "__init__.py":
                # last 3 characters are ".py"
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    @bot.event
    async def on_command_error(ctx, error):                         # Global error handler.
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globally")


    @bot.command(           # Configuration of the command. Can be shown with "!help ping"
            aliases = ['p'],                                        # Set aliases for the command. Enable "!p | !help p".
            help = "Type !ping or !p on the channel",               # Guide of the command. How to use this command.
            description = "This command will answer with pong",     # Discription part of the bot
            brief = "Answers with pong."                            # Brief description of the command. Shows when !help typed.
            # enabled = False,                                      # To make this command enable or not.
            # hidden = True                                         # To make this command hidden or not.
    )
    async def ping(ctx):                                # ctx: Various information such as message, channel, guild etc.
        """ Answers with pong. """                      # Brief description of this command. Replaced with brief.
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, what = "WHAT?"):                     # Only take single word. Default "WHAT?."
        await ctx.send(what)                                # Reply with it.
        
    @bot.command()
    async def say2(ctx, *what):                             # Take words as tokens delimited with space.
        await ctx.send(" ".join(what))                      # Adjust words(tokens) with spaces.

    @bot.command()
    async def choices(ctx, *options): 
        await ctx.send(random.choice(options))              # Return one random element from tokens.

    @bot.command()
    async def say3(ctx, what = "WHAT?", why = "WHY?"):      # Take two words as token for what and why.
        await ctx.send(what + why)                          # Adjust two tokens.

    @bot.command()
    async def joined(ctx, who : discord.Member):            # Get discord member's name for input. *Case sensitive*
        nick = who.nick
        await ctx.send(f"{nick} has joined at {who.joined_at}")     # Show joined time.


    bot.run(settings.TOKEN, root_logger=True)

if __name__ == "__main__":
    run()