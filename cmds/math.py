from discord.ext import commands

@commands.group()                                       # Make the group of commands.
async def math(ctx):                                    # Function name is going to be the group name.
    if ctx.invoked_subcommand is None:                  # Error handling for unmatched sub_command.
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")

@math.command()                                         # bot.command() -> math.command() # Group the command.
async def add(ctx, one : int, two : int):               # Set the type of input value.
    await ctx.send(one + two)                           # Return added result of two input values.

@add.error                                              # Set error handler for the command "!add".
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):     # If argument is missing.
        await ctx.send("handled error locally")
            
@math.command()
async def substract(ctx, one : int, two : int):
    await ctx.send(one - two)

# setup function to access the bot instance
async def setup(bot):
    bot.add_command(math)
    bot.add_command(add)