# loading.py
import discord
from discord.ext import commands

@commands.command()
async def loading_faq(ctx):
    disclaimer = ctx.get_channel(712641701268684850)
    pack_loading = ctx.get_channel(713145111965597718)

    await ctx.send("@everyone")

    embed = discord.Embed(title="FAQ | Pack Loading", description=f"Prices: {pack_loading.mention}", color=0xF5942D)
    embed.add_field(name="**Is pack loading legal?**", value="Yes, pack loading is 100% legal and safe.", inline=False)
    embed.add_field(name="**Can I get banned for having my packs loaded?**",
                    value="Pack loading is against Warner Bros T&C, but it is impossible for them to detect it unless "
                          "you openly mention it in a game chat.",
                    inline=False)
    embed.add_field(name="**Is my information safe?**",
                    value=f"Yes, in our {disclaimer.mention} we guarantee discrete and confidential services.",
                    inline=False)
    embed.add_field(name="**How does payment work?**",
                    value="We accept PayPal and Revolut as payment methods. Once we are ready to begin your order, "
                          "we will take payment. All currencies are accepted, but we need them converted to USD. When "
                          "using PayPal, always send as Friends & Family.",
                    inline=False)
    embed.add_field(name="**What is the account login process?**",
                    value="Once we receive your FaceBook login information, we will use it to sign into your FB bound "
                          "game account. We will go straight to the pack shop and purchase your pack. Once the pack "
                          "is purchased we will log out of your FaceBook account, remove it from our device, "
                          "and exit the game account as well.",
                    inline=False)
    embed.add_field(name="**Where do I go to make an order?**",
                    value="After you have agreed to our #disclaimer by ticking the green checkmark, you can go to "
                          "#place-an-order and open a ticket with **-ticket open `service`**. What is a ticket? A "
                          "ticket is a temporary channel created by the customer, where we conduct our orders. Once "
                          "the order is complete you can close the ticket. Only the customer and their staff will "
                          "have access. Tickets maximize security and privacy.",
                    inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")

    await ctx.send(embed=embed)
    await ctx.message.delete()
    
# LOADING SERVICE
@commands.command()
async def loading_page(ctx):
    embed = discord.Embed(title="Our Pack Loading Page", description="-Information\n"
                                                                     "-Prices", color=0xF5942D)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def loading_info(ctx):
    how_to_order = ctx.get_channel(712630999321935926)
    disclaimer = ctx.get_channel(712641701268684850)
    place_order = ctx.get_channel(712649074041421875)

    embed = discord.Embed(title="Information", description=f"Our disclaimer: {disclaimer.mention}\n"
                                                           f"How to order: {how_to_order.mention}", color=0xF5942D)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="> **What is pack loading?**",
                    value="Pack loading is a way of buying in-app purchases in some "
                          "games for much less than you would normally pay. It "
                          "involves arbitrage, which is a fancy word for finding "
                          "loopholes through currency exchange rates.\n"
                          "\n"
                          "We'll need your FaceBook login so we can enter your bound account. Once logged in we will "
                          "buy the requested pack. Yes, it's that simple.", inline=False)
    embed.add_field(name="> **How we make profit**",
                    value="Using the concept I just explained, we are paying much less than the pack would normally "
                          "cost. Say for example loaders pay 80 USD for a pack worth 100 USD, they would ask you to "
                          "send 85 USD. Making $5 profit.", inline=False)
    embed.add_field(name="> **Special Request for Apple users**",
                    value="The WarnerBros pack cycle for GoTC is different for Android and IOS devices, meaning you "
                          "may see the pack you want on your phone but when we log in it might not appear. This is "
                          "best prevented by you closing your game an hour before making your order. This will let us "
                          "load your pack *much* faster.", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def loading_prices(ctx):
    embed = discord.Embed(title="Prices", description="Prices listed in USD. We take all currencies, priced according "
                                                      "to exchange rate.", color=0xF5942D)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="**Large Pack**",
                    value="$85 - £64 - €71",
                    inline=False)
    embed.add_field(name="**Medium Pack**",
                    value="$45 - £34 - €37")
    embed.add_field(name="**Kingdom Launch Deal**",
                    value="Tobho + Whent + 14-day delivery = $38 - £28 - €32\n"
                          "\n"
                          "\n"
                          "`When sending money, make sure we receive these exact amounts in the "
                          "currency we request ( "
                          "usually USD or EUR)`")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command()
async def temp_loading_prices(ctx):
    embed = discord.Embed(title="Prices", description="We receive these amounts, regardless of fees.", color=0xF5942D)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.add_field(name="**Large Pack**",
                    value="$90 - £68 - €75\n"
                          "\n"
                          "🌟 Pre-Orders\n"
                          "$85 - £64 - €71",
                    inline=False)
    embed.add_field(name="**Medium Pack**",
                    value="$47 - £36 - €40\n"
                          "\n"
                          "🌟 Pre-Orders\n"
                          "$45 - £35 - €38")
    embed.add_field(name="**Kingdom Launch Deal**",
                    value="Tobho + Whent + 14-Day Delivery\n"
                          "$42 - £32 - €36\n", inline=False)
    await ctx.send(embed=embed)
    sembed = discord.Embed(title="Warning: Apple Users", description="Please have your game closed for 1 hour before "
                                                                     "your order.", color=discord.colour.Color.red())
    sembed.set_footer(text="Read info to know more")
    await ctx.send(embed=sembed)
    await ctx.message.delete()

def setup(bot):
    bot.add_command(loading_faq)
    bot.add_command(loading_page)
    bot.add_command(loading_prices)
    bot.add_command(temp_loading_prices)t