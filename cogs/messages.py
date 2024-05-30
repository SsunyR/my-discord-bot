import discord
from discord.ext import commands
import random

# Simple check if message owner is guild owner
async def is_owner(ctx):
    return ctx.author.id == ctx.guild.owner_id

class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # Configuration of the command. Can be shown with "!help ping"
    @commands.command(
            # Set aliases for the command. Enable "!p | !help p".
            aliases = ['p'],
            # Guide of the command. How to use this command.
            help = "Type !ping or !p on the channel",
            # Discription part of the bot
            description = "This command will answer with pong",
            # Brief description of the command. Shows when !help typed.
            brief = "Answers with pong."
            # # To make this command enable or not.
            # enabled = False,
            # # To make this command hidden or not.
            # hidden = True
    )
    # ctx: Various information such as message, channel, guild etc.
    async def ping(self, ctx):
        # Brief description of this command. Replaced with brief.
        """ Answers with pong. """
        await ctx.send("pong")

    # Check permission with is_owner
    @commands.command()
    @commands.check(is_owner)
    # @commands.is_owner
    # Only take single word. Default "WHAT?."
    async def say(self, ctx, what = "WHAT?"):
        # Reply
        await ctx.send(what)

    @say.error
    async def say_error(ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Permission denied.")
        
    
    @commands.command()
    # Take words as tokens delimited with space.
    async def say2(self, ctx, *what):
        # Adjust words(tokens) with spaces.
        await ctx.send(" ".join(what))
    

    @commands.command()
    async def choices(self, ctx, *options): 
        # Return one random element from tokens.
        await ctx.send(random.choice(options))

    @commands.command()
    # Take two words as token for what and why.
    async def say3(self, ctx, what = "WHAT?", why = "WHY?"):
        # Adjust two tokens.
        await ctx.send(what + why)

async def setup(bot):
    await bot.add_cog(Messages(bot))