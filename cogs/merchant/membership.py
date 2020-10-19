# userdata.py
import discord
from discord.ext import commands

# Customer Information
store_credit = 0
store_total = 0
total_spent = '$' + str(store_total) + '.00'


@commands.command()
async def upgrade(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)

    embed_color = 0x9e805b

    image_id = '736375721882026074'
    image_name = 'Bronze'

    if role.id == 735272119310483587:
        await member.remove_roles(ctx.guild.get_role(735272169054928942))
        embed_color = 0xc2c0c0
        image_id = '736375709261627397'
        image_name = 'Silver'
    if role.id == 735272070992232529:
        await member.remove_roles(ctx.guild.get_role(735272119310483587))
        embed_color = 0xe9c657
        image_id = '736375692186484751'
        image_name = 'Gold'
    if role.id == 735272021411233902:
        await member.remove_roles(ctx.guild.get_role(735272070992232529))
        embed_color = 0x8ca1d4
        image_id = '736375672938692618'
        image_name = 'Diamond'
    if role.id == 735271929828737166:
        await member.remove_roles(ctx.guild.get_role(735272021411233902))
        embed_color = 0xda5555
        image_id = '736375651887480982'
        image_name = 'Executive'

    card = 'https://cdn.discordapp.com/attachments/736374327607296111/' + image_id + '/Bazaar' + image_name + \
           'Thumbnail.jpg '

    print(f"{member} has been upgraded to {role}")
    embed = discord.Embed(title=f"⬆️ | {member} upgraded to `{role}`!", description='Check customer card with `,rank`',
                          color=embed_color)
    embed.set_thumbnail(url=f"{card}")
    embed.add_field(name=f"{role} __Perks__", value=f"🔥 {role} Ticket Priority\n"
                                                    "🔥 Request for specific Hunter\n"
                                                    "🔥 Request for specific Loader")
    await ctx.send(embed=embed)


# Information Pulling
@commands.command()
async def userinfo(ctx, member: discord.Member):
    member = member or ctx.message.author
    tempo = member.joined_at
    cr_time = member.created_at
    f_date = tempo.strftime("%d/%m/%Y")
    f_time = tempo.strftime("%H:%M:%S")
    cr_date = cr_time.strftime("%d/%m/%Y")
    c_time = cr_time.strftime("%H:%M:%S")

    embed = discord.Embed(title=f'User: {member}')
    embed.add_field(name="User ID", value=f"{member.id}")
    embed.add_field(name="Joined server", value=f"{f_date} at {f_time}", inline=False)
    embed.add_field(name="Account created", value=f"{cr_date} at {c_time}", inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def rank(ctx, member: discord.Member = None):
    member = member or ctx.message.author
    ranks = [735271929828737166, 735272021411233902, 735272070992232529, 735272119310483587, 735272169054928942]
    roles = [role.id for role in member.roles]
    shared = [role_id for role_id in ranks if role_id in roles]

    highest_role = ctx.guild.get_role(shared[-1])
    next_rank = ctx.guild.get_role(735272169054928942)

    image_id = ''

    if highest_role.id == 735272169054928942:
        image_id = '736375721882026074'
        next_rank = ctx.guild.get_role(735272119310483587)
    if highest_role.id == 735272119310483587:
        image_id = '736375709261627397'
        next_rank = ctx.guild.get_role(735272070992232529)
    if highest_role.id == 735272070992232529:
        image_id = '736375692186484751'
        next_rank = ctx.guild.get_role(735272021411233902)
    if highest_role.id == 735272021411233902:
        image_id = '736375672938692618'
        next_rank = ctx.guild.get_role(735271929828737166)
    if highest_role.id == 735271929828737166:
        image_id = '736375651887480982'
        next_rank = ctx.guild.get_role(735951836380659732)

    card = 'https://cdn.discordapp.com/attachments/736374327607296111/' + image_id + '/Bazaar' + highest_role.name.strip() + 'Thumbnail.jpg '

    rank_info = client.get_channel(735873994623942716)

    embed = discord.Embed(description=f"Customer: {member.mention}")
    embed.add_field(name="Rank", value=f"{highest_role.mention}", inline=True)
    embed.add_field(name=f"Next Rank", value=f"{next_rank.mention}", inline=True)
    embed.add_field(name="💵 Credit", value=f"{store_credit}", inline=False)
    embed.add_field(name="🎉 Giveaway Wins", value=f"{giveaways_won}", inline=False)
    embed.add_field(name='━━━━━━━━━━━━━━', value=f"Visit {rank_info.mention}", inline=False)
    embed.set_thumbnail(url=f"{card}")
    embed.set_author(name="💳 Bazaar Customer Card")

    await ctx.send(embed=embed)
    await ctx.message.delete(delay=5)


# Error Handlers
@rank.error
async def unregistered_customer(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        disclaimer = client.get_channel(712641701268684850)
        place_order = client.get_channel(712649074041421875)
        faq = client.get_channel(727844667965702164)

        embed = discord.Embed(description=f"{ctx.author.mention}, make an order to get a rank today!")
        embed.set_author(name="User Not Registered")
        embed.add_field(name='Step 1', value=f"For permissions, first agree to: {disclaimer.mention}", inline=False)
        embed.add_field(name='Step 2', value=f"Visit the 'Services' category to find what you want", inline=False)
        embed.add_field(name='Step 3', value=f"Type **-ticket open `service`** in {place_order.mention}", inline=False)
        embed.add_field(name="━━━━━━━━━━━━━━", value=f"Questions? First visit our FAQ ({faq.mention})")
        embed.set_footer(text=f"Additional guidance will be provided within your ticket.")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(upgrade)
    bot.add_command(userinfo)
    bot.add_command(rank)