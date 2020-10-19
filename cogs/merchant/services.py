# services.py
import discord
from discord.ext import commands
# FAQ POSTS
@commands.command()
async def farming_faq(ctx):
    disclaimer = client.get_channel(712641701268684850)
    resources = client.get_channel(712650458229112902)

    #await ctx.send("@everyone")

    embed = discord.Embed(title="FAQ | Resource Farming", description=f"Prices: {resources.mention}", color=0x23D886)
    embed.add_field(name="**How does it work?**", value="We create a multitude of alt accounts with many resources in "
                                                        "each one and then teleport them to your desired location. "
                                                        "Then you can hit the alts and farm the resources.",
                    inline=False)
    embed.add_field(name="**How long does it take?**",
                    value="Largely depending on the amount of resources ordered, the alt-making can take up to "
                          "several hours. We have multiple team members working on your order to complete it as fast "
                          "as possible.",
                    inline=False)
    embed.add_field(name="**What if someone else steals the resources?**",
                    value=f"We do not take responsibility for third-party attacks, but before starting we will work "
                          f"with you to locate the safest and most discrete spots to prevent this from happening.",
                    inline=False)
    embed.add_field(name="**What do I need to do?**",
                    value="We do all the hard work, all you need to do is hit the alts as we deliver them to you. If "
                          "the order is big you may have better things to do.. No problem at all! In that case we "
                          "alaways offer the option to farm it for you.",
                    inline=False)
    embed.add_field(name="**Do you need my login?**",
                    value="We will not ask for your login unless we are farming the rss for you.",
                    inline=False)
    embed.add_field(name="**Do you provide resources outside of events?**",
                    value="We don't make alts outside of events because it takes much longer and is extremely "
                          "inefficient.",
                    inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")

    await ctx.send(embed=embed)
    await ctx.message.delete()




# SECRET MARKET
@commands.command()
async def secret_market(ctx):
    how_to_order = client.get_channel(741965740151799889)
    customer = ctx.guild.get_role(712733451941576757)
    embed = discord.Embed(title="Dark Bazaar - The Secret Market", description=f"{customer.mention} Only",
                          color=0xf0ad1f)
    embed.set_author(name="Oxygen's Bazaar [VIP]")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/736374327607296111/745278474713038848/BazaarDark.png")
    embed.add_field(name="**Services**", value=f"> **🎉 Raffles**\n"
                                               f"> Get packs and accounts with cheap raffle entries!\n"
                                               f"\n"
                                               f"> **⚒️ Amoury Improvement**\n"
                                               f"> We will use our skillful luck to strengthen your armoury.\n"
                                               f"\n"
                                               f"> **⛺ SoP Camping**\n"
                                               f"> We will surround your SoP with alts, decimating the enemy "
                                               f"advantage!\n "
                                               f"\n"
                                               f"> **🏰 Keep-Sitting**\n"
                                               f"> Date night? Emergency? We will keep growing your account.")
    sembed = discord.Embed(description=f"Visit {how_to_order.mention} and make your first purchase!",
                           color=discord.Color.red())
    sembed.set_author(name=f"Become a {customer} today!")
    await ctx.send(embed=embed)
    await ctx.send(embed=sembed)
    await ctx.message.delete()


# ARMOURY IMPROVEMENT
@commands.command()
async def armory(ctx):
    embed = discord.Embed(title="Armoury Improvement", description="The armoury is one of the most important aspects "
                                                                   "of GoTC. We are proud to offer you our hand in "
                                                                   "bringing your game to the next level. Let us take "
                                                                   "care of your sets with the cheapest and safest "
                                                                   "crafting method out there.", color=0x7779ec)
    embed.set_author(name="Oxygen's Bazaar")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.set_footer(text="We can advise you but we do not share or sell our methods.")
    embed.add_field(name="> **Deals**", value="> **Level**\n"
                                              "> example - price\n"
                                              "> example - price\n"
                                              "> waiting for dark!!!")

    sembed = discord.Embed(title="Instagram Showcase", description="> `◆` Payment not taken if unsuccessful\n"
                                                                   "> `◆` Fast Service\n"
                                                                   "> `◆` Lucky\n"
                                                                   "\n"
                                                                   "See what we've done for our customers on our "
                                                                   "Instagram page!\n "
                                                                   "\n", color=0xE1306C)
    sembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736374327607296111/745335658817650698"
                             "/BazaarInstagram.png")
    sembed.add_field(name="Visit IG:", value="[Oxygen's Bazaar](https://www.instagram.com/oxygensbazaar/)")
    await ctx.send(embed=embed)
    await ctx.send(embed=sembed)

