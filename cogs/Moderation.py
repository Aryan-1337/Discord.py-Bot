import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick Command
    @commands.command(name="kick", help="Kicks A User From The Server.", usage="kick <user> [reason]")
    @commands.cooldown(1, 30, commands.BucketType.user)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "No Reason Provided."

        kick_reason = f"Kicked By {ctx.author} (ID: {ctx.author.id}) With Reason: {reason}"

        await member.kick(reason=kick_reason)
        await ctx.send(f"Successfully Kicked {member} With Reason: **`{reason}`**")

    # Kick Error
    @kick.error
    async def kick_error(self, ctx, error):
        embed = discord.Embed(title="Error", description=f"{error}", color=0xFF0000)
        await ctx.send(embed=embed)

    # Ban Command
    @commands.command(name="ban", help="Bans A User From The Server.", usage="ban <user> [reason]")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ban(self, ctx, member: discord.User, *, reason=None):
        if reason == None:
            reason = "No Reason Provided."

        ban_reason = f"Banned By {ctx.author} (ID: {ctx.author.id}) With Reason: {reason}"

        await ctx.guild.ban(member, reason=ban_reason)
        await ctx.send(f"Successfully Banned {member} With Reason: **`{reason}`**")

        # Ban Error
    @ban.error
    async def ban_error(self, ctx, error):
        embed = discord.Embed(title="Error", description=f"{error}", color=0xFF0000)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
