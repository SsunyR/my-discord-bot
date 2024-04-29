import settings

#[D] = Discord
import discord
from discord.ext import commands

#[L] = Logger
logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()                     # Enable all type of intents. Only for developing.

    # Choose intent types to enable
    # intents = discord.Intents.default()
    # intents.message_content = True # Enable message intents

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():                                           # When bot is online.
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")        # Show message with the format I set.

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

        
    bot.run(settings.TOKEN, root_logger=True)

if __name__ == "__main__":
    run()