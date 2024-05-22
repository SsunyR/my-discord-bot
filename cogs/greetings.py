# This file is for command collection with cog.

import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # Reactioning on messages
    async def on_message(self, message: discord.Message):
        await message.add_reaction("✅")

    @commands.command()
    # Say hello to channel member. !hello (channel member)
    async def hello(self, ctx, *, member: discord.Member):
        await ctx.send(f"Hello {member.name}")

async def setup(bot):
    await bot.add_cog(Greetings(bot))