# SOP CAMPING
@commands.command()
async def camping(ctx):
    embed = discord.Embed(title="SoP Camping", description="The SoP Camping service will ensure that spots around "
                                                           "your SoP are secured, so enemies can't port nearby. We "
                                                           "will leave the initial 5-day shield on.", color=0x7779ec)
    embed.set_author(name="Oxygen's Bazaar")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="**Deals**",
                    value=f"> **Paramount Encampment**\n"
                          f"> 1 Layer - $10\n"
                          f"> 2 Layers - $15\n"
                          f"> 3 Layers - $25\n"
                          f"\n"
                          f"> **Lockable Encampment**\n"
                          f"> 1 Layer - $5\n"
                          f"> 2 Layers - $10\n"
                          f"> 3 Layers - $15", inline=False)
    embed.add_field(name="> **Reservations**", value=
    "> We will bind any given amount of alts to swap spots whenever you need!\n"
    "> $2.50 per alt")
    embed.set_footer(text="We cannot guarantee that another keep will be positioned before we set the encampment. "
                          "Therefore please plan and make your order in advance.")
    await ctx.send(embed=embed)
    await ctx.message.delete()

# KEEP-SITTING

# RESOURCE SERVICE
@commands.command()
async def resource_page(ctx):
    embed = discord.Embed(title="Our Resource Page", description="-Information\n"
                                                                 "-Prices", color=0x23D886)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def resource_info(ctx):
    how_to_order = client.get_channel(712630999321935926)
    disclaimer = client.get_channel(712641701268684850)
    place_order = client.get_channel(712649074041421875)

    embed = discord.Embed(title="Information", description=f"Our disclaimer: {disclaimer.mention}\n"
                                                           f"How to order: {how_to_order.mention}", color=0x23D886)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="> **What is resource farming?**",
                    value="We will make alts with resources and then teleport "
                          "them                                                   where you want. From there the alts can be "
                          "farmed (hit) from your account to gather their "
                          "resources.", inline=False)
    embed.add_field(name="> **What do I need to do as customer?**",
                    value="1. Send us the friend code for your kingdom.\n"
                          "2. Send us your coordinates.\n "
                          "3. Hit the alts as we deliver *or* have us do it for you (read below).", inline=False)
    embed.add_field(name="> **Alt Farming (optional)**",
                    value="As we make the alts there needs to be consistent alt "
                          "farming and porting from your account to make space for "
                          "the new alts. We totally get it if you don't have the "
                          "time to keep this up for a long time and that's why we "
                          "can do it all for you. If you decide to use this "
                          "sub-service we will need your FaceBook login "
                          "information. Check below for pricing.", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def resource_prices(ctx):
    embed = discord.Embed(title="Prices", description="Food and wood have the same prices. You can mix if you'd like. "
                                                      "We open all boxes so you get the most of out each alt. Prices "
                                                      "vary by event, and we do not offer this service without "
                                                      "building events.",
                          color=0x23D886)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="**Varys / Preparing for War / Total Powers**", value="100m wood/food = $17.50 - £13 - €14\n"
                                                                               "200m wood/food = $35 - £26 - €29\n"
                                                                               "500m wood/food = $70 - £53 - €58\n"
                                                                               "1B wood/food = $140 - £106 - €117\n"
                                                                               "2B wood/food = $275 - £209 - €231\n"
                                                                               "5m iron 80m wood/food each "
                                                                               "= 80$ - £68 - €62\n "
                                                                               "10m iron 160m wood/food each "
                                                                               "= $150$ - £127 - €115\n "
                                                                               "20m iron 320 wood/food each"
                                                                               "= 300$ - £255 - €230", inline=False)
    embed.add_field(name="**Rich Man's Shadow**", value="100m wood/food = $30 - £22 - €25\n"
                                                        "200m wood/food = $60 - £45 - €50\n"
                                                        "500m wood/food = $120 - £91 - €101\n"
                                                        "1B wood/food = $230 - £175 - €193\n"
                                                        "1m iron + 20m wood/food each "
                                                        "= $25 - £22 - €20\n"
                                                        "5m iron + 110m wood/food each "
                                                        "= 145$ - £123 - €111\n"
                                                        "10m iron + 220m wood/food each "
                                                        "= 280$ - £240 - €215", inline=False)
    embed.add_field(name="**Additional Alt Farming**", value="Cost depends on:\n"
                                                             "-Order size\n"
                                                             "-March count\n"
                                                             "-Troop load\n"
                                                             "-Troop tier\n"
                                                             "-March cap/speed\n"
                                                             "-Siege wall power")
    sembed = discord.Embed(title="Notice",
                           description="Due to a large demand of resource orders, we suggest you open a ticket ahead of "
                                       "time to save a spot in line. Please be specific when telling us what you want. We "
                                       "can help you calculate needs for your progress as well.",
                           color=discord.colour.Color.red())
    await ctx.send(embed=embed)
    await ctx.send(embed=sembed)
    await ctx.message.delete()

def setup(bot):
    bot.add_command(farming_faq)
    bot.add_command(secret_market)
    bot.add_command(camping)
    bot.add_command(armory)
    bot.add_command(resource_page)
    bot.add_command(resource_info)
    bot.add_command(resource_prices)
    