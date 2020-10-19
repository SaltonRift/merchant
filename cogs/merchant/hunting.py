#   hunting.py
import asyncio
import discord
from discord.ext import commands

@commands.command()
async def hunting_faq(ctx):
    disclaimer = ctx.get_channel(712641701268684850)
    farming = ctx.get_channel(712650458229112902)
    hunting = ctx.get_channel(713145070836121640)

    await ctx.send("@everyone")

    embed = discord.Embed(title="FAQ | Hunting", description=f"Prices: {hunting.mention}", color=0x2368D8)
    embed.add_field(name="**How does it work?**",
                    value="One of our hunters will log into your account and hunt creatures for you.",
                    inline=False)
    embed.add_field(name="**How long does it take?**",
                    value="Hunting (also known as farming) can take a very long time, especially when you are aiming "
                          "for high house levels or expensive development, from a few hours to a day or two. That's "
                          "why this service is such a blessing, you can catch up on sleep, work, and spend time with "
                          "others while we get that grind for you.",
                    inline=False)
    embed.add_field(name="**How powerful do I need to be?**",
                    value=f"We will work with what you have, but if your account is a bit weak it will take *much* "
                          f"longer to complete your order, and consequently we will either ask for a higher price or "
                          f"smaller order.",
                    inline=False)
    embed.add_field(name="**Do I need to buy the gold?**",
                    value="Yes, hunting huge amounts will require lots of gold for stamina and teleports. Providing "
                          "the gold for this is not a part of our service.",
                    inline=False)
    embed.add_field(name="**Do you need my login?**",
                    value="Of course.",
                    inline=False)
    embed.add_field(name="**What about the healing bill?**",
                    value=f"Good question, depending on how much march power you have and the target creature, "
                          f"the healing bill might be pretty high. To minimise the food spent you could craft a good "
                          f"healing set. You are expected to have all the necessary food. (Need more food? We can top "
                          f"you up during events: {hunting})",
                    inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")

    await ctx.send(embed=embed)
    await ctx.message.delete()
    
    # HUNTING SERVICE
@commands.command()
async def hunting_page(ctx):
    embed = discord.Embed(title="Our Hunting Page", description="-Information\n"
                                                                "-Prices", color=0x2368D8)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def hunting_info(ctx):
    how_to_order = ctx.get_channel(712630999321935926)
    disclaimer = ctx.get_channel(712641701268684850)
    place_order = ctx.get_channel(712649074041421875)

    embed = discord.Embed(title="Information", description=f"Our disclaimer: {disclaimer.mention}\n"
                                                           f"How to order: {how_to_order.mention}", color=0x2368D8)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="> **What is hunting?**",
                    value="Hunting is also known as farming, we call it hunting to easily "
                          "distinguish between resource farming and farming creatures.\n"
                          "\n"
                          "1. We log into your account via FaceBook.\n"
                          "2. We hunt creatures for you.\n"
                          "\n"
                          "This is very useful when you need to get enough advanced "
                          "materials to make that jump for expensive construction or "
                          "research. The grind will take hours, and we'll do it all for "
                          "you. "
                          "You may need to climb to a high house level. Why spend the "
                          "entire "
                          "day "
                          "killing creatures when you have work to do and people to spend "
                          "time with? Yeah it's a complete waste of time and that's why "
                          "we "
                          "get it done for you.", inline=False)
    embed.add_field(name="> **What are the requirements?**",
                    value="1. You provide all the gold for teleports and stamina.\n"
                          "2. Level 33+ creatures can be defeated with four "
                          "marches.\n "
                          "3. You have enough provisions for the healing bill.", inline=False)
    embed.add_field(name="> 📅**Caravan Hunting Days**", value="Monday - Scholarly Fragments\n"
                                                               "Tuesday - Bricks\n"
                                                               "Wednesday - Pale Steel Shards\n"
                                                               "Thursday - Pine", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def hunting_prices(ctx):
    embed = discord.Embed(title="Prices", description="Prices are listed assuming you meet requirements. If you "
                                                      "contact us we can find a custom price if you do not meet the "
                                                      "requirements.", color=0x2368D8)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="**Advanced Materials**", value="25k Scholarly Fragments/Bricks - $10 - £7 - €8\n"
                                                         "10k Pale Steel Shards/Pine - $10 - £7 - €8\n"
                                                         "\n"
                                                         "100k Scholarly Fragments/Bricks - $40 - £30 - €34\n"
                                                         "40k Pale Steel Shards/Pine - $40 - £30 - €34\n"
                                                         "\n"
                                                         "200k Scholarly Fragments/Bricks - $75 - £57 - €63\n"
                                                         "80k Pale Steel Shards/Pine - $75 - £57 - €63\n"
                                                         "\n"
                                                         "500k Scholarly Fragments/Bricks - $185 - £140 - €155\n"
                                                         "200k Pale Steel Shards/Pine - $185 - £140 - €155",
                    inline=False)
    embed.add_field(name="**Prestige**", value="5m Prestige = $25 - £19 - €21\n"
                                               "10m Prestige = $50 - £38 - €42\n"
                                               "20m Prestige = $95 - £72 - €80\n"
                                               "50m Prestige $235 - £179 - €198\n"
                                               "\n"
                                               "\n"
                                               "`When sending money, make sure we receive these exact amounts in the "
                                               "currency we request ( "
                                               "usually USD or EUR)`")
    await ctx.send(embed=embed)
    await ctx.message.delete()

def setup(bot):
    bot.add_command(hunting_faq)
    bot.add_command(hunting_page)
    bot.add_command(hunting_info)
    bot.add_command(hunting_prices)
    